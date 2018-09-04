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
    carbon = 0
    plant_matter = 0
    tree_matter = 0
    grass = 0
    trees = 0
    for x_val in range(0, world.max_x_size):
        for y_val in range(0, world.max_y_size):
            x_y_key = utils.get_x_y_key(x_val, y_val)
            nitrogen += world.world_map[x_y_key].nitrogen
            phosphorus += world.world_map[x_y_key].phosphorus
            potassium += world.world_map[x_y_key].potassium
            carbon += world.world_map[x_y_key].carbon
            plant_matter += world.world_map[x_y_key].plant_matter
            tree_matter += world.world_map[x_y_key].tree_matter
            grass += len(world.world_map[x_y_key].beings['grass'])
            trees += len(world.world_map[x_y_key].beings['tree'])
    print('nitrogen:{} phosphorus:{} potassium:{} carbon:{} plant_matter:{} tree_matter:{}'
          .format(nitrogen, phosphorus, potassium, carbon, plant_matter, tree_matter))
    print('grass: {} trees:{}'.format(grass, trees))
