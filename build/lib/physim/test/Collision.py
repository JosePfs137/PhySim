from physim import Simulation, MassPoint, Wall, Particles

SCALE = 10
WIDTH = 600
HEIGHT = 600

W1 = Wall([WIDTH/2, HEIGHT/2], WIDTH, SCALE)
p1 = MassPoint([WIDTH/3, HEIGHT/4], [10*SCALE, 0], 2, radius = 2*SCALE)
p2 = MassPoint([2*WIDTH/3, HEIGHT/4], [-10*SCALE, 0], 1, radius = 1*SCALE)

p3 = MassPoint([WIDTH/3, 3*HEIGHT/4], [10*SCALE, 0], 2, radius = 2*SCALE)
W2 = Wall([2*WIDTH/3, 3*HEIGHT/4], 2*SCALE, HEIGHT/4)

P = Particles(p1, p2, p3)
SIM = Simulation(P, walls = [W1, W2], size = (WIDTH, HEIGHT), name = 'Collision')
SIM.run()