import pygame
from pygame.locals import*
import time
import math
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

x = 0.01
y = 0
z = 0

angle = 0.01
display = (600,600)

counter = 0
def lorenz_attractor(x,y,z,counter):

    #parameters of lorenz attractor
    # let a be sigma
    # let b be rho
    # let c be beta
    dt = 0.01
    a = 10.0
    b = 28
    c = (8/3)
    dx = 0
    dy = 0
    dz = 0
    while(counter !=10000):
        glColor3d(1, 1, 1)
        #formula for the three differential equations
        dx = (a*(y - x)) * dt
        dy = (x*(b - z) - y) * dt
        dz = (x*y - c*z) * dt
        
        glVertex3d(x,y,z)
        
        x = x + dx
        y = y + dy
        z = z + dz
        counter+=1
    
def main(angle):
    #initialize pygame
    pygame.init()
    
    #set the display for the OpenGL
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]), 0.1, 1500)

    glVertex3d(0, 0, -1)
    glRotatef(0,0,0,0)

    glTranslatef(0,0,0)
    
    clock = pygame.time.Clock()
    
    while (True) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        clock.tick(69)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #time.sleep(0.1)
        #pygame.time.wait(10)
        
        #zoom out, translate points and rotate
        if (angle<1):
            glRotatef(angle,-0.5,-angle,-5)
            glTranslatef(0,0,-0.5)
        
        #zoom in, translate points and rotate
        if (angle>1):
            glRotatef(0.9,5,1,-1)
            glTranslatef(0,0,0.01)
            
        glEnable(GL_POINT_SMOOTH)
        glPointSize(1)

        glBegin(GL_POINTS)
    
        lorenz_attractor(x, y, z, counter)
            
        glEnd()
        
        pygame.display.flip()
        angle+=0.005
        
main(angle)