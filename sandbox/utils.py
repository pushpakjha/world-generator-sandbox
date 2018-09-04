"""Useful utils."""
import random


def get_x_y_key(x_val, y_val):
    """Return a string of x:y used for the world map keys.

    :param int x_val: The x value
    :param int y_val: The y value
    """
    return '{}:{}'.format(x_val, y_val)


def get_new_position(orig_x, orig_y, max_x, max_y, distance):
    """Get new positions for things to reproduce.

    :param int orig_x: The original x position
    :param int orig_y: The original y position
    :param int max_x: The max x position
    :param int max_y: The max y position
    :param int distance: The possible distance to spread
    :rtype: tuple
    """
    x_diff = 0
    while not x_diff:
        x_diff = random.randint(0, distance * 2) - distance
    y_diff = 0
    while not y_diff:
        y_diff = random.randint(0, distance * 2) - distance
    new_x = orig_x + x_diff
    new_y = orig_y + y_diff
    if new_x < 0:
        new_x = max_x - 1
    if new_x >= max_x:
        new_x = 0
    if new_y < 0:
        new_y = max_y - 1
    if new_y >= max_y:
        new_y = 0
    return new_x, new_y
