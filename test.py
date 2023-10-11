import pandas as pd
import numpy as np
from vpython import *


data = {
    "t": [],
    "x": [],
    "y": [],
    "z": [],
    "u(p)": [],
    "0.0": [],
    "0.00": [],
    "fN-used": []
}

f = open("/sample_data/CPbl.a", "r")
headerLen = 10
for l, line in enumerate(f):  # Add the dataset into the "data" directory      
    if l >= headerLen:         
        part = line.split()
        data["t"].append(float(part[0]))
        data["x"].append(float(part[1]))
        data["y"].append(float(part[2]))
        data["z"].append(float(part[3]))
        data["u(p)"].append(float(part[4]))
        data["0.0"].append(float(part[5]))
        data["0.00"].append(float(part[6]))
        data["fN-used"].append(float(part[7]))

for d in data:
    data[d] = np.array(data[d])

df = pd.DataFrame(data)
#print(df)

scene = canvas(title="Particle Motion", width=800, height=600)

trail = curve(color=color.blue, radius=0.1)

time = df["t"]
x_data = df["x"]
y_data = df["y"]
z_data = df["z"]

particle = sphere(pos=vector(x_data[0], y_data[0], z_data[0]), radius=0.2, color=color.red)

dt = 0.01  # Adjust the time step as needed

for i in range(1, len(time)):
    rate(1 / dt)  # Adjust the animation speed
    
    # Update the particle's position
    particle.pos = vector(x_data[i], y_data[i], z_data[i])
    
    # Append the new position to the trail
    trail.append(pos=particle.pos)



