import pygame
import random

def randomise_values():
    "Returns a list with the keypad shuffled"
    random.shuffle(["1","2","3","4","5","6","7","8","9","*","0","+"])
    return lst

def append_to_number(to_add, number): return number+to_add

def draw_init(screen):
    # We are writing easy code not good code
    screen.fill("#1f1f1f")
    pygame.draw.rect(screen, "#2e2e2e", ((20, 20), (340, 60)))

    pygame.draw.rect(screen, "#2e2e2e", ((20, 100), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((140, 100), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((260, 100), (100, 100)))

    pygame.draw.rect(screen, "#2e2e2e", ((20, 220), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((140, 220), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((260, 220), (100, 100)))

    pygame.draw.rect(screen, "#2e2e2e", ((20, 340), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((140, 340), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((260, 340), (100, 100)))

    pygame.draw.rect(screen, "#2e2e2e", ((20, 460), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((140, 460), (100, 100)))
    pygame.draw.rect(screen, "#2e2e2e", ((260, 460), (100, 100)))

    pygame.draw.rect(screen, "#2e2e2e", ((20, 580), (340, 80)))

    pygame.display.update()

def main_window():
    pygame.init()
    screen = pygame.display.set_mode((380, 680))
    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_init(screen)
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
main_window()