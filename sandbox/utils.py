"""Useful utils."""


def get_x_y_key(x_val, y_val):
    """Return a string of x:y used for the world map keys.

    :param int x_val: The x value
    :param int y_val: The y value
    """
    return '{}:{}'.format(x_val, y_val)


def reproduce(class_type, max_lifetime, x_position, y_position):
    """Make a new child bacteria.

    :param Any class_type: The class of the child
    :param int max_lifetime: How long the bacteria should live
    :param int x_position: The x position of this bacteria
    :param int y_position: The y position of this bacteria
    """
    child = class_type(max_lifetime, x_position, y_position)
    return child
