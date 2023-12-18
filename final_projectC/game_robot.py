import pygame
import map_set as ms
import player_set as ps


width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
font_end = pygame.font.Font(None, 50)

text8 = 'You have been caught by a robot!'
playerX_edge = 10
playerY_edge = 20
robot_m = 0.05
w1 = []
x1 = []
y1 = []
z1 = []


def robot_move():
    for a in range(len(ms.robotX)):
        if abs(ms.robotX[a] - ps.playerX) < playerX_edge and abs(ms.robotY[a] - ps.playerY) < playerY_edge:
            text_surface10 = font_end.render(text8, True, (255, 0, 0))
            screen.blit(text_surface10, (200, 400))
            return True
        if ms.robotX[a] - ps.playerX > 0 and ms.robotY[a] == ps.playerY:
            ms.robotX[a] -= robot_m
        elif ms.robotX[a] - ps.playerX < 0 and ms.robotY[a] == ps.playerY:
            ms.robotX[a] += robot_m
        elif ms.robotY[a] - ps.playerY > 0 and ms.robotX[a] == ps.playerX:
            ms.robotY[a] -= robot_m
        elif ms.robotY[a] - ps.playerY < 0 and ms.robotX[a] == ps.playerX:
            ms.robotY[a] += robot_m
        elif (ms.robotX[a] - ps.playerX > 0) and (ms.robotY[a] - ps.playerY > 0):
            ms.robotX[a] -= robot_m
            ms.robotY[a] -= robot_m
        elif (ms.robotX[a] - ps.playerX > 0) and (ms.robotY[a] - ps.playerY < 0):
            ms.robotX[a] -= robot_m
            ms.robotY[a] += robot_m
        elif (ms.robotX[a] - ps.playerX < 0) and (ms.robotY[a] - ps.playerY > 0):
            ms.robotX[a] += robot_m
            ms.robotY[a] -= robot_m
        elif (ms.robotX[a] - ps.playerX < 0) and (ms.robotY[a] - ps.playerY < 0):
            ms.robotX[a] += robot_m
            ms.robotY[a] += robot_m
    return False


def robot_hit_dead_text():
    if robot_hit_dead():
        w, x = robot_hit_dead()
        w1.append(w)
        x1.append(x)
        ms.robotX.remove(w)
        ms.robotY.remove(x)


def robot_hit_dead():
    for a in range(len(ms.robotX)):
        for b in range(len(w1)):
            if abs(ms.robotX[a] - w1[b]) < playerX_edge and abs(ms.robotY[a] - x1[b]) < playerY_edge:
                return ms.robotX[a], ms.robotY[a]


def robot_dead():
    for a in range(len(ms.robotX)):
        for b in range(a + 1, len(ms.robotX)):
            # if not w1:
            if abs(ms.robotX[b] - ms.robotX[a]) < playerX_edge and abs(ms.robotY[b] - ms.robotY[a]) < playerY_edge:
                return ms.robotX[b], ms.robotY[b], ms.robotX[a], ms.robotY[a]


def robot_dead_text():
    if robot_dead():
        w, x, y, z = robot_dead()
        w1.append(w)
        x1.append(x)
        w1.append(y)
        x1.append(z)
        ms.robotX.remove(w)
        ms.robotY.remove(x)
        ms.robotX.remove(y)
        ms.robotY.remove(z)
