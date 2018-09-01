"""Definitions of the simulated bacteria in the world."""
from sandbox import utils


class Bacteria:
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    :param int reproduction_rate: Seconds needed for each reproduction cycle
    """
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
            child = utils.reproduce(self.__class__, self.max_lifetime, self.x_position,
                                    self.y_position)
            world.global_bacteria.append(child)

    def die(self, world):
        """Kill the bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        world.global_bacteria.remove(self)


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
