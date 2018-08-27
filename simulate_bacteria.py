# Definitions of the simulated bacteria in the world.
import abc


class Bacteria(object):
    """Base bacteria object.

    :param int max_lifetime: How long the bacteria should live
    :param list[Bacteria] global_bacteria: List of all the bacteria
    :param int child_counter: The id of the parent to this child, if this is a child else None
    """
    def __init__(self, max_lifetime, global_bacteria, child_counter=None, reproduction_rate=5):
        self.current_lifetime = 0
        self.max_lifetime = max_lifetime
        self.global_bacteria = global_bacteria
        self.child_counter = child_counter
        self.reproduction_rate = reproduction_rate

    def execute_second(self):
        """Add to the lifetime and perform basic life checks."""
        self.current_lifetime += 1
        if self.current_lifetime >= self.max_lifetime:
            self.die()
        if self.current_lifetime % self.reproduction_rate == 0:
            child = self.reproduce()
            self.global_bacteria.append(child)

    def die(self):
        """Kill the bacteria."""
        self.global_bacteria.remove(self)

    def reproduce(self):
        """Make a new child bacteria."""
        self.child_counter += 1
        return self(self.max_lifetime, self.child_counter)
