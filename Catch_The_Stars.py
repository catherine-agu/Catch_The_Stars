# Hello I will be giving you a rundown of my code
# It's a bit sloppy(ps i am a beginner that started coding 2 weeks ago), but you know the saying if it works DON'T TOUCH
# Anyway, lets get right to it!

# I start of by importing the big three, pygame for the whole code functionality, sys for when i want to exit game, and random to randomize time, range and whatnot
import pygame
from pygame.locals import*
import sys
import random

# I made these variable score and missed to store how much stars the user scores and missed hence giving them the value of zero as the starting number so more can be added
score = 0
missed = 0

# getting clock to later tell the clock how fast or slow it would go
clock = pygame.time.Clock()


# Making my color combinations, PS not all are used i just like to have options
colorPINK = (255, 200, 200)
colorBLUE = (0, 0, 255)
colorRED = (255, 0, 0)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorYELLOW = (255, 255, 0)

# initializing game
pygame.init()
# Creating the screen and giving it its measurements
screen = pygame.display.set_mode((800, 600), 0, 32)

# Fill the color screen black
screen.fill(colorBLACK)

# Setting the caption orr name of the pygame to be catch the stars
pygame.display.set_caption("Catch the stars!")





# Getting our bools for our while loop later on
running = False
Start = True

# updating screen
pygame.display.update()

# one of the many fonts that will be seen and giving it a size of 50 and will be used for the stars aka *
thirdFont = pygame.font.SysFont(None, 50)

