import pygame
import random
import const, colors
from functions import *
pygame.init()
clock = pygame.time.Clock()
def gameLoop():
    x1 = const.DIS_WIDTH / const.DIVIDER_X1_Y1
    y1 = const.DIS_HEIGHT / const.DIVIDER_X1_Y1
    x1_change = 0
    y1_change = 0
    snake_List = []
    foodx = round(random.randrange(0, const.DIS_WIDTH - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
    foody = round(random.randrange(0, const.DIS_HEIGHT - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
    game_over = False
    game_close = False
    while not game_over:
        while game_close == True:
            dis.fill(colors.BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", colors.RED)
            your_score(const.SNAKE_LENGHT - const.SINGLE_SCORE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_q:
                            game_over = True
                            game_close = False
                        case pygame.K_c:
                            gameLoop()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_over = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            x1_change = -const.SNAKE_BLOCK
                            y1_change = const.NONE
                        case pygame.K_RIGHT:
                            x1_change = const.SNAKE_BLOCK
                            y1_change = const.NONE
                        case pygame.K_UP: 
                            y1_change = -const.SNAKE_BLOCK
                            x1_change = const.NONE
                        case pygame.K_DOWN:
                            y1_change = const.SNAKE_BLOCK
                            x1_change = const.NONE
        if x1 >= const.DIS_WIDTH or x1 < const.NONE or y1 >= const.DIS_HEIGHT or y1 < const.NONE:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(colors.BLACK)
        pygame.draw.rect(dis, colors.RED, [foodx, foody, const.SNAKE_BLOCK, const.SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > const.SNAKE_LENGHT:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(const.SNAKE_BLOCK, snake_List)
        your_score(const.SNAKE_LENGHT - const.SINGLE_SCORE)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, const.DIS_WIDTH - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
            foody = round(random.randrange(0, const.DIS_HEIGHT - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
            const.SNAKE_LENGHT += const.SINGLE_SCORE
        clock.tick(const.SNAKE_SPEED)
    pygame.quit()
    quit()
# def game_closing(game_over, game_close):
    
#     while game_close == True:
#             dis.fill(colors.BLACK)
#             message("You Lost! Press C-Play Again or Q-Quit", colors.RED)
#             your_score(const.SNAKE_LENGHT - const.SINGLE_SCORE)
#             pygame.display.update()
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     match event.key:
#                         case pygame.K_q:
#                             game_over = True
#                             game_close = False
#                         case pygame.K_c:
#                             gameLoop()
gameLoop()
