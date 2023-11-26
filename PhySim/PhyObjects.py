import numpy as np
import pygame
import os 

class MassPoint:
    '''
    In physics one of the core concepts is the mass point; with 
    this concept, you can study the kinematics and dynamics of 
    every object (at least in the classical world) and construct 
    models to describe solids, gases, and liquids. The MassPoint 
    class aims to abstract this concept for later usage.
    '''
    def __init__(self, r_0, v_0, m, a_0 = [0,0], q = 0, radius = 1, color = (0, 180, 200)):
        '''
        Defines a point mass with its initial position and 
        velocity, and its mass.
            Inputs:
                    r_0 (list): A list with the x and y coordinates of the point.
                    v_0 (list): A list with the x and y components of the points velocity.
                    m (float): A real positive number that represents the mass of the point
                Optional:
                    a_0(list): The initial acceleration of the particle. (0 by default)
                    q (float): The charge of the particle. (0 by default)
                    radius (float): Because we can't visualize points, a radius to graph a circle is needed.
                    color (tuple (int, int, int)): The color in RGB format.
        '''
        self.r = np.array(r_0)
        self.v = np.array(v_0)
        self.m = m
        self.a = np.array(a_0)
        self.q = q
        self.radius = radius
        self.color = color

    def draw(self, win):
        '''
        With the help of pygame library draw our particle on 
        the pygame window.
            Inputs:
                    win (pygame.Surface): The surface on which the particle will be drawn.
        '''
        pygame.draw.circle(win, self.color, (self.r[0], self.r[1]), self.radius)
    
    def update(self, dt):
        '''
        Updates the current state of the particle by using the finite step 
        approximation.
            Inputs:
                    dt (float): The length of the time step.
        '''
        #self.fieldUp()
        self.r = self.r + dt * self.v
        self.v = self.v + dt * self.a
    
    def wall_collision(self, wall):
        '''
        Handles the collision between particle wall.
            Inputs:
                    wall (Wall object): The physim.Wall that could collide with the particle.
        '''
        #Since there are no diagonal walls, we only need to check vertical and horizontal collisions.

        pLpoint = self.r[0] - self.radius
        pRpoint = self.r[0] + self.radius
        pUpoint = self.r[1] - self.radius
        pDpoint = self.r[1] + self.radius

        wLpoint = wall.r[0] - wall.width/2
        wRpoint = wall.r[0] + wall.width/2
        wUpoint = wall.r[1] - wall.height/2
        wDpoint = wall.r[1] + wall.height/2

        Roverlap = pRpoint - wLpoint
        Loverlap = wRpoint - pLpoint
        Doverlap = pDpoint - wUpoint
        Uoverlap = wDpoint - pUpoint

        Xcollision = (0 < Roverlap) and (0 < Loverlap)
        Ycollision = (0 < Doverlap) and (0 < Uoverlap)

        if Ycollision and Xcollision:
            if min(Roverlap, Loverlap) >= min(Doverlap, Uoverlap):
                d = self.r[1] - wall.r[1]
                d = d/abs(d)
                self.r[1] = wall.r[1] + d*wall.height/2 + d*self.radius
                self.v[1] = -self.v[1]
            
            if min(Roverlap, Loverlap) <= min(Doverlap, Uoverlap):
                d = self.r[0] - wall.r[0]
                d = d/abs(d)
                self.r[0] = wall.r[0] + d*wall.width/2 + d*self.radius
                self.v[0] = -self.v[0]

            
    def particle_collision(self, p2):
        '''
        Handles the collisions particle-particle.
            Inputs:
                    p2 (MassPoint object): The physim.MassPoint that could collide with the particle.
        '''
        #We named d the distance between both particles.
        d = p2.r - self.r
        d_len = np.sqrt(np.dot(d, d))
        #If the particles overlap:
        if np.sqrt(np.dot(d, d)) < self.radius + p2.radius:
            #We calculate the final velocity assuming that the collision is elastic, therefore, 
            #the energy and momentum right before the collision are the same as the energy and 
            # momentum after the hit.

            d_unit = d/d_len
            midpoint = d*(1/2) + self.r
            self.r = midpoint - d_unit*self.radius
            p2.r = midpoint + d_unit*p2.radius
            
            c1 = (self.m - p2.m)/(self.m + p2.m)
            c2 = 2*self.m / (self.m + p2.m)
            v_r = self.v - p2.v
            self.v = c1*v_r + p2.v
            p2.v = c2*v_r + p2.v

    
    def __str__(self):
        return 'A '+ str(self.m) +' units of mass point in ' + '(' + str(self.r[0]) + ',' + str(self.r[1]) + ')'
    
