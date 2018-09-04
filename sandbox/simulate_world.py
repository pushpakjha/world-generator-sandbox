"""Main simulation loop file"""
import collections
import random

import pygame

from sandbox import display_world
from sandbox import simulate_plants
from sandbox import utils

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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
        self.global_plants = []


class Land:
    """Object to represent a piece of land.

    :param int x_position: The x position of their piece of land
    :param int y_position: The y position of their piece of land
    :param float carbon: The amount of carbon
    :param float potassium: The amount of potassium
    :param float nitrogen: The amount of nitrogen
    :param float phosphorus: The amount of phosphorus
    :param int plant_matter: The amount of plant matter
    :param int tree_matter: The amount of tree matter
    :param list[Any] beings: A list of any things living in this piece of land
    """
    def __init__(self, x_position, y_position, carbon=0, potassium=0, nitrogen=0,
                 phosphorus=0, plant_matter=0, tree_matter=0, beings=None):
        self.x_position = x_position
        self.y_position = y_position
        self.carbon = float(carbon)
        self.potassium = float(potassium)
        self.nitrogen = float(nitrogen)
        self.phosphorus = float(phosphorus)
        self.plant_matter = plant_matter
        self.tree_matter = tree_matter
        self.beings = collections.defaultdict(list)
        if beings:
            self.beings.update(beings)


class SimulateWorld:
    """Execute the simulation on a world object.

    :param World world: The world object
    :param int end_time: Number of ticks to simulate world
    :param list[sandbox.simulate_bacteria.Bacteria]|None initial_bacteria: Initial bacteria to seed
        the world with
    """
    def __init__(self, world, end_time, initial_bacteria=None):
        self.world = world
        self.end_time = end_time
        self.global_bacteria = world.global_bacteria
        self.global_plants = world.global_plants
        if initial_bacteria:
            self.global_bacteria.extend(initial_bacteria)

    def execute(self):
        """Main execute function, runs in a loop until time has elapsed."""
        pygame.init()  # pylint: disable=no-member
        window_size = [self.world.max_x_size * WIDTH, self.world.max_y_size * HEIGHT]
        screen = pygame.display.set_mode(window_size)
        screen.fill(WHITE)
        pygame.display.set_caption('Sandbox')
        clock = pygame.time.Clock()

        while self.world.time < self.end_time:
            self.execute_tick()
            self.update_screen(clock, screen)
            self.world.time += 1
            display_world.plot_bacteria(self.world)

    def execute_tick(self):
        """Run one tick of the simulation."""

        for plant in self.global_plants:
            plant.execute_tick(self.world)
        for bacteria in self.global_bacteria:
            bacteria.execute_tick(self.world)
        # Seed the world with plants after some time
        self.spawn_plants()

    def spawn_plants(self):
        """Spawn plants."""
        if 100 < self.world.time < 125:
            for _ in range(0, 5):
                rand_x_pos = random.randint(0, self.world.max_x_size - 1)
                rand_y_pos = random.randint(0, self.world.max_y_size - 1)
                self.spawn_grass_plant(rand_x_pos, rand_y_pos)
        if 200 < self.world.time < 215:
            for _ in range(0, 5):
                rand_x_pos = random.randint(0, self.world.max_x_size - 1)
                rand_y_pos = random.randint(0, self.world.max_y_size - 1)
                self.spawn_tree(rand_x_pos, rand_y_pos)

    def spawn_grass_plant(self, x_position, y_position):
        """Spawn a single grass plant.

        :param int x_position: The x position of this grass plant
        :param int y_position: The y position of this grass plant
        """
        plant = simulate_plants.GrassPlant(x_position, y_position)
        x_y_key = utils.get_x_y_key(x_position, y_position)
        self.world.global_plants.append(plant)
        self.world.world_map[x_y_key].beings['grass'].append(plant)

    def spawn_tree(self, x_position, y_position):
        """Spawn a single tree.

        :param int x_position: The x position of this tree
        :param int y_position: The y position of this tree
        """
        tree = simulate_plants.TreePlant(x_position, y_position)
        x_y_key = utils.get_x_y_key(x_position, y_position)
        self.world.global_plants.append(tree)
        self.world.world_map[x_y_key].beings['tree'].append(tree)

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
        :rtype: tuple
        """
        scale_factor = 1
        x_y_key = utils.get_x_y_key(x_position, y_position)
        red_color = ((self.world.world_map[x_y_key].phosphorus +
                      self.world.world_map[x_y_key].potassium +
                      self.world.world_map[x_y_key].nitrogen) * scale_factor)
        red_color -= len(self.world.world_map[x_y_key].beings['grass']) * 400
        green_color = self.world.world_map[x_y_key].nitrogen * scale_factor
        green_color += len(self.world.world_map[x_y_key].beings['grass']) * 45
        blue_color = self.world.world_map[x_y_key].potassium * scale_factor
        blue_color -= len(self.world.world_map[x_y_key].beings['grass']) * 60
        if len(self.world.world_map[x_y_key].beings['tree']) >= 2:
            red_color = 139
            green_color = 69
            blue_color = 19

        return self._get_safe_rgb_color(red_color, green_color, blue_color)

    @staticmethod
    def _get_safe_rgb_color(red_color, green_color, blue_color):
        """Get the color of the land for the simulation.

        :param float red_color: The red color
        :param float green_color: The green color
        :param float blue_color: The blue color
        :rtype: tuple
        """
        red_color = int(red_color)
        green_color = int(green_color)
        blue_color = int(blue_color)
        if red_color > 255:
            red_color = 255
        if green_color > 255:
            green_color = 255
        if blue_color > 255:
            blue_color = 255
        if red_color < 0:
            red_color = 0
        if green_color < 0:
            green_color = 0
        if blue_color < 0:
            blue_color = 0
        color = (red_color, green_color, blue_color)
        return color
