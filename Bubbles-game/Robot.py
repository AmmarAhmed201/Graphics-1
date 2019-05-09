from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for theta in np.arange(0, 2*pi, .01):
        x = .5*sin(theta)
        y = .5+.4*cos(theta)
        glVertex(x,y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for theta in np.arange(0, 2*pi, .01):
        x = .4+.07*sin(theta)
        y = .5+.07*cos(theta)
        glVertex(x,y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for theta in np.arange(0, 2*pi, .01):
        x = -.06+.07*sin(theta)
        y = .5+.07*cos(theta)
        glVertex(x,y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.05*sin(theta) -0.17
        y = 0.08*cos(theta) -0.4
        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.05*sin(theta) +0.17
        y = 0.08*cos(theta) -0.4
        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.3*sin(theta)
        y = 0.4*cos(theta)
        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for theta in np.arange(0,2*pi,0.01):
        x = 0.2*sin(theta)
        y = 0.3*cos(theta)
        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    glVertex2d(.5,.3 )
    glVertex2d(.5,-.3 )
    glVertex2d(-.5,.3 )
    glEnd()



    #----
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"hey")
glutDisplayFunc(draw)
glutMainLoop()
