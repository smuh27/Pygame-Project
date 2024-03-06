import pygame, sys, pygame.freetype
from pygame.rect import Rect
from player import Player

WIDTH, HEIGHT = 800,600
BLUE, WHITE = (106, 159, 181), (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
start_img = pygame.image.load("images/start_btn.png").convert_alpha()
exit_img = pygame.image.load("images/exit_btn.png").convert_alpha()
pygame.display.set_caption("Trivia")

player_name = ''
answer_key = {'Kashif was the true creator of the server': False}

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        pos  = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action 

start_button = Button(100, 300, start_img, 0.8)
exit_button = Button(500, 300, exit_img, 0.8)

pygame.init()

def main_menu():
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('Trivia', True, BLUE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT//4)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((202, 228, 241))
        if start_button.draw(screen):
            stage1()
        if exit_button.draw(screen):
            running = False
        screen.blit(text, textRect)
        
        pygame.display.flip()
    pygame.quit()



def stage1():
    font = pygame.font.Font('freesansbold.ttf', 32)
    name_text = font.render('Enter Your Name: ', True, BLUE, )
    textRect = name_text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT//4)
    font = pygame.font.Font('freesansbold.ttf', 24)
    input_box = pygame.Rect(100, 100, 140, 32)
    input_box.center = (WIDTH // 2, HEIGHT//2)
    active = False
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    player_1 = ''
    color = color_passive
    text = ''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_1 = Player(text)
                    stage2(player_1)
        screen.fill((202, 228, 241))

        if active: 
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_box)
        text_surface = font.render(text, True, (255,255,255))
        screen.blit(name_text, textRect)
        screen.blit(text_surface, input_box)
        input_box.w = max(30, text_surface.get_width()+10)
        
        pygame.display.update()


def stage2(player_name):
    font = pygame.font.Font('freesansbold.ttf', 24)
    question = font.render(str(next(iter(answer_key))), True, BLUE, )
    textRect = question.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT//4)
    font = pygame.font.Font('freesansbold.ttf', 24)
    answer_1 = font.render('True', True, BLUE, )
    answer1Rect = answer_1.get_rect()
    answer1Rect.center = (100, 300)
    font = pygame.font.Font('freesansbold.ttf', 24)
    answer_2 = font.render('False', True, BLUE, )
    answer2Rect = answer_1.get_rect()
    answer2Rect.center = (700, 300)
    running = True
    correct_answer = answer_key[str(next(iter(answer_key)))]
    user_answer = None
    while running:
        screen.fill((202, 228, 241))


        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if answer1Rect.collidepoint(event.pos):
                        user_answer = True
                        print("Incorrect")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if answer2Rect.collidepoint(event.pos):
                        user_answer = False
                        print("Correct")
        screen.blit(question, textRect)
        screen.blit(answer_1, answer1Rect)
        screen.blit(answer_2, answer2Rect)

        pygame.display.flip()

    if user_answer == correct_answer:
        print("Correct")
    else:
        print("Incorrect")


    pygame.quit()
