import pygame
from pygame import *
import random


class pusher:
    def __init__(self, x1, y1, image, obj, do1=None, do2=None, time=0, pos_do=None,
        anti_pos_do=None, infinity=0, proces=2):
        self.x1, self.y1 = x1, y1
        self.image = image
        self.x2, self.y2 = self.image.get_size()
        self.obj = obj
        self.do1 = do1
        self.do2 = do2
        self.time = time
        self.proces = proces
        self.pos_do = pos_do
        self.anti_pos_do = anti_pos_do
        self.infinity = infinity

    def be(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.proces == 2:
            if self.x2 + self.x1 > self.x > self.x1:
                if self.y2 + self.y1 > self.y > self.y1:
                    self.obj.change(self.pos_do)
                    if self.obj.mouse is True:
                        self.t = pygame.time.get_ticks()
                        if self.infinity < 2:
                            self.proces = 1
                        self.obj.change(self.do1)
                else:
                    self.obj.change(self.anti_pos_do)
            else:
                self.obj.change(self.anti_pos_do)
        if self.proces == 1:
            if pygame.time.get_ticks() - self.t > self.time:
                self.obj.change(self.do2)
                if self.infinity < 1:
                    self.proces = 0
                    self.obj.change(self.anti_pos_do)
                else:
                    self.recall()
        if self.proces > 0:
            self.obj.screen.blit(self.image, (self.x1, self.y1))

    def update(self, x1, y1, image, obj, do1=None, do2=None, time=0, pos_do=None, anti_pos_do=None,
        infinity=0):
        self.x1, self.y1, = x1, y1
        self.image = image
        self.x2, self.y2 = self.image.get.size()
        self.obj = obj
        self.do1 = do1
        self.do2 = do2
        self.time = time
        self.mouse = False
        self.pos_do = pos_do
        self.anti_pos_do = anti_pos_do
        self.infinity = infinity

    def recall(self):
        self.proces = 2


def collide(obj1, obj2):
    ret = []
    if obj2.y + obj2.y1 > obj1.y + obj1.y1 > obj2.y and obj1.x + obj1.x1 > obj2.x and obj1.x\
    < obj2.x + obj2.x1:
        ret.append('upcollide')
    if obj2.y + obj2.y1 > obj1.y > obj2.y and obj1.x + obj1.x1 > obj2.x and obj1.x < obj2.x + \
    obj2.x1:
        ret.append('downcollide')
    if 'upcollide' in ret:
        if 'downcollide' in ret:
            if obj1.x < obj2.x:
                return 'leftcollide'
            elif obj1.x + obj1.x1 > obj2.x + obj2.x1:
                return 'rightcollide'
        else:
            return 'upcollide'
    elif 'downcollide' in ret:
        return 'downcollide'


class game:

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
        self.running = True
        self.play = False
        pygame.init()
        self.mouse = False
        self.normal = pygame.font.SysFont(None, 44)
        self.exit_text = self.normal.render('Exit', 1, (0, 0, 0))
        self.exit = pusher(550, 600, self.exit_text, self, 'blackscreen', time=5000)
        self.start_text = self.normal.render('Start', 1, (20, 20, 20))
        self.start = pusher(550, 200, self.start_text, self, 'shine', time=3000)
        self.main_text = self.normal.render('Main Menu', 1, (40, 40, 40))
        self.main_menu = pusher(550, 400, self.main_text, self, 'menu', proces=0)
        self.continue_text = self.normal.render('Continue', 1, (60, 60, 60))
        self.Continue = pusher(550, 200, self.continue_text, self, 'continue', proces=0)

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = True
                else:
                    self.mouse = False
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.play = False
                        self.exit.recall()
                        self.Continue.recall()
                        self.main_menu.recall()
            self.screen.fill((255, 255, 255))
            self.exit.be()
            self.start.be()
            self.main_menu.be()
            self.Continue.be()
            pygame.display.flip()

    def change(self, what):
        self.what = what
        if self.what == 'blackscreen':
            self.all = 255
            while self.running:
                self.screen.fill((self.all, self.all, self.all))
                self.exit.be()
                self.start.be()
                self.all -= 1
                if self.all == 0:
                    self.running = False
                pygame.display.flip()
        if self.what == 'shine':
            self.screen.fill((random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255)))
            pygame.display.flip()
            pygame.time.wait(500)
            self.play = True
            self.exit.proces = 0
        if self.what == 'menu':
            self.start.recall()
            self.Continue.proces = 0
        if self.what == 'continue':
            self.main_menu.proces = 0
            self.exit.proces = 0
            self.play = True

Game = game()
Game.main()
