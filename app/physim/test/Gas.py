#Importing PhyObjects from parent directory.
#Not needed if you have pip installed PhySimn
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from PhyObjects import Gas,Simulation

SCALE = 10
WIDTH = 700
HEIGHT = 600
P = []
E = 1*10**7
N = 150
G = Gas([WIDTH/2, HEIGHT/2], N, 1, E, WIDTH, HEIGHT)

SIM = Simulation(G,size = (WIDTH, HEIGHT), name = 'Gas')
SIM.run(ShowFPS = True)