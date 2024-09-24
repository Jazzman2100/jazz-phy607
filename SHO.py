# Codes from Nich's work
# %% Cell 1
import matplotlib.pyplot as plt
# init variables
k = 1
m = 1
t = 0
time = []
time_s = []
x = 1
x_pos = []
x_pos_s = []
v = 0
vel = []
vel_s = []
a = 0
acc = []
acc_s = []
dt = 0.01

# time evolution 'explicit' estimation
while t < 120:
    time.append(t)
    x_pos.append(x)
    vel.append(v)
    acc.append(a)
    F = -k*(x)
    a = F/m
    x = x + v*dt
    v = v + a*dt
    t = t + dt
# reset variable
t = 0
x = 1
v = 0
a = 0

# time-evolution 'symplectic' estimation
while t < 120:
    time_s.append(t)
    x_pos_s.append(x)
    vel_s.append(v)
    acc_s.append(a)


    F = -k*(x)
    a = F/m
    v = v + a*dt
    x = x + v*dt
    t = t + dt

# Plotting Dynamics
# %% Cell 2
plt.figure(1)
plt.plot(time, x_pos, time, x_pos_s)
plt.title("Position Vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.legend("Explicit", "Symplectic")
