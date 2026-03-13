import pygame
import math
import random

pygame.init()

"""type hint why? for pygame  They serve as excellent inline documentation, making the code easier to understand and use correctly. 
  '->' symbol is used to annotate the function's return type.
  both above are optional but they can enhance code readability and maintainability, especially in larger projects or when working in teams.
  Calculate the distance between the robot and the battery using the distance formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
  
  
  """

def main_window(size:int, title:str) -> pygame.Surface:
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(title)
    return screen

def main():
    SIZE: int = 600
    screen: pygame.Surface = main_window(SIZE, "THE CHIPS EATER")
    background: pygame.Surface
    food_image: pygame.Surface
    pacman_image: pygame.Surface

    pacmanx: pygame.Vector2
    pacmany: pygame.Vector2
    food1x: pygame.Vector2
    food1y: pygame.Vector2
    food2x: pygame.Vector2
    food2y: pygame.Vector2
    
    count:int = 0
    distance1: int
    distance2: int
    user_quit: bool = False
    e:pygame.event.Event
    title: str = "THE CHIPS EATER"


    """
        Setup assets 

        .convert()- Mostly for jpeg images,  is used to optimize the image for faster blitting onto the screen. It converts the image to a format that matches the display, which can improve performance when rendering the image in the game loop. 
        .convert_alpha() is used for images with transparency (like PNGs) to preserve the alpha channel, allowing for proper rendering of transparent areas.
    """

    screen = main_window(SIZE, title)
    background = pygame.Surface((SIZE, SIZE))
    background.fill((255, 255, 255))
    pacman_image = pygame.image.load("pacman.jpeg").convert()
    food_image = pygame.image.load("food.jpeg").convert()
    pacmanx = random.randint(0, screen.get_width() - pacman_image.get_width())
    pacmany = random.randint(0, screen.get_height() - pacman_image.get_height())
    food1x = random.randint(0, screen.get_width() - food_image.get_width())
    food1y = random.randint(0, screen.get_height() - food_image.get_height())
    food2x = random.randint(0, screen.get_width() - food_image.get_width())
    food2y = random.randint(0, screen.get_height() - food_image.get_height())
    clock =  pygame.time.Clock()

    """
        Events processing loop until the user quits the game.

    """
    while not user_quit:
        count += 1
        if count == 60:
            distance1 = math.sqrt((pacmanx - food1x) ** 2 + (pacmany - food1y) ** 2)
            distance2 = math.sqrt((pacmanx - food2x) ** 2 + (pacmany - food2y) ** 2)

            if distance1 < distance2:
                pacmanx = food1x
                pacmany = food1y
            else:
                pacmanx = food2x
                pacmany = food2y

        elif count == 120:
            pacmanx = random.randint(0, screen.get_width() - pacman_image.get_width())
            pacmany = random.randint(0, screen.get_height() - pacman_image.get_height())
            food1x = random.randint(0, screen.get_width() - food_image.get_width())
            food1y = random.randint(0, screen.get_height() - food_image.get_height())
            food2x = random.randint(0, screen.get_width() - food_image.get_width())
            food2y = random.randint(0, screen.get_height() - food_image.get_height())
            
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEMOTION:
                pass
            elif e.type == pygame.KEYDOWN:
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif e.type == pygame.MOUSEBUTTONUP:
                pass
            elif e.type ==pygame.ACTIVEEVENT:
                pass


        #Draw the background, pacman and food on the screen
        screen.blit(background, (0, 0))
        screen.blit(pacman_image, (pacmanx, pacmany))
        screen.blit(food_image, (food1x, food1y))
        screen.blit(food_image, (food2x, food2y))
        #showbizz the display
        pygame.display.flip()

pygame.quit()
main()