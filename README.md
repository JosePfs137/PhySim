# PhySim
My project for the Computational Physics class attempts to add some objects useful for creating your 2D physics simulations with Python.

***
## Objects
***
### MassPoint

In physics one of the core concepts is the mass point; with this concept, you can study the kinematics and dynamics of every object (at least in the classical world) and construct models to describe solids, gases, and liquids. The MassPoint class aims to abstract this concept for later usage.

```
physim.MassPoint(r_0, v_0, m, a_0 = [0,0], q = 0, radius = 1, color = (0, 180, 200))
```

**r_0 (list)**: A list with the x and y coordinates of the point.

**v_0 (list)**: A list with the x and y components of the points velocity.

**m (float)**: A real positive number that represents the mass of the point

***Optional***:

**a_0(list)**: The initial acceleration of the particle. (0 by default)

**q (float)**: The charge of the particle. (0 by default)

**radius (float)**: Because we can't visualize points, a radius to graph a circle is needed.

**color (tuple (int, int, int))**: The color in RGB format.

***
### Wall

Wall class aims to simulate a rectangular object with infinite mass (in the sense that it won't move at all).

```
physim.Wall(r_0, width, height)
```

**r_0 (list)**: The x and y coordinates of the center of the wall

**width (float)**: A positive real number describing the horizontal extension of the wall.

**height (float)**: A positive real number describing the vertical extension of the wall.

***
### Particles
Attempts to simulate a list of particles, with some methods like Collision and MeanRadius.

```
physim.Particles(*P)
```

***P**(*args of physim.MassPoint): The particles to be contained in our list.

***
### Gas
Inherited from Particles, aims to stimulate a Gas with a given energy and with just a few particles (less than 200).

```
physim.Gas(r_0, N, m, energy, width, height, radius = 10, SCALE = 10) 
```
**r_0 (list)**: A [x, y] list with the x and y coordinates of the center of mass of the given gas.

**N(int)**: The number of particles in the gas.

**m(int)**: The mass of each particle

**energy(float)**: The energy of the whole gas (in the units you are using)

**width** and **height (float)**: The space region in which you'll find the particles

***Optional***

**radius(float)**: Because we can't visualize points, a radius to graph a circle is needed.

**SCALE(float)**: The amount of pixels per unit of length

***
### Simulation

The simulation itself, with the pygame window and the main function.
```
physim.Simulation(P, walls = [],size = (600, 600), FPS = 60, time_res = 1, backgound = (240,240,240), name = 'Simulation', TOP = True, BOTTOM = True, LEFT = True, RIGHT = True)
```
**P(physim.Particles)**: All the particles in our simulation. (empty by default)

**walls (list of physim.Wall objects)**: All the additional walls in our simulation (empty by default).

**size (tuple of int)**: A (WIDTH, HEIGHT) tuple that defines the size of our windows.

**FPS (int)**: The maximum frame rate at which the simulation will run.

**time_res(float)**:A positive real number that indicates the time step length relative to a frame. (1 by default; it means that we will take 1/FPS time steps)

**background (tuple)**: A (RED, GREEN, BLUE) tuple with the background color with the usual RGB values.

**name (string)**: The caption of the window.

**TOP, BOTTOM, LEFT, RIGHT (boolean)**: If true, the corresponding window border will act as a wall.