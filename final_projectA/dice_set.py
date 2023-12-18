import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

dice_font = pygame.font.Font(None, 36)
text1 = ""
text2 = ['+-------+', '|          |', '|          |', '|          |', '+-------+']
text3 = 'o'
text_surface2 = ['', '', '', '', '']
width_ran = [-100, -100, -100, -100, -100, -100]
height_ran = [-100, -100, -100, -100, -100, -100]


def dice1(wid, hei):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    screen.blit(text_surface3, (wid + 35, hei + 40))


def dice2(wid, hei, pos):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    if pos:
        screen.blit(text_surface3, (wid + 15, hei + 20))
        screen.blit(text_surface3, (wid + 55, hei + 60))
    else:
        screen.blit(text_surface3, (wid + 55, hei + 20))
        screen.blit(text_surface3, (wid + 15, hei + 60))


def dice3(wid, hei, pos):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    if pos:
        screen.blit(text_surface3, (wid + 15, hei + 20))
        screen.blit(text_surface3, (wid + 35, hei + 40))
        screen.blit(text_surface3, (wid + 55, hei + 60))
    else:
        screen.blit(text_surface3, (wid + 55, hei + 20))
        screen.blit(text_surface3, (wid + 35, hei + 40))
        screen.blit(text_surface3, (wid + 15, hei + 60))


def dice4(wid, hei):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    screen.blit(text_surface3, (wid + 15, hei + 20))
    screen.blit(text_surface3, (wid + 15, hei + 60))
    screen.blit(text_surface3, (wid + 55, hei + 20))
    screen.blit(text_surface3, (wid + 55, hei + 60))


def dice5(wid, hei):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    screen.blit(text_surface3, (wid + 15, hei + 20))
    screen.blit(text_surface3, (wid + 15, hei + 60))
    screen.blit(text_surface3, (wid + 35, hei + 40))
    screen.blit(text_surface3, (wid + 55, hei + 20))
    screen.blit(text_surface3, (wid + 55, hei + 60))


def dice6(wid, hei):
    for i in range(5):
        text_surface2[i] = dice_font.render(text2[i], True, (0, 0, 0))
    for j in range(5):
        screen.blit(text_surface2[j], (wid, hei + 20 * j))
    text_surface3 = dice_font.render(text3, True, (0, 0, 0))
    screen.blit(text_surface3, (wid + 15, hei + 20))
    screen.blit(text_surface3, (wid + 15, hei + 60))
    screen.blit(text_surface3, (wid + 15, hei + 40))
    screen.blit(text_surface3, (wid + 55, hei + 40))
    screen.blit(text_surface3, (wid + 55, hei + 20))
    screen.blit(text_surface3, (wid + 55, hei + 60))
