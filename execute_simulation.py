"""Main file to execute the simulation of the world"""
import sandbox


if __name__ == "__main__":
    world = sandbox.World(20, 20)
    initial_bacteria = [sandbox.OxygenBacteria(2, 2), sandbox.NitrogenBacteria(4, 4), sandbox.PhosphorusBacteria(6, 6)]
    simulate_world = sandbox.SimulateWorld(world, 75, initial_bacteria=initial_bacteria)
    simulate_world.execute()
