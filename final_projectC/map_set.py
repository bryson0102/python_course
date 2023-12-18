import pygame
import random

pygame.init()

width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 36)
text = '..'
robot = 'R'
text_surface = []
scaled_text_surface = []
width_ran = []
height_ran = []
robotX = []
robotY = []
minX = 24
maxX = 542
minY = 134-25
maxY = 712-25
original_text_width, text_height = font.size(robot)

scaled_text_width = int(original_text_width * 0.6)
scaled_text_height = int(text_height * 1)
# 確認隨機地圖生成，是否有重疊


def check_position(wid, hei):
    for a in range(len(wid)):
        for b in range(a + 1, len(wid)):
            if wid[a] == wid[b] and hei[a] == hei[b]:
                return True
    return False


# 印出地圖，以..作為基底
def element(width_num=0, height_num=0, height_num1=75, width_num1=10):
    for a in range(3):
        text_surface.append(font.render(text, True, (0, 0, 0)))
        screen.blit(text_surface[a], (width_num1 + width_num * 14, height_num1 + height_num * 34 + a * 10))


def robot_position():
    for a in range(len(robotX)):
        scaled_text_surface.append(pygame.transform.scale(font.render(robot, True, (0, 0, 0)),
                                                          (scaled_text_width, scaled_text_height)))
        # 一格初始格為(25,50)，y+14，x+34
        screen.blit(scaled_text_surface[a], (robotX[a], robotY[a]))


# 地圖生成
def map_set():
    for a in range(40):
        element(a)
        element(a, 0, maxY + 34)
    for b in range(1, 19):
        element(0, b)
        element(0, b, 75, maxX + 14)
    for a in range(100):
        element(width_num1=width_ran[a], height_num1=height_ran[a])


# 地圖生成
for i in range(110):
    width_ran.append(random.randrange(minX, maxX+1, 14))
    height_ran.append(random.randrange(minY, maxY+1, 34))

    while check_position(width_ran, height_ran):
        width_ran.pop()
        height_ran.pop()
        width_ran.append(random.randrange(minX, maxX+1, 14))
        height_ran.append(random.randrange(minY, maxY+1, 34))

robotX = width_ran[-10:]
robotY = height_ran[-10:]
for j in range(10):
    robotX[j] += 2
    robotY[j] += 17
