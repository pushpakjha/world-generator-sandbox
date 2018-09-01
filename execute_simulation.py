"""Main file to execute the simulation of the world"""
import sandbox


if __name__ == "__main__":
    world = sandbox.World(max_x_size=20, max_y_size=20)
    initial_bacteria = [sandbox.PotassiumBacteria(x_position=1, y_position=4),
                        sandbox.PotassiumBacteria(x_position=3, y_position=18),
                        sandbox.PhosphorusBacteria(x_position=5, y_position=6),
                        sandbox.PhosphorusBacteria(x_position=7, y_position=7),
                        sandbox.NitrogenBacteria(x_position=14, y_position=19),
                        sandbox.NitrogenBacteria(x_position=18, y_position=2)
                        ]
    simulate_world = sandbox.SimulateWorld(world=world, end_time=500, initial_bacteria=initial_bacteria)
    simulate_world.execute()
