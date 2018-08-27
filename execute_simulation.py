# Main file to execute the simulation of the world
import sandbox


if __name__ == "__main__":
    world = sandbox.World()
    simulate_world = sandbox.SimulateWorld(world, 100)
    simulate_world.execute()
