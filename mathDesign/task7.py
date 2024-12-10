import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Броуновское движение")

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Параметры шариков
NUM_BALLS = random.randint(5, 15)
BALLS = []
RADIUS_RANGE = (10, 20)
SPEED_RANGE = (1, 5)  # Диапазон скорости


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Отражение от границ экрана
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other_ball):
        # Проверка на столкновение с другим шариком
        distance = math.sqrt((self.x - other_ball.x) ** 2 + (self.y - other_ball.y) ** 2)
        if distance < self.radius + other_ball.radius:
            angle = math.atan2(self.y - other_ball.y, self.x - other_ball.x) # Вычисление угла столкновения

            # Момент столкновения
            self.dx, self.dy = self.reflect(self.dx, self.dy, angle)
            other_ball.dx, other_ball.dy = self.reflect(other_ball.dx, other_ball.dy, angle)

    def reflect(self, dx, dy, angle):
        # Угол между направлением движения и направлением столкновения
        normal_angle = math.atan2(dy, dx)
        angle_diff = normal_angle - angle
        speed = math.sqrt(dx ** 2 + dy ** 2)

        # Вычисление нового направления после отражения
        new_dx = speed * math.cos(angle_diff)
        new_dy = speed * math.sin(angle_diff)

        return new_dx, new_dy


def create_balls():
    for _ in range(NUM_BALLS):
        radius = random.randint(RADIUS_RANGE[0], RADIUS_RANGE[1])
        x = random.randint(radius, WIDTH - radius)
        y = random.randint(radius, HEIGHT - radius)
        color = random.choice(COLORS)
        BALLS.append(Ball(x, y, radius, color))


def main():
    create_balls()
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for ball in BALLS:
            ball.move()
            ball.draw()

        for i in range(len(BALLS)):
            for j in range(i + 1, len(BALLS)):
                BALLS[i].check_collision(BALLS[j])

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
