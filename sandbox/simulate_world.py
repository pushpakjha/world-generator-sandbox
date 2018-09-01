"""Main simulation loop file"""
import pygame

from sandbox import display_world
from sandbox import utils

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)
WIDTH = 20
HEIGHT = 20


class World:
    """Main world object.

    :param int max_x_size: The x size of the world
    :param int max_y_size: The y size of the world
    """
    def __init__(self, max_x_size, max_y_size):
        self.max_x_size = max_x_size
        self.max_y_size = max_y_size

        self.time = 0
        self.world_map = {}
        for x_val in range(0, self.max_x_size):
            for y_val in range(0, self.max_x_size):
                x_y_key = utils.get_x_y_key(x_val, y_val)
                self.world_map[x_y_key] = Land(x_val, y_val)
        self.global_bacteria = []


class Land:
    """Object to represent a piece of land.

    :param int x_position: The x position of their piece of land
    :param int y_position: The y position of their piece of land
    :param int oxygen: The amount of oxygen
    :param int nitrogen: The amount of nitrogen
    :param int phosphorus: The amount of phosphorus
    :param list[Any] beings: A list of any things living in this piece of land
    """
    def __init__(self, x_position, y_position, oxygen=0, nitrogen=0, phosphorus=0, beings=None):
        self.x_position = x_position
        self.y_position = y_position
        self.oxygen = oxygen
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.beings = []
        if beings:
            self.beings.extend(beings)


class SimulateWorld:
    """Execute the simulation on a world object.

    :param World world: The world object
    :param int end_time: Number of seconds to simulate world
    :param list[sandbox.simulate_bacteria.Bacteria]|None initial_bacteria: Initial bacteria to seed
        the world with
    """
    def __init__(self, world, end_time, initial_bacteria=None):
        self.world = world
        self.end_time = end_time
        self.global_bacteria = world.global_bacteria
        if initial_bacteria:
            self.global_bacteria.extend(initial_bacteria)

    def execute(self):
        """Main execute function, runs in a loop until time has elapsed."""
        pygame.init()  # pylint: disable=no-member
        window_size = [self.world.max_x_size * WIDTH, self.world.max_y_size * HEIGHT]
        screen = pygame.display.set_mode(window_size)
        screen.fill(BLACK)
        pygame.display.set_caption('Sandbox')
        clock = pygame.time.Clock()

        while self.end_time:
            self.execute_second()
            self.update_screen(clock, screen)
            self.end_time -= 1
            self.world.time += 1
            # display_world.plot_bacteria(self.world)

    def execute_second(self):
        """Run one second of the simulation."""
        for bacteria in self.global_bacteria:
            bacteria.execute_second(self.world)

    def update_screen(self, clock, screen):
        """Update the screen of the game."""
        for x_position in range(self.world.max_x_size):
            for y_position in range(self.world.max_y_size):
                color = self.get_land_color(x_position, y_position)
                pygame.draw.rect(screen,
                                 color,
                                 [WIDTH * x_position,
                                  HEIGHT * y_position,
                                  WIDTH,
                                  HEIGHT])
        clock.tick(60)
        pygame.display.flip()

    def get_land_color(self, x_position, y_position):
        """Get the color of the land for the simulation.

        :param int x_position: The x position of their piece of land
        :param int y_position: The y position of their piece of land
        """
        x_y_key = utils.get_x_y_key(x_position, y_position)
        color = (self.world.world_map[x_y_key].oxygen,
                 self.world.world_map[x_y_key].nitrogen,
                 self.world.world_map[x_y_key].phosphorus)
        return color
