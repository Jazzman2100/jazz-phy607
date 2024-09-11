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
# prompt user to input the initial velocity of x
init_velocity_x = 20 #m/s
time = [0, 1, 2, 3]
new_position_x = np.array([])
def updated_position_x(total_force, init_velocity_x, mass, init_position_x, time_step):
    acceleration = total_force/mass
    new_position_x = init_position_x + init_velocity_x*time_step
    updated_position_x= np.array([force_gravity, 0, 1000, 0, 10])
    return updated_position_x

def new_position_x(total_force, init_velocity_x, mass, init_position_x, time_step):
    new_position_x= init_position_x + init_velocity_x*time_step
    return new_position_x
    position_x = updated_position_x(0, init_velocity_x, 1000, 0, time)
    print(position_x)

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
    potential_energy = mass*gravity*height
    kinetic_energy = 0.5*mass*velocity**2
    total_energy = potential_energy + kinetic_energy
    return potential_energy, kinetic energy, total_energy


def main():
    init_velocity_x = 20 #m/s
    init_position_x = 0 #m
    time = [0, 1, 2, 3]
    position = np.array([0.0,1000.0])
    velocity = np.array([10.0,0.0])
    mass = 1000
    #if we need this: wind_resistance_constant = 1
    time_step =0.1
    time = 0
    max_time = 1000

    #make lists for plotting

    position_x = []
    position_y =[]
    velocity_x = []
    velocity_y= []
    energy = []

    while position[1]>0 and time<max_time:
        force_x = compute_forces_x(position_x, velocity_x, mass, force_wind_resistance)
        force_y = compute_forces_y(position_y, velocity_y, mass, force_wind_resistance)
        positions.append(position.copy())
        velocity.append(velocity.copy())
        energy.append((potential_energy, kinetic_energy, total_energy))

        time += time_step

    print(f"Final X- Position: {position_x}")
    print(f"Final X-Velocity: {velocity_x}")
    print(f"Final Y-Position: {position_y}")
    print(f"Final Y-Velocity: {velocity_y}")
    print(f"Final Time: {time}")
if __name__ == "__main__":
    main()


def plot():
    position = np.array(position)
    velocity = np.array(velocity)

    plt.plot()

# %% Cell 1
import numpy as np
import matplotlib.pyplot as plt
#%% Cell 2
mo = 1000 #kg
vo = 200 #m/s
g = 9.8 #m/s^2
y0 = 1000 #m
t = np.arange(0,int(1000/10))

def v(t):
    return vo - g*t

def y(t):
    return y0 + vo*t - 0.5*g*(t**2)

plt.plot(t,y(t))
plt.grid()
plt.show()

# Cell 3
# Energy plot
KE = 0.5*mo*v(t)**2
plt.plot(t,KE, color='green')
plt.xlabel("Time(s)")
plt.ylabel("Kenitic Energy(J)")
plt.grid()
plt.show()
