import pygame
import sys
import random
import dice_play as dp
import dice_rule as dr
import time
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 24)
pygame.display.set_caption("Text Input in Pygame")

dice_test = []
dice = []
text = "Enter the sum:"
text1 = ""

width_ran = []
height_ran = []
point = +1
correct = 0
wrong = -1
start_time = time.time()

while dp.tim(start_time):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                width_ran = []
                height_ran = []
                dice_test = []
                dice_num = random.randint(2, 6)
                if point == 1:
                    start_time = time.time()
                # running = dp.tim(start_time)

                if text1 == str(sum(dice)):
                    point += 4
                    correct += 1
                    text1 = ''
                else:
                    text = "Enter the sum:"
                    point -= 1
                    wrong += 1
                    text1 = ''
                for i in range(dice_num):
                    dice_test.append(random.randint(1, 6))
                    width_ran.append((random.randint(25, 700)))
                    height_ran.append((random.randint(160, 450)))

                while dp.check_position(width_ran) and dp.check_position(height_ran):
                    dice_test = []
                    for i in range(dice_num):
                        dice_test.append(random.randint(1, 6))
                        width_ran[i] = (random.randint(25, 700))
                        height_ran[i] = (random.randint(160, 450))
                dice = dice_test
            elif event.key == pygame.K_BACKSPACE:
                text1 = text1[:-1]
            else:
                text1 += event.unicode

    screen.fill((255, 255, 255))
    dr.rule()
    text_surface1 = font.render(text1, True, (0, 0, 0))
    screen.blit(text_surface1, (125, height - 30))
    dp.dice_play(dice, width_ran, height_ran)
    pygame.display.flip()

print(f'答對{correct}題，答錯{wrong}題，總分{point}分')
pygame.quit()
sys.exit()
