#???

import pygame
import math
import random

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кораблик на волне")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SHIP_COLOR = (150, 75, 0)

# Волна
wave_amplitude = random.randint(50, 150)  # Амплитуда волны
wave_frequency = random.uniform(0.01, 0.05)  # Частота волны
wave_phase_shift = random.uniform(0, math.pi * 2)  # Сдвиг фазы

# Размеры корабля
ship_width = random.randint(50, 100)
ship_height = random.randint(20, 40)

def draw_ship(x, y, width, height):
    pygame.draw.rect(screen, SHIP_COLOR, (x - width // 2, y, width, height))
    pygame.draw.polygon(screen, SHIP_COLOR, [(x, y), (x - width // 4, y - height), (x + width // 4, y - height)])

def get_wave_y(x):
    return wave_amplitude * math.cos(wave_frequency * x + wave_phase_shift)

def main():
    global wave_amplitude, wave_frequency, ship_width, ship_height
    running = True
    clock = pygame.time.Clock()

    ship_x = WIDTH // 2
    ship_y = HEIGHT // 2
    angle = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ship_x += 2  # Кораблик движется по оси X
        if ship_x > WIDTH:
            ship_x = 0  # Возвращаем корабль на начало экрана

        ship_y = HEIGHT // 2 + get_wave_y(ship_x)  # Позиция Y зависит от волны
        angle = get_wave_y(ship_x)  # Наклон корабля в зависимости от волны

        # Рисуем волны
        for x in range(0, WIDTH, 10):
            pygame.draw.line(screen, BLUE, (x, HEIGHT // 2 + get_wave_y(x)), (x, HEIGHT // 2), 1)

        #Изменение корабля ЛКМ
        if pygame.mouse.get_pressed()[0]:
            ship_height = random.randint(20, 40)


        draw_ship(ship_x, ship_y, ship_width, ship_height)


        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