# Class function for the stars, and making it fall at random speeds im sorry i dont have a better in depth explanation for this but this is to help it collide and react to things
class Star(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = thirdFont.render("*", False, colorPINK, colorBLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(3,7) # random speeds between 3 and 7 pixels per frane

# Making the tap and setting its coordinates and it is sprite so i can make it be able to collide with objects and react
tab = pygame.sprite.Sprite()
tab.rect = pygame.Rect(300,500,150,10)

# My list of stars well not technically a list i tried that and failed but lets just call it a list and it basically creates the stars with the help of the class Star function
# And gives them their cooridinates
star1 = Star(colorPINK, 100,140)
star2 = Star(colorWHITE, 250,140)
star3 = Star(colorPINK, 400,140)
star4 = Star(colorWHITE, 550, 140)
star5 = Star(colorYELLOW, 700, 140)
star6 = Star(colorWHITE, 175,140)
star7 = Star(colorWHITE, 325,140)
star8 = Star(colorPINK, 475,140)
star9 = Star(colorWHITE, 625, 140)


# Creating a sprite group called stars
stars = pygame.sprite.Group()
# adding the list of stars i created earlier to this
stars.add(star1, star2, star3, star4, star5, star6, star7, star8, star9)

# Created a font with the size 50 (why didnt i just use the stars font), created a variable named turf to render or add text and color to the exit text,
# Created another variable called exit text to create the measurements and coordinates and then lastly adding it to the screen
fifthFont = pygame.font.SysFont("Arial", 50)
turf = fifthFont.render('EXIT', False, colorWHITE, colorPINK)
exitText = pygame.Rect(200,200,116,60)
screen.blit(turf, exitText)




# main function, basically saying "if running is false do all of this below"
while not running:
    # run event
    for event in pygame.event.get():
        # if the player clicks the red 'x', it is considered a quit game and quits game
        if event.type == QUIT:
            running = True
            pygame.quit()
            sys.exit()
        # if the player clicks the e or the escape button, it is considered a quit game and quit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # if user clicks the exit with the mouse, it is considered a quit game and quits game
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitText.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
    # Pretty self explanatory....
    if Start is True:
        # if the user presses the arrow key left button it moves left 70
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tab.rect.x = tab.rect.x - 70
            # if arrow key right is pressed, move the object right
            if event.key == pygame.K_RIGHT:
                tab.rect.x = tab.rect.x + 70
        # check to see if we collide with the right screen end
        if tab.rect.x > 625:
            tab.rect.x = 624
        # check to see if we collide with the left screen end
        if tab.rect.x < 27:
            tab.rect.x = 28

        # If the stars collide with the tab and if it does it adds 1 to score
        for star in stars:
            star.rect.y += star.speed
            if pygame.sprite.collide_rect(star, tab):
                star.rect.y = 140
                star.rect.x = random.randint(100, 625)
                star.speed = random.randint(3,7)
                score += 1

            # if the stars go beyond the tab it adds 1 to the missed
            if star.rect.y > 540:
                star.rect.y = 140
                star.rect.x = random.randint(100, 625)
                star.speed = random.randint(2, 6)
                missed += 1







        # fills screen black
        screen.fill(colorBLACK)

        # a font with the size 50 (why do i have so many fonts with the same function, im sorry guys))
        myFont = pygame.font.SysFont("Arial", 50)

        #i will start summarizing my text from now on

        # adding {catch the stars} to the screen
        openingText = myFont.render("{Catch The Stars}",False, colorPINK, colorBLACK)

        openingTextRect = openingText.get_rect()
        openingTextRect.left = 210
        openingTextRect.top = 40

        screen.blit(openingText, openingTextRect)

        secondFont = pygame.font.SysFont("Arial", 25)

        # Drawing the border lines for the game
        pygame.draw.line(screen, colorWHITE, (1,25), (800,25),1)
        pygame.draw.line(screen, colorPINK, (25, 1), (25,600), 1)
        pygame.draw.line(screen, colorWHITE, (1, 575), (800, 575), 1 )
        pygame.draw.line(screen, colorPINK, (775, 1), (775, 800), 1)

        # adding the score and missed to the screen and also allowing the values to change
        Score = secondFont.render(f"Score:{score}", False, colorPINK, colorBLACK)
        screen.blit(Score, (650,40))

        Missed = secondFont.render(f"Missed:{missed}", False, colorPINK, colorBLACK)
        screen.blit(Missed, (650,70))



        # Adding the tab and stars to screen
        pygame.draw.rect(screen, colorPINK, tab)
        stars.draw(screen)

    # game over function
    if missed >= 5:
        running = False
        # makes start false so the previous function stops working
        Start = False

        # fills screen black
        screen.fill(colorBLACK)

        # a font with the size 50 (why do i have so many fonts with the same function, im sorry guys))
        myFont = pygame.font.SysFont("Arial", 50)

        # adding {catch the stars} to the screen
        openingText = myFont.render("{Catch The Stars}", False, colorPINK, colorBLACK)

        openingTextRect = openingText.get_rect()
        openingTextRect.left = 210
        openingTextRect.top = 40

        screen.blit(openingText, openingTextRect)

        secondFont = pygame.font.SysFont("Arial", 25)

        # Drawing the border lines for the game
        pygame.draw.line(screen, colorWHITE, (1, 25), (800, 25), 1)
        pygame.draw.line(screen, colorPINK, (25, 1), (25, 600), 1)
        pygame.draw.line(screen, colorWHITE, (1, 575), (800, 575), 1)
        pygame.draw.line(screen, colorPINK, (775, 1), (775, 800), 1)

        # adding the score and missed to the screen and also allowing the values to change
        Score = secondFont.render(f"Score:{score}", False, colorPINK, colorBLACK)
        screen.blit(Score, (650, 40))

        Missed = secondFont.render(f"Missed:{missed}", False, colorPINK, colorBLACK)
        screen.blit(Missed, (650, 70))

        #Removed the stars and tab from showing on screen

        # Adding a you lose text to screen
        forthFont = pygame.font.SysFont("Arial", 75)
        endingText = forthFont.render('YOU LOSE', False, colorBLACK, colorPINK)
        screen.blit(endingText, (215, 250))

        # adding an exit text/button to screen
        fifthFont = pygame.font.SysFont("Arial", 50)
        turf = fifthFont.render('EXIT', False, colorBLACK, colorPINK)
        exitText = pygame.Rect(350,340,170,60)
        screen.blit(turf, exitText)


    # update our screen
    pygame.display.update()
    # makes the clock go 15 frames per second
    clock.tick(15)


# And thst is it i hope you understood everything future me or random person that decides to use or read my code
# Have a great day! :)