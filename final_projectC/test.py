import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Width Scaling in Pygame")

font_size = 36
original_font = pygame.font.Font(None, font_size)
text_color = (0, 0, 0)

text_to_display = "Hello, Pygame!"

# 缩放因子，1.0 表示原始大小，小于 1.0 缩小，大于 1.0 放大
scale_factor = 1.5

# 获取原始文本的宽度和高度
original_text_width, text_height = original_font.size(text_to_display)

# 根据缩放因子计算缩放后的宽度和高度
scaled_text_width = int(original_text_width * scale_factor)
scaled_text_height = int(text_height * scale_factor)

# 创建一个新的 Surface，将文本渲染到新的 Surface 上，并进行缩放
scaled_text_surface = pygame.transform.scale(original_font.render(text_to_display, True, text_color), (scaled_text_width, scaled_text_height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # 计算文本显示位置为窗口中央
    text_rect = scaled_text_surface.get_rect(center=(width // 2, height // 2))

    # 将缩放后的文字绘制到屏幕上
    screen.blit(scaled_text_surface, text_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()