import pygame
import math
import random


def minigame():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MiniGame")

    ball_radius = 20
    ball_speed = 5
    spawn_interval = 500  

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    colors = [RED, BLUE, CYAN]

    font = pygame.font.Font(None, 36)

    class Ball:
        def __init__(self, x, y, angle, color):
            self.x = x
            self.y = y
            self.angle = angle
            self.color = color
            if color == RED:
                self.speed = ball_speed * 1.5
                self.radius = ball_radius
                self.points = 3
                self.hits_to_destroy = 1
            elif color == BLUE:
                self.speed = ball_speed * 0.5
                self.radius = ball_radius * 1.5
                self.points = 5
                self.hits_to_destroy = 2
            else:
                self.speed = ball_speed
                self.radius = ball_radius
                self.points = 1
                self.hits_to_destroy = 1

        def move(self):
            self.x += self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle) 
            
            if self.x <= self.radius or self.x >= WIDTH - self.radius:
                self.angle = math.pi - self.angle
            if self.y <= self.radius or self.y >= HEIGHT - self.radius:
                self.angle = -self.angle

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))

    def draw_text(screen, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        screen.blit(text_obj, (x, y))

    def draw_menu(screen):
        screen.fill('BLACK')
        draw_text(screen, "PAUSE MENU", font, 'WHITE', WIDTH // 2 - 100, HEIGHT // 2 - 60)
        draw_text(screen, "Press R to Resume", font, 'WHITE', WIDTH // 2 - 100, HEIGHT // 2 - 20)
        draw_text(screen, "Press Q to Quit", font, 'WHITE', WIDTH // 2 - 100, HEIGHT // 2 + 20)
        pygame.display.flip()

    def draw_crosshair(screen, x, y):
        pygame.draw.line(screen, 'WHITE', (x - 10, y), (x + 10, y), 2)
        pygame.draw.line(screen, 'WHITE', (x, y - 10), (x, y + 10), 2)

    def lock_mouse():
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

    def unlock_mouse():
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)

    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02}"
    
    balls = []
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, spawn_interval)

    score = 0
    total_time = 10  
    paused = False
    start_ticks = pygame.time.get_ticks()

    running = True
    clock = pygame.time.Clock()

    while running:
        if not paused:
            lock_mouse()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == spawn_event:
                    initial_x = random.randint(ball_radius, WIDTH - ball_radius)
                    initial_y = random.randint(ball_radius, HEIGHT - ball_radius)
                    initial_angle = random.uniform(0, 2 * math.pi)
                    color = random.choice(colors)
                    balls.append(Ball(initial_x, initial_y, initial_angle, color))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for ball in balls[:]:
                        if (ball.x - mouse_x) ** 2 + (ball.y - mouse_y) ** 2 <= ball.radius ** 2:
                            ball.hits_to_destroy -= 1
                            if ball.color == BLUE:
                                ball.radius -= ball_radius * 0.5
                            if ball.hits_to_destroy <= 0:
                                score += ball.points
                                balls.remove(ball)
                            break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
            
            screen.fill('PURPLE')
            for ball in balls:
                ball.move()
                ball.draw(screen)
            
            seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
            remaining_time = max(total_time - seconds_passed, 0)
            time_text = format_time(remaining_time)
            draw_text(screen, f"Score: {score}", font, 'WHITE', 10, 10)
            draw_text(screen, f"Time: {time_text}", font, 'WHITE', 10, 50)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            draw_crosshair(screen, mouse_x, mouse_y)

            pygame.display.flip()
            
            if remaining_time == 0:
                running = False
            clock.tick(60)
        else:
            unlock_mouse()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        paused = False
                        start_ticks = pygame.time.get_ticks() - (total_time - remaining_time) * 1000
                    elif event.key == pygame.K_q:
                        running = False
            draw_menu(screen)

    pygame.quit()
    return score
