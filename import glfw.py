import glfw
from OpenGL.GL import *

# Ukuran window (layar)
WIDTH, HEIGHT = 800, 600

def draw_rectangle(xmin, ymin, xmax, ymax):
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # -----------------------------
    # 1. GAMBAR WINDOW (kiri)
    # -----------------------------
    glViewport(0, 0, WIDTH // 2, HEIGHT)  # kiri layar

    glColor3f(0, 0, 1)  # biru
    draw_rectangle(0.1, 0.1, 0.9, 0.9)

    # titik dalam window
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(0.5, 0.5)
    glEnd()

    # -----------------------------
    # 2. GAMBAR VIEWPORT (kanan)
    # -----------------------------
    glViewport(WIDTH // 2, 0, WIDTH // 2, HEIGHT)  # kanan layar

    glColor3f(0, 1, 0)  # hijau
    draw_rectangle(0.2, 0.2, 0.8, 0.8)

    # hasil transformasi titik
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(0.5, 0.5)  # contoh hasil mapping
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(WIDTH, HEIGHT, "Window vs Viewport", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Set koordinat OpenGL (0 - 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1, 0, 1, -1, 1)

    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()