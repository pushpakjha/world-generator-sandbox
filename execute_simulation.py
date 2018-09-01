"""Main file to execute the simulation of the world"""
import sandbox


if __name__ == "__main__":
    world = sandbox.World(max_x_size=20, max_y_size=20)
    initial_bacteria = [sandbox.OxygenBacteria(x_position=8, y_position=8),
                        sandbox.NitrogenBacteria(x_position=10, y_position=10),
                        sandbox.PhosphorusBacteria(x_position=12, y_position=12)]
    simulate_world = sandbox.SimulateWorld(world=world, end_time=250, initial_bacteria=initial_bacteria)
    simulate_world.execute()
