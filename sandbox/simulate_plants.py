"""Definitions of the simulated plants in the world."""
from sandbox import simulate_bacteria
from sandbox import utils


class GrassPlant(simulate_bacteria.Bacteria):
    """Basic grass plant.

    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """
    DEATH_CONCENTRATION = 5

    def __init__(self, max_lifetime, x_position, y_position):
        super(GrassPlant, self).__init__(max_lifetime, x_position, y_position, reproduction_rate=8)

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def _die(self, world):
        """Kill the nitrogen bacteria.

        :param sandbox.simulation_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        world.global_plants.remove(self)

    def reproduce(self, world):
        """Make a new child nitrogen bacteria.

        :param sandbox.simulate_world.World world: The world object
        :rtype: sandbox.simulate_bacteria.NitrogenBacteria
        """
        new_x_position, new_y_position = utils.get_new_position(
            self.x_position, self.y_position, world.max_x_size, world.max_y_size, 2)
        child = GrassPlant(self.max_lifetime, new_x_position, new_y_position)
        return child

    def check_death(self, world):
        """Check if nitrogen bacteria should die.

        :param sandbox.simulate_world.World world: The world object
        """
        x_y_key = utils.get_x_y_key(self.x_position, self.y_position)
        if world.world_map[x_y_key].nitrogen > self.DEATH_CONCENTRATION:
            self._die(world)
