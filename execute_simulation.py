"""Main file to execute the simulation of the world"""
import sandbox
import matplotlib


if __name__ == "__main__":
    world = sandbox.World()
    initial_bacteria = [sandbox.OxygenBacteria(), sandbox.NitrogenBacteria(), sandbox.PhosphorusBacteria()]
    simulate_world = sandbox.SimulateWorld(world, 100, initial_bacteria=initial_bacteria)
    simulate_world.execute()
