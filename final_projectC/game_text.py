import pygame
import player_set as ps

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 36)
text1 = '(T)teleports remaining:'
text2 = ['(Q)', '(W)', '(E)', '(A)', '(S)', '(D)', '(Z)', '(X)', '(C)']
text5 = 'Enter move or Quit:'
text6 = '--snip--'
text7 = 'Hungry Robots!'
text8 = 'You have been caught by a robot!'
tel_remaining = 2
died_robot = 'X'
text_surface2 = []
direction = []

for i in range(-34, 35, 34):
    for j in range(-14, 15, 14):
        direction.append([j, i])


def text_direct(w1, x1):
    text_surface1 = font.render(text1, True, (0, 0, 0))
    text_surface5 = font.render(text5, True, (0, 0, 0))
    text_surface6 = font.render(text6, True, (0, 0, 0))
    text_surface7 = font.render(text7, True, (0, 0, 0))
    text_surface8 = font.render(str(tel_remaining), True, (0, 0, 0))
    screen.blit(text_surface1, (600, 50))
    screen.blit(text_surface5, (600, 155))
    screen.blit(text_surface6, (600, 200))
    screen.blit(text_surface7, (10, 10))
    screen.blit(text_surface6, (10, 50))
    screen.blit(text_surface8, (880, 50))
    text_surface9 = font.render(died_robot, True, (0, 0, 0))
    for a in range(len(w1)):
        screen.blit(text_surface9, (w1[a], x1[a]))


def text1_direct():
    for a in range(9):
        text_surface2.append(font.render(text2[a], True, (0, 0, 0)))
    for X, Y in direction:
        a = direction.index([X, Y])
        if ps.check_player_move(X, Y):
            if a <= 2:
                screen.blit(text_surface2[a], (835 + a * 40, 85))
            elif a <= 5:
                screen.blit(text_surface2[a], (835 + (a - 3) * 40, 120))
            else:
                screen.blit(text_surface2[a], (835 + (a - 6) * 40, 155))