class Wall:
    '''
    Wall class aims to simulate a rectangular object with infinite mass (in the sense that it won't 
    move at all).
    '''

    def __init__(self, r_0, width, height):
        '''
        Defines our immovable wall.
            Inputs:
                    r_0 (list): The x and y coordinates of the center of the wall
                    width (float): A positive real number describing the horizontal extension of the wall.
                    height (float): A positive real number describing the vertical extension of the wall.
        '''
        self.width = width
        self.height = height
        self.r = np.array(r_0)
    
    def draw(self, win, color):
        '''
        With the help of pygame library draw our wall on 
        the pygame window.
            Inputs:
                    win (pygame.Surface): The surface on which the particle will be drawn.
                    color (tuple (int, int, int)): The color in RGB format.
        '''
        rectangle = pygame.Rect(self.r[0] - self.width/2, self.r[1] - self.height/2, self.width, self.height)
        pygame.draw.rect(win, color, rectangle)

class Simulation: 
    '''
    The simulation itself, with the pygame window and the main function.
    '''

    def __init__(self, particles = [], walls = [],size = (600, 600), FPS = 60, time_res = 1, backgound = (240,240,240), name = 'Simulation', TOP = True, BOTTOM = True, LEFT = True, RIGHT = True):
        '''
        We first save all variables needed for the simulation
            Inputs:
                    particles (list of physim.MassPoint objects): All the particles in our simulation (empty by default).
                    walls (list of physim.Wall objects): All the additional walls in our simulation (empty by default).
                    size (tuple of int): A (WIDTH, HEIGHT) tuple that defines the size of our windows.
                    FPS (int): The maximum frame rate at which the simulation will run.
                    time_res(float):A positive real number that indicates the time step length relative to a frame. (1 by default; it means that we will take 1/FPS time steps)
                    background (tuple): A (RED, GREEN, BLUE) tuple with the background color with the usual RGB values.
                    name (string): The caption of the window.
                    TOP, BOTTOM, LEFT, RIGHT (boolean): If true, the corresponding window border will act as a wall.
        '''
        self.particles = particles
        self.walls = walls
        self.size = size
        self.FPS = FPS
        self.time_res = time_res
        self.background = backgound
        self.name = name

        self.WIN = pygame.display.set_mode(size)
        self.borders = []
        if TOP:
            self.borders.append(Wall((size[0]/2, 0), size[0], 10))
        if BOTTOM:
            self.borders.append(Wall((size[0]/2, size[1]), size[0], 10))
        if LEFT:
            self.borders.append(Wall((0, size[1]/2), 10, size[1]))
        if RIGHT:
            self.borders.append(Wall((size[0], size[1]/2), 10, size[1]))
    
    def particles_collisions (self):
        '''
        Handles all the collisions between particles.
        '''
        #We make a list with len(self.particles) elements so we can iterate in each particle easily.
        N = len(self.particles)
        N_list = range(N)
        #Now we're interested in checking only once the collision between particle i and 
        #particle j, we created a set for that purpose.
        checked = set()

        #We don't want to check the collision of a particle with itself or check the collision of a 
        #particle twice.
        for i in N_list:
            for j in N_list:
                if (i == j) | (j in checked):
                    continue
                self.particles[i].particle_collision(self.particles[j])
            checked.add(i)
    
    def wall_collisons (self):
        '''
        Handles all the collisions between particles and walls.
        '''
        for p in self.particles:
            for wall in self.walls:
                p.wall_collision(wall)
        
        for p in self.particles:
            for wall in self.borders:
                p.wall_collision(wall)


    def draw(self):
        '''
        Draws each frame of the simulation.
        '''
        self.WIN.fill(self.background)

        for wall in self.walls:
            wall.draw(self.WIN, (35, 54, 77))

        for wall in self.borders:
            wall.draw(self.WIN, (13, 20, 28))
        
        for p in self.particles:
            p.draw(self.WIN)
        
        pygame.display.update()

    def run(self):
        '''
        The main function in which we run the loop with the simulation.
        Here we're going to integrate all the functions we defined 
        before and update the whole system in real time, step by step.
        '''
        #clock will help us to control the maximum speed of our simulation.
        clock = pygame.time.Clock()
        #dt are the little time steps that we will take to update our simulation.
        dt = self.time_res / self.FPS

        #The Loop with the simulation.
        while True:
            #Here we define the maximum frame rate of our simulation.
            clock.tick(self.FPS)

            #The next loop helps us to end the program whenever the "X" 
            #button on the up-right corner of the window is pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            
            #Now we update the particles one by one.
            for p in self.particles:
                p.update(dt)

            self.particles_collisions()
            self.wall_collisons()
            self.draw()


