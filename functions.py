import pygame, random
import const, colors
pygame.init()
dis = pygame.display.set_mode((const.DIS_WIDTH, const.DIS_HEIGHT))
pygame.display.set_caption('Snake Game by 00013372_00013186')
font_style = pygame.font.SysFont("montserrat", const.FONT_SIZE)
score_font = pygame.font.SysFont("montserrat", const.FONT_SIZE)
x1 = const.DIS_WIDTH / const.DIVIDER_X1_Y1
y1 = const.DIS_HEIGHT / const.DIVIDER_X1_Y1
x1_change = 0
y1_change = 0
snake_List = []
foodx = round(random.randrange(0, const.DIS_WIDTH - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
foody = round(random.randrange(0, const.DIS_HEIGHT - const.SNAKE_BLOCK) / const.FOODS_CONST) * const.FOODS_CONST
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, colors.YELLOW)
    dis.blit(value, [0, 0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colors.GREEN, [x[0], x[1], const.SNAKE_BLOCK, const.SNAKE_BLOCK])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [const.DIS_WIDTH / const.DIS_W_DIVIDER, const.DIS_HEIGHT / const.DIS_H_DIVIDER])
