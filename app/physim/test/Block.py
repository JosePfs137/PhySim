#Importing PhyObjects from parent directory.
#Not needed if you have pip installed PhySimn
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from PhyObjects import Simulation, Particles, MassPoint

SCALE = 10

v = [10*SCALE, 5*SCALE]
Block = Particles(*[])
for i in range(20):
    for j in range(5):
        p = MassPoint([SCALE*(2*i+1), 3*SCALE*(j+1)], v, 1, radius = 0.5*SCALE)
        Block.add(p)

SIM = Simulation(Block, name = 'Block')
SIM.run()