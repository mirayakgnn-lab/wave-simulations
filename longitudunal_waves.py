import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_particles = 50
amplitude = .5
wavelength = 10
frequency = 1.0
wave_speed = 3.0

# Equilibrium positions
x_eq = np.linspace(0, 40, num_particles)

fig, ax = plt.subplots(figsize=(10, 3))
ax.set_title("Longitudinal Wave Simulation")
ax.set_xlabel("Position")
ax.get_yaxis().set_visible(1)

particles_list = []

for i in range(20):
    line, = ax.plot(x_eq, np.full(num_particles, i), 'bo')
    particles_list.append(line)

def update(frame):
    # Time based on frame
    t = frame * 0.1
    
    # Longitudinal displacement formula: A * sin(k*x - omega*t)
    # k = 2*pi / wavelength
    # omega = 2*pi * frequency
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    
    # Calculate new positions
    x_new = x_eq + amplitude * np.sin(k * x_eq - omega * t)
    
    # Update particle positions
    for i in range(20):
        particles_list[i].set_xdata(x_new)
        
    return particles_list

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()