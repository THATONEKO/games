import pygame, sys
from settings import *
from pyvidplayer import Video
from button_class import Button
from lori import *


pygame.init()

# display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("impact_fighters(main_menu")

# set frame rate
clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

vid = Video("intro/Get Into Fighting Games (Intro).mp4")
vid.set_size((SCREEN_WIDTH, SCREEN_HEIGHT))

def intro():
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_menu()


bg_image = pygame.image.load("assets/back_ground/kof2002-japan-stage3.gif").convert_alpha()


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function for fighter health bar
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 1, y - 1, 402, 32))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, (400 * ratio), 30))


# create two instances of fighters
fighter_1 = Lori(200, 310)
fighter_2 = Lori(700, 310)


def play():

    # game loop
    run = True
    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        clock.tick(FSP)

        screen.fill("black")
        # draw background
        draw_bg()

        # show player stats
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

        # move fighters
        fighter_1.move(screen, fighter_2)

        # draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # PLAY_TEXT = get_font(24).render("This is the play screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 260))
        # screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(50, 30),
                           text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")

        PLAY_BACK.change_color(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)


        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.check_for_input(PLAY_MOUSE_POS):
                    main_menu()


        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(500, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        #screen.blit(BG, (0, 0))
        screen.fill("Black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(500, 250),
                             text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(500, 400),
                                text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(500, 550),
                             text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


intro()



