"""Methods to help plot the stuff in the world."""
import matplotlib


def plot_bacteria(world):
    """Plot the bacteria in the world.

    :param sandbox.simulate_world.World world: The world object
    """
    print('*'*50)
    print(world.time)
    for bacteria in world.global_bacteria:
        print(bacteria)
