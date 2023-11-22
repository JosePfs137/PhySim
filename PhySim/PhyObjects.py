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

    


    
    def __str__(self):
        return 'A '+ str(self.m) +' units of mass point in ' + '(' + str(self.r[0]) + ',' + str(self.r[1]) + ')'
    
help(MassPoint)
    