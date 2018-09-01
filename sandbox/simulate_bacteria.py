"""Definitions of the simulated bacteria in the world."""
import abc

from sandbox import utils


class Bacteria:
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    :param int reproduction_rate: Seconds needed for each reproduction cycle
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, max_lifetime, x_position, y_position, reproduction_rate=8):
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
            self._die(world)
            return

        self.check_death(world)

        if self.current_lifetime % self.reproduction_rate == 0:
            child = self.reproduce()
            world.global_bacteria.append(child)

    @abc.abstractmethod
    def _die(self, world):
        """Override this method to define die behavior.

        :param sandbox.simulate_world.World world: The world object
        """

    @abc.abstractmethod
    def reproduce(self):
        """Override this method to define reproduction behavior."""

    @abc.abstractmethod
    def check_death(self, world):
        """Override this method to define check death behavior.

        :param sandbox.simulate_world.World world: The world object
        """


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

    def _die(self, world):
        """Kill the nitrogen bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].nitrogen += 1
        world.global_bacteria.remove(self)

    def reproduce(self):
        """Make a new child nitrogen bacteria."""
        child = NitrogenBacteria(self.x_position, self.y_position)
        return child

    def check_death(self, world):
        """Check if nitrogen bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].nitrogen > 50:
            self._die(world)


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

    def _die(self, world):
        """Kill the phosphorus bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].phosphorus += 1
        world.global_bacteria.remove(self)

    def reproduce(self):
        """Make a new child phosphorus bacteria."""
        child = PhosphorusBacteria(self.x_position, self.y_position)
        return child

    def check_death(self, world):
        """Check if phosphorus bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].phosphorus > 50:
            self._die(world)


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

    def _die(self, world):
        """Kill the oxygen bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].oxygen += 1
        world.global_bacteria.remove(self)

    def reproduce(self):
        """Make a new child oxygen bacteria."""
        child = OxygenBacteria(self.x_position, self.y_position)
        return child

    def check_death(self, world):
        """Check if oxygen bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].oxygen > 50:
            self._die(world)
