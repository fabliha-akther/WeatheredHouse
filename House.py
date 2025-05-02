from OpenGL.GL import *
from OpenGL.GLUT import *




day_night = 1.0
rain_bend = 0
rain_positions = [(x, y) for x in range(50, 501, 50) for y in range(500, 0, -100)]


def draw_house():
    #walls
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.25, 0.1)
    glVertex2f(100, 100)
    glVertex2f(100, 300)
    glColor3f(0.7, 0.35, 0.15)
    glVertex2f(400, 300)
    glVertex2f(400, 100)
    glEnd()
    #roof
    glBegin(GL_TRIANGLES)
    glColor3f(0.6, 0.2, 0.2)
    glVertex2f(80, 300)
    glVertex2f(420, 300)
    glColor3f(0.9, 0.3, 0.3)
    glVertex2f(250, 400)
    glEnd()
    #window
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(200, 200)
    glVertex2f(200, 250)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(250, 250)
    glVertex2f(250, 200)
    glEnd()
    #door
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.15, 0.05)
    glVertex2f(275, 100)
    glVertex2f(275, 200)
    glColor3f(0.5, 0.25, 0.1)
    glVertex2f(325, 200)
    glVertex2f(325, 100)
    glEnd()


def draw_rain():
    glBegin(GL_LINES)
    glColor3f(0.5, 0.5, 1.0)
    for x, y in rain_positions:
        glVertex2f(x, y)
        glVertex2f(x + rain_bend, y - 10)
    glEnd()


def animate_rain():
    global rain_positions
    new_positions = []
    for x, y in rain_positions:
        y -= 5
        if y < 0:
            y = 500
        new_positions.append((x, y))
    rain_positions[:] = new_positions
    glutPostRedisplay()


def keyboard(key, x, y):
    global day_night
    if key == b'd':
        if day_night < 1.0:
            day_night += 0.1
    elif key == b'n':
        if day_night > 0.0:
            day_night -= 0.1
    glutPostRedisplay()


def special_keyboard(key, x, y):
    global rain_bend
    if key == GLUT_KEY_LEFT:
        rain_bend = max(rain_bend - 0.5, -5)
    elif key == GLUT_KEY_RIGHT:
        rain_bend = min(rain_bend + 0.5, 5)
    glutPostRedisplay()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(day_night, day_night, day_night, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()
    draw_rain()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"House")
glutDisplayFunc(showScreen)
glutIdleFunc(animate_rain)
glutKeyboardFunc(keyboard)
glutSpecialFunc(special_keyboard)
glutMainLoop()

