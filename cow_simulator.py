import numpy as np
import matplotlib.pyplot as plt

def compute_forces(position, velocity):
    gravity = 9.8 #m/s^2
    mass = 1000 #kg
    force_gravity = mass*gravity
    force_wind_resistance = velocity**2
    total_force = -force_wind_resistance + force_gravity
    return total_force

# no wind resistance for now
def updated_position_x(total_force, init_velocity_x, mass, init_position_x, time_step):
    acceleration = total_force/mass
    new_position_x = init_position_x + init_velocity_x*time_step
    return new_position_x

Y = updated_position_x(force_gravity, 0, 1000, 0, 10)

def updated_position_y(total force, init_velocity_y, mass, init_position_y, time_step):
    acceleration = total_force/mass
    new_position_y = init_position_y + init_velocity_y*time_step
    return new_position_y

def updated_velocity_x(init_velocity_x, time_step, total_force, mass):
    acceleration = total_force/mass
    new_velocity_x = init_velocity_x + acceleration*time_step
    return new_velocity_x
    

def updated_velocity_y(init_velocity_y, time_step, total_force, mass):
    acceleration = total_force/mass
    new_velocity_y = init_velocity_y + acceleration*time_step
    return new_velocity_y


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
