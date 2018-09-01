"""Definitions of the simulated plants in the world."""
import abc


class Plant:
    """Base plant object.

    :param int max_lifetime: How long the plant should live
    :param int x_position: The x position of this plant
    :param int y_position: The y position of this plant
    :param int reproduction_rate: Ticks needed for each reproduction cycle
    """
    __metaclass__ = abc.ABCMeta
    DEATH_CONCENTRATION = 3

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
            child = self.reproduce(world)
            world.global_plants.append(child)

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
