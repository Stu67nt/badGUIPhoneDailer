import pygame
import random
from dotenv import load_dotenv
import os
from twilio.rest import Client


def randomise_values():
    "Returns a list with the keypad shuffled"
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+"]
    random.shuffle(lst)
    return lst

def append_to_number(to_add, number): return number + to_add

def draw_init(screen, charset):
    """Draws all the initial squares"""
    # We are writing easy code not good code
    font = pygame.font.SysFont("wingdings", 27)
    screen.fill("#1f1f1f"),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 20), (340, 60))),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 100), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((140, 100), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((260, 100), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 220), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((140, 220), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((260, 220), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 340), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((140, 340), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((260, 340), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 460), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((140, 460), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((260, 460), (100, 100))),
    pygame.draw.rect(screen, "#2e2e2e", ((20, 580), (340, 80)))

    chars = charset.copy()
    lst = []
    for count in range(1, 12):
        choice = random.choice(chars)
        lst.append(choice)
        chars.remove(choice)

    screen.blit(font.render(lst[0], True, "white"), (40, 120))
    screen.blit(font.render(lst[1], True, "white"), (160, 120))
    screen.blit(font.render(lst[2], True, "white"), (280, 120))
    screen.blit(font.render(lst[3], True, "white"), (40, 220))
    screen.blit(font.render(lst[4], True, "white"), (160, 220))
    screen.blit(font.render(lst[5], True, "white"), (280, 220))
    screen.blit(font.render(lst[6], True, "white"), (40, 340))
    screen.blit(font.render(lst[7], True, "white"), (160, 340))
    screen.blit(font.render(lst[8], True, "white"), (280, 340))
    screen.blit(font.render(lst[9], True, "white"), (40, 480))
    screen.blit(font.render(lst[10], True, "white"), (160, 480))
    screen.blit(font.render("Rst", True, "white"), (280, 480))
    screen.blit(font.render("Call", True, "white"), (160, 600))

    pygame.display.update()

def call(number, screen, attempts):
    font = pygame.font.SysFont("Comic Sans MS", 18)
    pygame.draw.rect(screen, "#2e2e2e", ((20, 20), (340, 60)))
    screen.blit(font.render(f"Calling {number}", True, "white"), (40, 40))
    pygame.display.update()
    try:
        load_dotenv()
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_tkn = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_tkn)
        call = client.calls.create(
            to=number,
            from_=os.getenv("OUTBOUND_NUMBER"),
            url="http://demo.twilio.com/docs/voice.xml"
        )
        print(call.sid)
        return 0
    except Exception:
        print("Failed")
        pygame.draw.rect(screen, "#2e2e2e", ((20, 20), (340, 60)))
        screen.blit(font.render(f"Invalid Number LMAO", True, "white"), (40, 40))
        attempts+=1
        pygame.display.update()
        return attempts
    pygame.time.delay(500)

def check_button_input(number, charset, attempts, screen):
    x,y,clicked = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], pygame.mouse.get_pressed()[0]
    if len(number) < 13:
        if (20 <= x <=120) and (100 <= y <= 200) and clicked:
            number += charset[0]; pygame.time.delay(200); return number, charset, attempts
        elif (140 <= x <=240) and (100 <= y <= 200) and clicked:
            number += charset[1]; pygame.time.delay(200); return number, charset, attempts
        elif (260 <= x <=360) and (100 <= y <= 200) and clicked:
            number += charset[2]; pygame.time.delay(200); return number, charset, attempts
        elif (20 <= x <=120) and (220 <= y <= 320) and clicked:
            number += charset[3]; pygame.time.delay(200); return number, charset, attempts
        elif (140 <= x <=240) and (220 <= y <= 320) and clicked:
            number += charset[4]; pygame.time.delay(200); return number, charset, attempts
        elif (260 <= x <=360) and (220 <= y <= 320) and clicked:
            number += charset[5]; pygame.time.delay(200); return number, charset, attempts
        elif (20 <= x <=120) and (340 <= y <= 440) and clicked:
            number += charset[6]; pygame.time.delay(200); return number, charset, attempts
        elif (140 <= x <=240) and (340 <= y <= 440) and clicked:
            number += charset[7]; pygame.time.delay(200); return number, charset, attempts
        elif (260 <= x <=360) and (340 <= y <= 440) and clicked:
            number += charset[8]; pygame.time.delay(200); return number, charset, attempts
        elif (20 <= x <=120) and (460 <= y <= 560) and clicked:
            number += charset[9]; pygame.time.delay(200); return number, charset, attempts
        elif (140 <= x <=240) and (460 <= y <= 560) and clicked:
            number += charset[10]; pygame.time.delay(200); return number, charset, attempts
    if (260 <= x <=360) and (460 <= y <= 560) and clicked:
        pygame.time.delay(200); return "", charset, attempts
    if (20 <= x <= 360) and (580 <=y <= 660) and clicked:
        attempts = call(number, screen, attempts); charset=randomise_values(); return "", charset, attempts
    else: return number, charset, attempts
    pygame.time.delay(400)

def main_window():
    pygame.init()
    screen = pygame.display.set_mode((380, 680))
    clock = pygame.time.Clock()
    running = True
    pygame.font.init()
    font = pygame.font.SysFont("wingdings", 18)
    charset = randomise_values()
    attempts = 0
    number = ""
    draw_init(screen, charset)
    while running:
        if attempts >= 3: font = pygame.font.SysFont("Comic Sans MS", 18)
        else: font = pygame.font.SysFont("wingdings", 18)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        number, charset, attempts = check_button_input(number, charset, attempts, screen)
        pygame.draw.rect(screen, "#2e2e2e", ((20, 20), (340, 60))),
        screen.blit(font.render(number, True, "white"), (40, 40))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_window()