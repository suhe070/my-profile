from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variabel global (dinamis)
xc, yc, r = 0, 0, 20

def plot_circle_points(xc, yc, x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    glBegin(GL_POINTS)
    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*(x - y) + 1

        plot_circle_points(xc, yc, x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # warna putih

    midpoint_circle(xc, yc, r)

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # background hitam
    gluOrtho2D(-100, 100, -100, 100)  # koordinat 2D

def main():
    global xc, yc, r

    # Input dinamis
    xc = int(input("Masukkan pusat X: "))
    yc = int(input("Masukkan pusat Y: "))
    r = int(input("Masukkan radius: "))

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Midpoint Circle OpenGL")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()