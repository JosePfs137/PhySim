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
    def __init__(self, r_0, v_0, m, a_0 = [0,0], q = 0, radius = 1):
        '''
        Defines a point mass with its initial position and 
        velocity, and its mass.
            Inputs:
                    r_0 (list): A list with the x and y coordinates 
                                of the point.
                    v_0 (list): A list with the x and y components 
                                of the points velocity.
                    m (float): A real positive number that represents the mass
                               of the point
                Optional:
                    a_0(list): The initial acceleration of the particle.
                               (0 by default)
                    q (float): The charge of the particle. 
                               (0 by default)
                    radius (float): Because we can't visualize points, 
                                    a radius to graph a circle is needed.
        '''
        self.r = np.array(r_0)
        self.v = np.array(v_0)
        self.m = m
        self.a = np.array(a_0)
        self.q = q
        self.radius = radius

    def draw(self, win, color):
        '''
        With the help of pygame library draw our particle on 
        the pygame window.
            Inputs:
                    win (pygame.Surface): The surface on which the particle
                                          will be drawn.
                    color (tuple (int, int, int)): The color in RGB format.
        '''
        pygame.draw.circle(win, color, (self.r[0], self.r[1]), self.radius)
    
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

        #First, we check if the distance between the vertical coordinates of the wall and the particle
        #is less than the sum of the radius of the particle and the wall height so they don't overlap.
        if abs(self.r[1] - wall.r[1]) < (self.radius + wall.height):
            self.v[1] = -self.v[1]

        #Now we do the same for the horizontal coordinates.
        if abs(self.r[0] - wall.r[0]) < (self.radius + wall.width):
            self.v[0] = -self.v[0]

    def particle_collision(self, p2):
        '''
        Handles the collisions particle-particle.
            Inputs:
                    p2 (MassPoint object): The physim.MassPoint that could collide with the particle.
        '''
        #We named d the distance between both particles.
        d = self.r - p2.r
        #If the particles overlap:
        if np.sqrt(np.dot(d, d)) < self.radius + p2.radius:
            #We calculate the final velocity assuming that the collision is elastic, therefore, 
            #the energy and momentum right before the collision are the same as the energy and 
            # momentum after the hit.
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
                    width (float): A positive real number describing the horizontal 
                                   extension of the wall.
                    height (float): A positive real number describing the vertical
                                    extension of the wall.
        '''
        self.width = width
        self.height = height
        self.r = np.array(r_0)
    
    def draw(self, win, color):
        '''
        With the help of pygame library draw our wall on 
        the pygame window.
            Inputs:
                    win (pygame.Surface): The surface on which the particle
                                          will be drawn.
                    color (tuple (int, int, int)): The color in RGB format.
        '''
        rectangle = pygame.Rect(self.r[0] - self.width/2, self.r[1] - self.height/2, self.width, self.height)
        pygame.draw.rect(win, color, rectangle)

    