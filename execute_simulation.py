"""Main file to execute the simulation of the world"""
import sandbox


if __name__ == "__main__":
    world = sandbox.World(max_x_size=20, max_y_size=20)
    initial_bacteria = [sandbox.OxygenBacteria(x_position=5, y_position=5),
                        sandbox.NitrogenBacteria(x_position=10, y_position=10),
                        sandbox.PhosphorusBacteria(x_position=15, y_position=15)]
    simulate_world = sandbox.SimulateWorld(world=world, end_time=1000, initial_bacteria=initial_bacteria)
    simulate_world.execute()
