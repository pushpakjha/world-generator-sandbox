"""Methods to help plot the stuff in the world."""
from sandbox import utils

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
    nitrogen = 0
    phosphorus = 0
    potassium = 0
    for x_val in range(0, world.max_x_size):
        for y_val in range(0, world.max_y_size):
            x_y_key = utils.get_x_y_key(x_val, y_val)
            nitrogen += world.world_map[x_y_key].nitrogen
            phosphorus += world.world_map[x_y_key].phosphorus
            potassium += world.world_map[x_y_key].potassium
    print('nitrogen:{} phosphorus:{} potassium:{}'.format(nitrogen, phosphorus, potassium))
