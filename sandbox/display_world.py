"""Methods to help plot the stuff in the world."""


def plot_bacteria(world):
    """Plot the bacteria in the world.

    :param sandbox.simulate_world.World world: The world object
    """
    print('*'*100)
    print(world.time)
    bacteria_count = {}

    for bacteria in world.global_bacteria:
        if str(bacteria) in bacteria_count:
            bacteria_count[str(bacteria)] += 1
        else:
            bacteria_count[str(bacteria)] = 1

    print(bacteria_count)
