from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    # Body
    glColor(0.343, 0.534, 1)
    glVertex2d(.2, .2)
    glVertex2d(-.2, .2)
    glVertex2d(-.2, -.2)
    glVertex2d(.2, - .2)
    glEnd()
    # Right Leg
    glColor(0.412, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(.05, - .2)
    glVertex2d(.15, - .2)
    glVertex2d(.15, -.5)
    glVertex2d(.05, - .5)
    glEnd()
    # Left Leg
    glColor(0.412, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(-.05, - .2)
    glVertex2d(-.15, - .2)
    glVertex2d(-.15, -.5)
    glVertex2d(-.05, - .5)
    glEnd()
    # Left Hand
    glColor(1, 0.412, 0.4)
    glBegin(GL_POLYGON)
    glVertex2d(-.2, .2)
    glVertex2d(-.2, .1)
    glVertex2d(-.4, -.1)
    glVertex2d(-.45, -.05)
    glEnd()
    # Right Hand
    glColor(0.412, 0.3, 1)
    glBegin(GL_POLYGON)
    glVertex2d(.2, .2)
    glVertex2d(.2, .1)
    glVertex2d(0.4, -.1)
    glVertex2d(.45, -.05)
    glEnd()
    # Neck
    glColor(1, 0.67, 0)
    glBegin(GL_POLYGON)
    glVertex2d(.035, .2)
    glVertex2d(-.035, .2)
    glVertex2d(-.035, .28)
    glVertex2d(.035, .28)
    glEnd()
    # Head
    glColor(0.412, 0.412, 0.412)
    glBegin(GL_POLYGON)
    glVertex2d(.2, .28)
    glVertex2d(-.2, .28)
    glVertex2d(-.2, .52)
    glVertex2d(.2, .52)
    glEnd()
    # Mouth
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    a = .05
    b = .05

    for th in np.arange(0, 2 * pi, .001):

        x = a *sin(th)
        y = b *cos(th)
        glVertex2d(x, y )

    glEnd()
    # Nose
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0, .36)
    glVertex2d(-.03, .4)
    glVertex2d(.03, .4)
    glEnd()
    # Right Eye
    glColor(0, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.05, .42)
    glVertex2d(.05, .50)
    glVertex2d(.17, .50)
    glVertex2d(.17, .42)
    glEnd()
    # Left Eye
    glColor(0, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.05, .42)
    glVertex2d(-.05, .50)
    glVertex2d(-.17, .50)
    glVertex2d(-.17, .42)
    glEnd()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"First Program")
glutDisplayFunc(draw)
glutMainLoop()