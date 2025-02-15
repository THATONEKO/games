import pygame
from settings import *

class Lori():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 235))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # get key presses
        key = pygame.key.get_pressed()

        # movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        # can only perform other actions if not currently attacking
        if self.attacking is False:
            # jumping
            if key[pygame.K_w] and self.jump is False:
                self.vel_y = -30
                self.jump = True

            # attack
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)

                # determine which attack type was used
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 1

        # apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right
        if self.rect.bottom + dy > SCREEN_HEIGHT - 60:
            self.vel_y = 0
            self.jump = False
            dy = SCREEN_HEIGHT - 55 - self.rect.bottom

        # ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
