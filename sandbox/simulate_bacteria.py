# Definitions of the simulated bacteria in the world.
import abc


class Bacteria(object):
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int child_counter: The id of the parent to this child, if this is a child else None
    """
    def __init__(self, max_lifetime, child_counter=None, reproduction_rate=5):
        self.current_lifetime = 0
        self.max_lifetime = max_lifetime
        self.child_counter = child_counter
        self.reproduction_rate = reproduction_rate

    def execute_second(self, world):
        """Add to the lifetime and perform basic life checks.

         :param sandbox.simulation_world.World world: The world object
        """
        self.current_lifetime += 1
        if self.current_lifetime >= self.max_lifetime:
            self.die(world)
        if self.current_lifetime % self.reproduction_rate == 0:
            self.reproduce(world)

    def die(self, world):
        """Kill the bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        world.global_bacteria.remove(self)

    def reproduce(self, world):
        """Make a new child bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        self.child_counter += 1
        child = self(self.max_lifetime,  self.global_bacteria, self.child_counter, self.reproduction_rate)
        world.global_bacteria.append(child)
