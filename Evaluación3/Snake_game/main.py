import pygame
import random
import sys

# Inicialización
pygame.init()

# --- Configuración general ---
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colores
BLACK = (30, 30, 30)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (255, 60, 60)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

# Fuente
font = pygame.font.SysFont("consolas", 22, bold=True)

# Ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Cartoon - Niveles 🎮")

clock = pygame.time.Clock()

# --- Funciones ---
def draw_snake(snake):
    for segment in snake:
        x, y = segment
        # Cuerpo con dos tonos verdes para efecto "caricatura"
        pygame.draw.rect(screen, DARK_GREEN, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))
        pygame.draw.rect(screen, GREEN, (x + 4, y + 4, CELL_SIZE - 8, CELL_SIZE - 8))
    # Ojos en la cabeza
    head_x, head_y = snake[0]
    pygame.draw.circle(screen, WHITE, (head_x + 6, head_y + 6), 3)
    pygame.draw.circle(screen, WHITE, (head_x + 14, head_y + 6), 3)
    pygame.draw.circle(screen, BLACK, (head_x + 6, head_y + 6), 1)
    pygame.draw.circle(screen, BLACK, (head_x + 14, head_y + 6), 1)

def draw_food(food_pos):
    x, y = food_pos
    # Círculo rojo con tallo y brillo
    pygame.draw.circle(screen, RED, (x + CELL_SIZE//2, y + CELL_SIZE//2), CELL_SIZE//2 - 2)
    pygame.draw.rect(screen, (80, 40, 0), (x + CELL_SIZE//2 - 1, y - 5, 3, 6))
    pygame.draw.circle(screen, WHITE, (x + 10, y + 8), 2)

def show_info(score, level, objective):
    text = font.render(f"Puntos: {score}   Nivel: {level}   Objetivo: {objective}", True, YELLOW)
    screen.blit(text, (10, 10))

def game_over_screen(score):
    screen.fill(BLACK)
    msg = font.render("💀 GAME OVER 💀", True, RED)
    score_msg = font.render(f"Puntuación final: {score}", True, WHITE)
    retry = font.render("Pulsa [Espacio] para reiniciar o [ESC] para salir", True, WHITE)
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 50))
    screen.blit(score_msg, (WIDTH//2 - score_msg.get_width()//2, HEIGHT//2))
    screen.blit(retry, (WIDTH//2 - retry.get_width()//2, HEIGHT//2 + 40))
    pygame.display.flip()

def level_up_screen(level):
    screen.fill(BLACK)
    msg = font.render(f"🎉 Nivel {level} superado 🎉", True, GREEN)
    nxt = font.render("Presiona [Espacio] para continuar", True, WHITE)
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 20))
    screen.blit(nxt, (WIDTH//2 - nxt.get_width()//2, HEIGHT//2 + 20))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# --- Juego principal ---
def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    change_to = direction
    food_pos = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]
    score = 0
    level = 1
    FPS = 10
    objective = 5
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_SPACE and game_over:
                    return main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if not game_over:
            direction = change_to

            head_x, head_y = snake[0]
            if direction == "UP":
                head_y -= CELL_SIZE
            elif direction == "DOWN":
                head_y += CELL_SIZE
            elif direction == "LEFT":
                head_x -= CELL_SIZE
            elif direction == "RIGHT":
                head_x += CELL_SIZE

            new_head = (head_x, head_y)

            # Colisiones
            if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake):
                game_over = True
                continue

            snake.insert(0, new_head)

            # Comer comida
            if head_x == food_pos[0] and head_y == food_pos[1]:
                score += 1
                food_pos = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]
            else:
                snake.pop()

            # Subir de nivel
            if score >= objective:
                level += 1
                objective += 5
                FPS += 2
                level_up_screen(level)

            # Dibujar
            screen.fill(BLACK)
            draw_snake(snake)
            draw_food(food_pos)
            show_info(score, level, objective)
            pygame.display.flip()
            clock.tick(FPS)
        else:
            game_over_screen(score)

# Ejecutar el juego
if __name__ == "__main__":
    main()

