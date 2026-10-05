import pygame
import random

# 窗口大小和格子大小
WIDTH = 600
HEIGHT = 600
CELL = 20

# 几个颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (230, 60, 60)
GREEN = (60, 200, 80)
DARK = (35, 40, 48)

# 四个方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()
    # 显示中文要用中文字体
    font = pygame.font.SysFont("simhei", 26)

    # 蛇一开始有 3 节，列表里每一项是 [x, y]
    snake = [[300, 300], [280, 300], [260, 300]]
    direction = RIGHT

    # 食物随机落在一个格子上
    food = [random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)]

    score = 0
    running = True

    while running:
        # 一、处理键盘和关闭窗口
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # 不能直接往回走
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # 二、算出蛇头下一步的位置
        head_x = snake[0][0] + direction[0] * CELL
        head_y = snake[0][1] + direction[1] * CELL

        # 撞到墙就结束
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            break

        # 撞到自己就结束
        if [head_x, head_y] in snake:
            break

        # 把新的蛇头加到最前面
        snake.insert(0, [head_x, head_y])

        # 吃到食物就不删尾巴（蛇变长），没吃到就把尾巴删掉
        if head_x == food[0] and head_y == food[1]:
            score = score + 1
            food = [random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)]
        else:
            snake.pop()

        # 三、开始画画面
        screen.fill(DARK)

        # 画食物
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

        # 画蛇
        for body in snake:
            pygame.draw.rect(screen, GREEN, (body[0], body[1], CELL, CELL))

        # 左上角显示分数
        text = font.render(f"得分：{score}", True, WHITE)
        screen.blit(text, (12, 10))

        pygame.display.update()

        # 数字越大蛇跑得越快
        clock.tick(10)

    # 四、游戏结束，把分数显示出来再等一会儿
    screen.fill(DARK)
    over = font.render(f"游戏结束！最终得分：{score}", True, WHITE)
    screen.blit(over, (150, 280))
    pygame.display.update()
    pygame.time.wait(3000)

    pygame.quit()


if __name__ == "__main__":
    main()
