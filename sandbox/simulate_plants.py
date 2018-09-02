"""Definitions of the simulated plants in the world."""
import random

from sandbox import simulate_bacteria
from sandbox import utils


class GrassPlant(simulate_bacteria.Bacteria):
    """Basic grass plant.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """
    DEATH_CONCENTRATION = 3

    def __init__(self, max_lifetime, x_position, y_position):
        super(GrassPlant, self).__init__(max_lifetime, x_position, y_position,
                                         reproduction_rate=8)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def _die(self, world):
        """Kill the grass plant.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.world_map[x_y_key].plant_matter += 1
        world.world_map[x_y_key].carbon += 5
        world.world_map[x_y_key].nitrogen -= self.DEATH_CONCENTRATION * 2
        world.world_map[x_y_key].potassium -= self.DEATH_CONCENTRATION * 1
        self.spawn_bacteria(world)
        world.global_plants.remove(self)

    def reproduce(self, world):
        """Make a new child grass plant.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_bacteria.GrassPlant
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 2)
        child = GrassPlant(self.max_lifetime, new_x_position, new_y_position)
        world.global_plants.append(child)

    def check_death(self, world):
        """Check if grass plant should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].nitrogen <= self.DEATH_CONCENTRATION * 4 or \
           world.world_map[x_y_key].phosphorus <= self.DEATH_CONCENTRATION * 1 or \
           world.world_map[x_y_key].potassium <= self.DEATH_CONCENTRATION * 2:
            self._die(world)

    def spawn_bacteria(self, world):
        """Spawn new bacteria where grass died.

        :param sandbox.simulate_world.World world: The world object
        """
        rand_bacteria = random.randint(0, 4)
        if rand_bacteria in [0, 1, 2]:
            world.global_bacteria.append(simulate_bacteria.NitrogenBacteria(
                self.x_position, self.y_position))
        elif rand_bacteria in [3]:
            world.global_bacteria.append(simulate_bacteria.PhosphorusBacteria(
                self.x_position, self.y_position))
        elif rand_bacteria in [4]:
            world.global_bacteria.append(simulate_bacteria.PotassiumBacteria(
                self.x_position, self.y_position))
