import pygame
pygame.init()

width, height = 800, 600
font = pygame.font.Font(None, 24)
screen = pygame.display.set_mode((width, height))

text = "Enter the sum:"
text1 = "123"
text4 = "Dice Math."
text5 = "Add up the sides of all the dice displayed on the screen."
text6 = "You have 30 seconds to answer as many as possible."
text7 = "You get 4 points for each correct answer and lose 1 point for each incorrect answer."
text8 = "Press Enter to begin..."


# 版面文字繪製
def rule():
    text_surface = font.render(text, True, (0, 0, 0))
    text_surface4 = font.render(text4, True, (0, 0, 0))
    text_surface5 = font.render(text5, True, (0, 0, 0))
    text_surface6 = font.render(text6, True, (0, 0, 0))
    text_surface7 = font.render(text7, True, (0, 0, 0))
    text_surface8 = font.render(text8, True, (0, 0, 0))
    screen.blit(text_surface, (10, height - 30))
    screen.blit(text_surface4, (10, 10))
    screen.blit(text_surface5, (10, 60))
    screen.blit(text_surface6, (10, 80))
    screen.blit(text_surface7, (10, 100))
    screen.blit(text_surface8, (10, 150))
