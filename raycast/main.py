import pygame
import math

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raycasting Game")

# Карта
map_size = 24
map_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Параметры игрока
player_x = 12
player_y = 12
player_angle = 0
player_speed = 0.2

# Параметры луча
fov = math.pi / 3
num_rays = 800
max_depth = 40

# Цвета
floor_color = (100, 100, 100)
ceiling_color = (200, 200, 200)
wall_color = (150, 200, 200)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 0.1
    if keys[pygame.K_RIGHT]:
        player_angle += 0.1
    if keys[pygame.K_UP]:
        new_x = player_x + math.cos(player_angle) * player_speed
        new_y = player_y + math.sin(player_angle) * player_speed
        if map_grid[int(new_y)][int(new_x)] == 0:
            player_x = new_x
            player_y = new_y
    if keys[pygame.K_DOWN]:
        new_x = player_x - math.cos(player_angle) * player_speed
        new_y = player_y - math.sin(player_angle) * player_speed
        if map_grid[int(new_y)][int(new_x)] == 0:
            player_x = new_x
            player_y = new_y

    # Очистка экрана
    screen.fill(floor_color)

    # Raycasting
    for ray in range(num_rays):
        ray_angle = (player_angle - fov / 2) + (ray / num_rays) * fov
        distance = 0
        hit_wall = False

        eye_x = math.cos(ray_angle)
        eye_y = math.sin(ray_angle)

        while not hit_wall and distance < max_depth:
            distance += 0.1
            test_x = int(player_x + eye_x * distance)
            test_y = int(player_y + eye_y * distance)

            if test_x < 0 or test_x >= map_size or test_y < 0 or test_y >= map_size:
                hit_wall = True
                distance = max_depth
            else:
                if map_grid[test_y][test_x] == 1:
                    hit_wall = True

        # Расчет высоты стены
        wall_height = height / distance
        wall_top = int(height / 2 - wall_height / 2)
        wall_bottom = int(height / 2 + wall_height / 2)

        # Расчет тени
        shade = 1 - distance / max_depth
        shaded_wall_color = (int(wall_color[0] * shade), int(wall_color[1] * shade), int(wall_color[2] * shade))

        # Отрисовка стены
        pygame.draw.line(screen, shaded_wall_color, (ray, wall_top), (ray, wall_bottom))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()