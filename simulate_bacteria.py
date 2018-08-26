# Definitions of the simulated bacteria in the world.
import abc


class Bacteria(object):
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    """
    def __init__(self, max_lifetime):
        self.current_lifetime = 0
        self.max_lifetime = max_lifetime

    @abc.abstractmethod
    def execute_second(self):
        self.current_lifetime += 1
