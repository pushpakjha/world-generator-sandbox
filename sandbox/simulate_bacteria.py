"""Definitions of the simulated bacteria in the world."""
import abc

from sandbox import utils


class Bacteria:
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    :param int reproduction_rate: Ticks needed for each reproduction cycle
    """
    __metaclass__ = abc.ABCMeta
    DEATH_CONCENTRATION = 6

    def __init__(self, max_lifetime, x_position, y_position, reproduction_rate=2):
        self.current_lifetime = 0
        self.max_lifetime = max_lifetime
        self.reproduction_rate = reproduction_rate
        self.x_position = x_position
        self.y_position = y_position

    def execute_tick(self, world):
        """Add to the lifetime and perform basic life checks.

        :param sandbox.simulation_world.World world: The world object
        """
        self.current_lifetime += 1
        if self.current_lifetime > self.max_lifetime:
            self._die(world)
            return

        self.check_death(world)

        if self.current_lifetime % self.reproduction_rate == 0:
            self.reproduce(world)

    @abc.abstractmethod
    def _die(self, world):
        """Override this method to define die behavior.

        :param sandbox.simulate_world.World world: The world object
        """

    @abc.abstractmethod
    def reproduce(self, world):
        """Override this method to define reproduction behavior.

        :param sandbox.simulate_world.World world: The world object
        """

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
        super(NitrogenBacteria, self).__init__(max_lifetime=4, x_position=x_position,
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

    def reproduce(self, world):
        """Make a new child nitrogen bacteria.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_bacteria.NitrogenBacteria
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 1)
        child = NitrogenBacteria(new_x_position, new_y_position)
        world.global_bacteria.append(child)

    def check_death(self, world):
        """Check if nitrogen bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].nitrogen > self.DEATH_CONCENTRATION:
            self._die(world)


class PhosphorusBacteria(Bacteria):
    """Bacteria which make phosphorus.

    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """

    def __init__(self, x_position, y_position):
        super(PhosphorusBacteria, self).__init__(max_lifetime=2, x_position=x_position,
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

    def reproduce(self, world):
        """Make a new child phosphorus bacteria.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_bacteria.PhosphorusBacteria
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 1)
        child = PhosphorusBacteria(new_x_position, new_y_position)
        world.global_bacteria.append(child)

    def check_death(self, world):
        """Check if phosphorus bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].phosphorus > self.DEATH_CONCENTRATION:
            self._die(world)


class PotassiumBacteria(Bacteria):
    """Bacteria which make potassium.

    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """

    def __init__(self, x_position, y_position):
        super(PotassiumBacteria, self).__init__(max_lifetime=2, x_position=x_position,
                                                y_position=y_position)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def _die(self, world):
        """Kill the potassium bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].potassium += 1
        world.global_bacteria.remove(self)

    def reproduce(self, world):
        """Make a new child potassium bacteria.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_bacteria.PotassiumBacteria
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 1)
        child = PotassiumBacteria(new_x_position, new_y_position)
        world.global_bacteria.append(child)

    def check_death(self, world):
        """Check if potassium bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].potassium > self.DEATH_CONCENTRATION:
            self._die(world)
