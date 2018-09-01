"""Useful utils."""


def get_x_y_key(x_val, y_val):
    """Return a string of x:y used for the world map keys.

    :param int x_val: The x value
    :param int y_val: The y value
    """
    return '{}:{}'.format(x_val, y_val)
