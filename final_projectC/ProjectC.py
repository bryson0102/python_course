import pygame
import sys
import time
import map_set as ms
import player_set as ps
import game_text as gt
import game_robot as gr
pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Input in Pygame")
font_end = pygame.font.Font(None, 50)
text = ''
text9 = 'All the robots have crashed into each other'
text10 = 'and you lived to tell the tale! Good job!'

# player_fast_move(X, Y)
#     if event.key == pygame.K_w:
#         if check_player_move(0, -34):
#             playerY -= 34
#     elif event.key == pygame.K_x:
#         if check_player_move(0, 34):
#             playerY += 34
#     elif event.key == pygame.K_d:
#         if check_player_move(14, 0):
#             playerX += 14
#     elif event.key == pygame.K_a:
#         if check_player_move(-14, 0):
#             playerX -= 14
#     elif event.key == pygame.K_q:
#         if check_player_move(-14, -34):
#             playerX -= 14
#             playerY -= 34
#     elif event.key == pygame.K_e:
#         if check_player_move(14, -34):
#             playerX += 14
#             playerY -= 34
#     elif event.key == pygame.K_z:
#         if check_player_move(-14, 34):
#             playerX -= 14
#             playerY += 34
#     elif event.key == pygame.K_c:
#         if check_player_move(14, 34):
#             playerX += 14
#             playerY += 34


input_active = False

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                text += event.unicode
                if text[-1] == 'T':
                    if gt.tel_remaining > 0:
                        gt.tel_remaining -= 1
                        ps.playerX, ps.playerY = ps.check_player_position()
                elif text[-4:] == 'Quit':
                    print('Thanks for playing!')
                    running = False
            elif event.key == pygame.K_s:
                ps.playerX, ps.playerY, text = ps.player_move(ps.playerX, ps.playerY, text)
            else:
                text += event.unicode
    screen.fill((255, 255, 255))

    ms.map_set()
    ms.text_surface = []
    ps.player_position()
    ms.robot_position()
    gt.text_direct(gr.w1, gr.x1)
    gt.text1_direct()
    gr.robot_hit_dead_text()
    gr.robot_dead_text()
    if gr.robot_move():
        print('You have been caught by a robot!')
        pygame.display.flip()
        time.sleep(3)

        running = False
    if not ms.robotX:
        print('All the robots have crashed into each other and you lived to tell the tale! Good job!')
        text_surface10 = font_end.render(text9, True, (0, 255, 0))
        text_surface11 = font_end.render(text10, True, (0, 255, 0))
        screen.blit(text_surface10, (100, 400))
        screen.blit(text_surface11, (100, 450))
        pygame.display.flip()
        time.sleep(5)
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
