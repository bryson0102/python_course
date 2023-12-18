import pygame
import random
import map_set as ms

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
player = '@'
font = pygame.font.Font(None, 36)
minX = 24
maxX = 542
minY = 134 - 25
maxY = 712 - 25
disX = 1
disY = 16

original_text_width, text_height = font.size(player)
scaled_text_width = int(original_text_width * 0.5)
scaled_text_height = int(text_height * 1)


# 印出玩家，字有壓縮過
def player_position():
    scaled_text_surface = pygame.transform.scale(font.render(player, True, (0, 0, 0)),
                                                 (scaled_text_width, scaled_text_height))
    # 一格初始格為(25,50)，y+14，x+34
    screen.blit(scaled_text_surface, (playerX, playerY))


def check_player_position():
    X = 0
    Y = 0
    check = True
    while check:
        X = random.randrange(minX + disX, maxX + disX + 1, 14)
        Y = random.randrange(minY + disY, maxY + disY + 16, 34)

        for a in range(110):
            if X - disX != ms.width_ran[a] and Y - disY != ms.height_ran[a] and a == 99:
                check = False
            elif X - disX == ms.width_ran[a] and Y - disY == ms.height_ran[a]:
                break
    return X, Y


def check_player_move(move_playerX, move_playerY):
    X = playerX + move_playerX - disX
    Y = playerY + move_playerY - disY
    for a in range(110):
        if a < 100:
            if X == ms.width_ran[a] and Y == ms.height_ran[a]:
                return False
            elif X == 10 or X == 556 or Y == 75 or Y == maxY + 34:
                return False
            elif a == 99:
                if X != ms.width_ran[a] or Y != ms.height_ran[a]:
                    return True


def player_move(X, Y, t):
    if t[-1:] == 'w':
        if check_player_move(0, -34):
            Y -= 34
        t = ''
    elif t[-1:] == 'x':
        if check_player_move(0, 34):
            Y += 34
        t = ''
    elif t[-1:] == 'd':
        if check_player_move(14, 0):
            X += 14
        t = ''
    elif t[-1:] == 'a':
        if check_player_move(-14, 0):
            X -= 14
        t = ''
    elif t[-1:] == 'q':
        if check_player_move(-14, -34):
            X -= 14
            Y -= 34
        t = ''
    elif t[-1:] == 'e':
        if check_player_move(14, -34):
            X += 14
            Y -= 34
        t = ''
    elif t[-1:] == 'z':
        if check_player_move(-14, 34):
            X -= 14
            Y += 34
        t = ''
    elif t[-1:] == 'c':
        if check_player_move(14, 34):
            X += 14
            Y += 34
        t = ''
    return X, Y, t


playerX, playerY = check_player_position()
