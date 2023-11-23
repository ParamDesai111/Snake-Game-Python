import pygame
import random

pygame.init()

#colors
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

#size
width = 800
height = 600
window = (width, height)

game = pygame.display.set_mode(window)
pygame.display.set_caption("Snake Game")

snake_block_size = 20
snake_speed = 15


font_style = pygame.font.SysFont(None, 50)


def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, BLACK)
    game_window.blit(score_text, [10, 10])


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], snake_block_size, snake_block_size])

def game_loop():
    game_over = False
    game_end = False

   
    x1 = window_width / 2
    y1 = window_height / 2

  
    x1_change = 0
    y1_change = 0

  
    snake_list = []
    snake_length = 1


    apple_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0


    while not game_over:

        while game_end == True:
            game_window.fill(BLACK)
            game_over_text = font_style.render("Game Over!", True, RED)
            game_window.blit(game_over_text, [window_width / 2 - 100, window_height / 2 - 50])
            show_score(snake_length - 1)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_r:
                        game_loop()

        x1 += x1_change
        y1 += y1_change

