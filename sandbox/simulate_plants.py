"""Definitions of the simulated plants in the world."""
import abc
import random

from sandbox import simulate_bacteria
from sandbox import utils


class Plant:
    """Base plant object.

    :param int max_lifetime: How long the plant should live
    :param int x_position: The x position of this plant
    :param int y_position: The y position of this plant
    :param int reproduction_rate: Ticks needed for each reproduction cycle
    """
    __metaclass__ = abc.ABCMeta
    DEATH_CONCENTRATION = 4

    def __init__(self, max_lifetime, x_position, y_position, reproduction_rate=6):
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


class GrassPlant(Plant):
    """Basic grass plant.

    :param int x_position: The x position of this grass plant
    :param int y_position: The y position of this grass plant
    """
    DEATH_CONCENTRATION = 6

    def __init__(self, x_position, y_position):
        super(GrassPlant, self).__init__(max_lifetime=24, x_position=x_position,
                                         y_position=y_position,
                                         reproduction_rate=8)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def _die(self, world):
        """Kill the grass plant.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].plant_matter += 1
        world.world_map[x_y_key].carbon += 1
        self.spawn_bacteria(world)
        self.spawn_bacteria(world)
        self.spawn_bacteria(world)
        world.global_plants.remove(self)
        world.world_map[x_y_key].beings['grass'].remove(self)

    def reproduce(self, world):
        """Make a new child grass plant.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_plants.GrassPlant
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 2)
        child = GrassPlant(new_x_position, new_y_position)
        x_y_key = utils.get_x_y_key(new_x_position, new_y_position)
        world.global_plants.append(child)
        world.world_map[x_y_key].beings['grass'].append(child)

    def check_death(self, world):
        """Check if grass plant should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].nitrogen -= self.DEATH_CONCENTRATION * 3/self.max_lifetime
        world.world_map[x_y_key].phosphorus -= self.DEATH_CONCENTRATION * 1/self.max_lifetime
        world.world_map[x_y_key].potassium -= self.DEATH_CONCENTRATION * 1/self.max_lifetime
        if world.world_map[x_y_key].nitrogen <= self.DEATH_CONCENTRATION * 3 or \
           world.world_map[x_y_key].phosphorus <= self.DEATH_CONCENTRATION * 1 or \
           world.world_map[x_y_key].potassium <= self.DEATH_CONCENTRATION * 1:
            self._die(world)
            return
        if len(world.world_map[x_y_key].beings['grass']) > 12:
            self._die(world)
            return

    def spawn_bacteria(self, world):
        """Spawn new bacteria where grass died.

        :param sandbox.simulate_world.World world: The world object
        """
        rand_bacteria = random.randint(0, 7)
        if rand_bacteria in [0, 1, 6]:
            world.global_bacteria.append(simulate_bacteria.NitrogenBacteria(
                self.x_position, self.y_position))
        elif rand_bacteria in [2, 3]:
            world.global_bacteria.append(simulate_bacteria.PhosphorusBacteria(
                self.x_position, self.y_position))
        elif rand_bacteria in [4, 5]:
            world.global_bacteria.append(simulate_bacteria.PotassiumBacteria(
                self.x_position, self.y_position))


class TreePlant(Plant):
    """Basic tree.

    :param int x_position: The x position of this tree
    :param int y_position: The y position of this tree
    """
    DEATH_CONCENTRATION = 6

    def __init__(self, x_position, y_position):
        super(TreePlant, self).__init__(max_lifetime=180, x_position=x_position,
                                        y_position=y_position,
                                        reproduction_rate=20)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def _die(self, world):
        """Kill the tree.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].tree_matter += 10
        world.global_plants.remove(self)
        world.world_map[x_y_key].beings['tree'].remove(self)

    def reproduce(self, world):
        """Make a new child tree.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_plants.TreePlant
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 1)
        child = TreePlant(new_x_position, new_y_position)
        x_y_key = utils.get_x_y_key(new_x_position, new_y_position)
        world.global_plants.append(child)
        world.world_map[x_y_key].beings['tree'].append(child)

    def check_death(self, world):
        """Check if tree should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].plant_matter -= self.DEATH_CONCENTRATION * 5/self.max_lifetime
        world.world_map[x_y_key].carbon -= self.DEATH_CONCENTRATION * 4/self.max_lifetime
        world.world_map[x_y_key].nitrogen -= self.DEATH_CONCENTRATION * 1/self.max_lifetime
        world.world_map[x_y_key].phosphorus -= self.DEATH_CONCENTRATION * 1/self.max_lifetime
        world.world_map[x_y_key].potassium -= self.DEATH_CONCENTRATION * 1/self.max_lifetime
        if world.world_map[x_y_key].carbon <= self.DEATH_CONCENTRATION * 4 or \
           world.world_map[x_y_key].nitrogen <= self.DEATH_CONCENTRATION * 1 or \
           world.world_map[x_y_key].phosphorus <= self.DEATH_CONCENTRATION * 1 or \
           world.world_map[x_y_key].potassium <= self.DEATH_CONCENTRATION * 1:
            self._die(world)
            return
        if len(world.world_map[x_y_key].beings['tree']) > 2:
            self._die(world)
            return
