import pygame
from obj import Obj
from random import randint
from bird import Bird

pygame.init()

# Dimensiones de la ventana
largura = 360
altura = 640

# Configuración base
vel_anim = 4      # velocidad del movimiento lateral
vel = 0           # velocidad vertical del pájaro
grvity = 1        # gravedad
jogando = True

# Ventana
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Bird')

# Background
bg = Obj('sprites/flappybird-city-day.png', 0, 0, largura, altura)

# Bird
bird = Bird("sprites/flappybird-down-red.png", largura/4, altura/2, int(largura/6), int(altura/10))

# Pipes
pipe_y = randint(-180, 0)
pipe = Obj("sprites/block-green.png", largura, pipe_y, int(largura/5), int(altura/2.5))
pipe2 = Obj("sprites/block-green.png", largura, pipe_y + 450, int(largura/5), int(altura/2.5))

# Moneda
coin = Obj('sprites/gold.png', pipe.sprite.rect.x + 14, pipe_y + 325, int(largura/8), int(altura/13))

# Ground
ground = Obj("sprites/flappy-bird-base.png", 0, int(altura - altura/5), largura, int(altura/5))
ground2 = Obj("sprites/flappy-bird-base.png", largura, int(altura - altura/5), largura, int(altura/5))

# Puntuación
score = 0


# --- FUNCIONES PRINCIPALES ---

def Draw():
    pygame.font.init()
    font_defaut = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font_defaut, 38, True)
    font_render = font_size.render(str(score), True, (255, 255, 255))

    # Limpia la pantalla
    window.fill((0, 0, 0))

    # Dibuja en orden
    window.blit(bg.sprite.image, bg.sprite.rect)
    window.blit(pipe.sprite.image, pipe.sprite.rect)
    window.blit(pygame.transform.flip(pipe2.sprite.image, False, True), pipe2.sprite.rect)
    window.blit(coin.sprite.image, coin.sprite.rect)
    window.blit(bird.sprite.image, bird.sprite.rect)
    window.blit(ground.sprite.image, ground.sprite.rect)
    window.blit(ground2.sprite.image, ground2.sprite.rect)
    window.blit(font_render, (int(largura/2), int(altura/15)))

    if jogando:
        # Movimiento del suelo
        ground.sprite.rect.x -= vel_anim
        ground2.sprite.rect.x -= vel_anim
        if ground.sprite.rect.x <= -largura:
            ground.sprite.rect.x = largura
        if ground2.sprite.rect.x <= -largura:
            ground2.sprite.rect.x = largura

        # Movimiento de tuberías y moneda
        pipe.sprite.rect.x -= vel_anim
        pipe2.sprite.rect.x -= vel_anim
        coin.sprite.rect.x -= vel_anim

        # Reiniciar tuberías
        if pipe.sprite.rect.x <= -100:
            pipe_y = randint(-180, 0)
            pipe.sprite.rect.x = largura
            pipe.sprite.rect.y = pipe_y
            pipe2.sprite.rect.x = largura
            pipe2.sprite.rect.y = pipe_y + 450
            coin.sprite.rect.x = pipe.sprite.rect.x + 14
            coin.sprite.rect.y = pipe.sprite.rect.y + 325

        # Movimiento del pájaro
        bird.sprite.rect.y += vel

        # Limitar al suelo
        if bird.sprite.rect.y >= ground.sprite.rect.y - bird.sprite.rect.height:
            bird.sprite.rect.y = ground.sprite.rect.y - bird.sprite.rect.height


def Colission():
    global score, jogando

    col_pipe = pygame.sprite.spritecollide(bird.sprite, pipe.group, False)
    col_pipe2 = pygame.sprite.spritecollide(bird.sprite, pipe2.group, False)
    col_coin = pygame.sprite.spritecollide(bird.sprite, coin.group, False)

    if col_pipe or col_pipe2:
        jogando = False
    elif col_coin:
        score += 1
        coin.sprite.rect.y = -50  # desaparece la moneda


def Game_Over():
    font_size = pygame.font.SysFont(None, 50, True)
    text = font_size.render("GAME OVER", True, (255, 0, 0))
    window.blit(text, (largura/2 - 100, altura/2 - 30))
    pygame.display.update()


# FPS
clock = pygame.time.Clock()

loop = True
while loop:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if jogando and bird.sprite.rect.y > 10:
                vel = -12  # impulso hacia arriba

    # Gravedad
    vel += grvity
    if vel > 10:
        vel = 10

    # Límite superior
    if bird.sprite.rect.y < 0:
        bird.sprite.rect.y = 0
        vel = 4

    if jogando:
        Draw()
        Colission()
    else:
        Game_Over()

    pygame.display.update()
