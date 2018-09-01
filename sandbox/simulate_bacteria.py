"""Definitions of the simulated bacteria in the world."""
import abc


class Bacteria:
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    :param int reproduction_rate: Seconds needed for each reproduction cycle
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, max_lifetime, x_position, y_position, reproduction_rate=10):
        self.current_lifetime = 0
        self.max_lifetime = max_lifetime
        self.reproduction_rate = reproduction_rate
        self.x_position = x_position
        self.y_position = y_position

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

    @abc.abstractmethod
    def reproduce(self):
        """Override this method."""


class NitrogenBacteria(Bacteria):
    """Bacteria which make nitrogen.

    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """

    def __init__(self, x_position, y_position):
        super(NitrogenBacteria, self).__init__(max_lifetime=20, x_position=x_position,
                                               y_position=y_position)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def reproduce(self):
        """Make a new child bacteria.
        """
        child = NitrogenBacteria(self.x_position, self.y_position)
        return child


class PhosphorusBacteria(Bacteria):
    """Bacteria which make phosphorus.

    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """

    def __init__(self, x_position, y_position):
        super(PhosphorusBacteria, self).__init__(max_lifetime=20, x_position=x_position,
                                                 y_position=y_position)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def reproduce(self):
        """Make a new child bacteria.
        """
        child = PhosphorusBacteria(self.x_position, self.y_position)
        return child


class OxygenBacteria(Bacteria):
    """Bacteria which make oxygen.

    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """

    def __init__(self, x_position, y_position):
        super(OxygenBacteria, self).__init__(max_lifetime=20, x_position=x_position,
                                             y_position=y_position)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def reproduce(self):
        """Make a new child bacteria.
        """
        child = OxygenBacteria(self.x_position, self.y_position)
        return child
