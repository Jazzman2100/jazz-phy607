import numpy as np
import matplotlib.pyplot as plt

def compute_forces(position, velocity):
    gravity = 9.8 #m/s^2
    mass = 1000 #kg
    force_gravity = mass*gravity
    force_wind_resistance = velocity**2
    total_force = -force_wind_resistance + force_gravity
    return total_force

def updated_position_velocity(total_force, mass, position, velocity, time_step):
    acceleration = total_force/mass
    new_velocity =
    new_position =
    return new_position, new_velocity


def energy(gravity, position, velocity, mass):
    height = position[1]
    potential_energy = mass*g*height
    kinetic_energy = 0.5*mass*velocity**2
    total_energy = potential_energy + kinetic_energy
    return potential_energy, kinetic energy, total_energy


def main():
    position = np.array([0.0,1000.0])
    velocity = np.array([10.0,0.0])
    mass = 1000
    time_step =0.1
    time = 0
    max_time = 1000

    #make lists for plotting

    position = []
    velocity = []
    energy = []

    while position[1]>0 and time<max_time:
        force = compute_forces(position, velocity, mass, force_wind_resistance)
        position,velocity = updat

        time += time_step

    print(f"Final Position: {position}")
    print(f"Final Velocity: {velocity}")
    print(f"Final Time: {time}")
if __name__ == "__main__":
    main()


def plot():
    position = np.array(position)
    velocity = np.array(velocity)

    plt.plot()
