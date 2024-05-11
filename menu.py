import pygame, sys

class Button():
    def __init__(self, x, y, img, hoveredImg):
        self.img = img
        self.hovered = hoveredImg
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, display):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            print('if')
            display.blit(self.hovered, (self.rect.x, self.rect.y))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(00000)
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        print('click')
                        self.clicked = True
                        break
            return self.clicked
        else:
            print('else')
            display.blit(self.img, (self.rect.x, self.rect.y))


class Menu():
    def __init__(self,caption):
        pygame.init()

        self.display = pygame.display.set_mode((1280,720))
        self.caption = caption
        pygame.display.set_caption(caption)

        self.frame = pygame.image.load("assets/menu_frame.png")
        self.playButton = pygame.image.load('assets/play_button.png').convert_alpha()
        self.hoveredPlayButton = pygame.image.load('assets/hovered_play_button.png').convert_alpha()
        self.playerInput = pygame.image.load('assets/input_frame.png').convert_alpha()
        self.hoveredInput = pygame.image.load('assets/hovered_input.png').convert_alpha()
        self.playBtn = Button(508.5, 602.4, self.playButton, self.hoveredPlayButton)
        self.players = 0
        self.usernames = []


        self.menu = True
        self.askNumber = True

    def run(self):
        while self.menu:
            self.display.fill((165, 234, 241))
            self.display.blit(self.frame, (0, 0))

            btnPressed = self.playBtn.draw(self.display)
            self.menu = False if btnPressed else True
            btnPressed = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        self.menu = False

                    if event.key == pygame.K_ESCAPE:
                        exit()

            #mousePos = pygame.mouse.get_pos()

            pygame.display.update()
        x = 1
        print('a')
        while self.askNumber:
            print(x)
            x += 1
            self.display.fill((165, 234, 241))
            playersBtn = Button(394.6, 63.1, self.playerInput, self.hoveredInput)

            pressed = playersBtn.draw(self.display)
            pygame.display.update()
            
            inputPressed = pressed
            while True:
                if inputPressed:
                    playersBtn = None
                    pressed = None
                    self.display.fill((165, 234, 241))
                    self.display.blit(self.hoveredInput, (394.6, 63.1))
                    self.number = 'assets/' + str(self.players) + '.png'
                    if self.players > 0:
                        self.number = pygame.image.load(self.number)
                        self.display.blit(self.number, (0, 0))
                

                


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_2 and inputPressed == True and self.players == 0:
                            self.players = 2
                        if event.key == pygame.K_3 and inputPressed == True and self.players == 0:
                            self.players = 3
                        if event.key == pygame.K_4 and inputPressed == True and self.players == 0:
                            self.players = 4
                        if event.key == pygame.K_5 and inputPressed == True and self.players == 0:
                            self.players = 5
                        if event.key == pygame.K_6 and inputPressed == True and self.players == 0:
                            self.players = 6
                        if event.key == pygame.K_7 and inputPressed == True and self.players == 0:
                            self.players = 7
                        if event.key == pygame.K_8 and inputPressed == True and self.players == 0:
                            self.players = 8
                        if event.key == pygame.K_RETURN and self.players > 0:
                            print('lol')
                            self.askNumber = False
                        if event.key == pygame.K_BACKSPACE and self.players > 0:
                            self.players = 0
                if inputPressed == False:
                    break
                pygame.display.update()
            pygame.display.update()
        #pygame.quit()

x = Menu('Dye!')
x.run()

