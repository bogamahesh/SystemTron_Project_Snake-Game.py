import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake settings
snake_block = 20  # Size of the snake segments
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        # Draw each segment of the snake as a circle
        pygame.draw.circle(screen, green, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def draw_food(x, y, color):
    pygame.draw.circle(screen, color, (x + snake_block // 2, y + snake_block // 2), snake_block // 2)

def gameLoop():  # Creating a function
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Blinking food
    blink_foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    blink_foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    blink_food_visible = True
    blink_food_timer = 0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Draw stable food as a circle
        draw_food(foodx, foody, white)

        # Blinking food logic
        blink_food_timer += 1
        if blink_food_timer > 15:  # Change food visibility every 15 frames
            blink_food_visible = not blink_food_visible
            blink_food_timer = 0  # Corrected line

        if blink_food_visible:
            draw_food(blink_foodx, blink_foody, blue)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        # Check for collision with stable food
        if (x1 + snake_block // 2) >= foodx and (x1 - snake_block // 2) <= (foodx + snake_block) and \
           (y1 + snake_block // 2) >= foody and (y1 - snake_block // 2) <= (foody + snake_block):
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Check for collision with blinking food
        if blink_food_visible and (x1 + snake_block // 2) >= blink_foodx and (x1 - snake_block // 2) <= (blink_foodx + snake_block) and \
           (y1 + snake_block // 2) >= blink_foody and (y1 - snake_block // 2) <= (blink_foody + snake_block):
            blink_foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            blink_foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        pygame.display.update()

        # Control the speed of the snake
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()