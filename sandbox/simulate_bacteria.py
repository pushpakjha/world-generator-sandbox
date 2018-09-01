"""Definitions of the simulated bacteria in the world."""


class Bacteria:
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int|None child_counter: The id of the parent to this child, if this is a child else None
    :param int reproduction_rate: Seconds needed for each reproduction cycle
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
        if self.current_lifetime > self.max_lifetime:
            self.die(world)
        if self.current_lifetime % self.reproduction_rate == 0:
            child = self.reproduce()
            world.global_bacteria.append(child)

    def die(self, world):
        """Kill the bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        world.global_bacteria.remove(self)

    def reproduce(self):
        """Make a new child bacteria.
        """
        if not self.child_counter:
            self.child_counter = 1
        else:
            self.child_counter += 1
        return self.__class__(self.max_lifetime, self.child_counter, self.reproduction_rate)


class NitrogenBacteria(Bacteria):
    """Bacteria which make nitrogen."""

    def __init__(self):
        super(NitrogenBacteria, self).__init__(max_lifetime=20)


class PhosphorusBacteria(Bacteria):
    """Bacteria which make phosphorus."""

    def __init__(self):
        super(PhosphorusBacteria, self).__init__(max_lifetime=20)


class OxygenBacteria(Bacteria):
    """Bacteria which make oxygen."""

    def __init__(self):
        super(OxygenBacteria, self).__init__(max_lifetime=20)
