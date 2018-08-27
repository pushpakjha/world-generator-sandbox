# Main simulation loop file
import collections


class World(object):
    """Main world object."""
    def __init__(self):
        self.time = 0
        self.world_map = collections.defaultdict(dict)
        self.global_bacteria = []


class SimulateWorld(object):
    """Execute the simulation on a world object.

    :param World world: The world object
    :param int end_time: Number of seconds to simulate world
    """
    def __init__(self, world, end_time):
        self.world = world
        self.end_time = end_time
        self.global_bacteria = world.global_bacteria

    def execute(self):
        """Main execute function, runs in a loop until time has elapsed."""
        while self.end_time:
            self.execute_second()
            self.end_time -= 1
            self.world.time += 1

    def execute_second(self):
        """Run one second of the simulation."""
        for bacteria in self.global_bacteria:
            bacteria.execute_second(self.world)
