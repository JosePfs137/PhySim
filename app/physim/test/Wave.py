#Importing PhyObjects from parent directory.
#Not needed if you have pip installed PhySimn
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from PhyObjects import Simulation, Particles, MassPoint

SCALE = 30
WIDTH = 400
HEIGHT = 400

w = int(WIDTH/SCALE)
h = int(HEIGHT/SCALE)

v = [10*SCALE, 0]
Medium = Particles(*[])
for i in range(1, w):
    for j in range(h):
        p = MassPoint([SCALE*(2*i+1), 3*SCALE*(j+1)], [0,0], 1, radius = 0.5*SCALE)
        Medium.add(p)

for j in range(h):
    p = MassPoint([SCALE, 3*SCALE*(j+1)], v, 1, radius = 0.5*SCALE)
    Medium.add(p)

SIM = Simulation(Medium, size = (WIDTH, HEIGHT), name = 'Wave')
SIM.run(ShowFPS = True)