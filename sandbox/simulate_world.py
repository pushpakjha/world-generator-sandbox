"""Main simulation loop file"""
import collections
import time

from sandbox import display_world


class World:
    """Main world object."""
    def __init__(self):
        self.time = 0
        self.world_map = collections.defaultdict(list)
        self.global_bacteria = []


class SimulateWorld:
    """Execute the simulation on a world object.

    :param World world: The world object
    :param int end_time: Number of seconds to simulate world
    :param list[sandbox.simulate_bacteria.Bacteria]|None initial_bacteria: Initial bacteria to seed
        the world with
    """
    def __init__(self, world, end_time, initial_bacteria=None):
        self.world = world
        self.end_time = end_time
        self.global_bacteria = world.global_bacteria
        if initial_bacteria:
            self.global_bacteria.extend(initial_bacteria)

    def execute(self):
        """Main execute function, runs in a loop until time has elapsed."""
        while self.end_time:
            self.execute_second()
            self.end_time -= 1
            self.world.time += 1
            display_world.plot_bacteria(self.world)
            time.sleep(0.1)

    def execute_second(self):
        """Run one second of the simulation."""
        for bacteria in self.global_bacteria:
            bacteria.execute_second(self.world)
