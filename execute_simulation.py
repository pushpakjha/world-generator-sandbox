"""Main file to execute the simulation of the world"""
import sandbox


if __name__ == "__main__":
    world = sandbox.World(max_x_size=20, max_y_size=20)
    initial_bacteria = [sandbox.PotassiumBacteria(x_position=4, y_position=4),
                        sandbox.PhosphorusBacteria(x_position=9, y_position=9),
                        sandbox.NitrogenBacteria(x_position=14, y_position=15),
                        sandbox.NitrogenBacteria(x_position=2, y_position=2)
                        ]
    simulate_world = sandbox.SimulateWorld(world=world, end_time=750,
                                           initial_bacteria=initial_bacteria)
    simulate_world.execute()
