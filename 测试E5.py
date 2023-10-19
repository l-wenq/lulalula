import pygame

# 初始化游戏引擎
pygame.init()

# 设置窗口尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario")

# 加载背景图像
background_image = pygame.image.load("background.png").convert()

# 加载角色图像
character_image = pygame.image.load("character.png").convert_alpha()
character_rect = character_image.get_rect()
character_x, character_y = 100, 300

# 游戏主循环
running = True
while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景
    screen.blit(background_image, (0, 0))

    # 移动角色
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= 5
    if keys[pygame.K_RIGHT]:
        character_x += 5

    # 边界检测
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_rect.width:
        character_x = screen_width - character_rect.width

    # 绘制角色
    screen.blit(character_image, (character_x, character_y))

    # 刷新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
