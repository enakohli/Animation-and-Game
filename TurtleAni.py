#-------------------------------------------------------------------------------
# Name: Ena Kohli
# Date: 06/07/2017
# Name of Program: Turtle Animation
# Program Description: An animation on a turtle moving across the screen and a person waving
#-------------------------------------------------------------------------------

#Pygame Initialization
import pygame
import sys
from pygame.locals import *
pygame.init()


#Screen Size
WINDOW = pygame.display.set_mode((900,800))


#Name of the caption
pygame.display.set_caption ("ISU Animation - Turtle Animation")


#Colours that are being used
blue = (60,140,228)
darkgreen = (35,133,35)
lightgreen = (118,224,112)
yellow = (240,235,19)
white = (255,255,255)
black = (0,0,0)
lightblue = (137,188,235)
brown = (131,105,91)
darkbrown = (105,82,37)
beige = (178,152,118)
red = (154,26,26)
pink = (215,77,166)
purple = (120,55,237)


#Set the Frames per Second
FPS = 5
fpsClock = pygame.time.Clock()


#Introduce the variables that are being used and where they begin
x = 0
y = 0
a = 700
b = 300
c = 450


#Loop used for the program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #The colour of the background
    WINDOW.fill(blue)


    #The changing values for the variables
    x = x + 1
    a = a - 1
    b = b + 2
    c = c + 1


    #Grass
    pygame.draw.rect(WINDOW,darkgreen,(0, 650, 900, 150))


    #Sun
    pygame.draw.circle(WINDOW, yellow, (750, 150), 70, 0)
    pygame.draw.line(WINDOW, yellow, (750,150), (850,90),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (865,150),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (850,205),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (825,240),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (775,260),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (715,255),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (665,228),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (635,180),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (635,128),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (665,75),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (725,45),5)
    pygame.draw.line(WINDOW, yellow, (750,150), (790,50),5)


    #Moving Cloud
    pygame.draw.circle(WINDOW, white, (x,80), 40, 0)
    pygame.draw.circle(WINDOW, white, (x-40,120), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+10,160), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+60,170), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+110,160), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+150,120), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+40,120), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+80,120), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+110,90), 40, 0)
    pygame.draw.circle(WINDOW, white, (x+50,70), 40, 0)


    #Smaller Cloud One
    pygame.draw.circle(WINDOW, white, (170,280), 40, 0)
    pygame.draw.circle(WINDOW, white, (210,280), 52, 0)
    pygame.draw.circle(WINDOW, white, (270,280), 52, 0)
    pygame.draw.circle(WINDOW, white, (320,280), 40, 0)


    #Smaller Cloud Two
    pygame.draw.circle(WINDOW, white, (530,180), 40, 0)
    pygame.draw.circle(WINDOW, white, (580,180), 52, 0)
    pygame.draw.circle(WINDOW, white, (630,180), 52, 0)
    pygame.draw.circle(WINDOW, white, (680,180), 40, 0)


    #Plane
    pygame.draw.ellipse(WINDOW, lightblue, (b-50, 300,200, 40))
    pygame.draw.polygon(WINDOW, lightblue, ((b,200),(b+10,200),(b+80,320),(b+20,310)))
    pygame.draw.polygon(WINDOW, lightblue, ((b,450),(b+10,450),(b+80,320),(b+20,310)))
    pygame.draw.rect(WINDOW,black,(b+120,310,10,20))


    #Tree
    pygame.draw.rect(WINDOW, brown,(710,430,30,250))
    pygame.draw.circle(WINDOW, darkgreen, (710,400), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (680,420), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (710,460), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (740,470), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (780,460), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (730,445), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (760,410), 35, 0)
    pygame.draw.circle(WINDOW, darkgreen, (780,430), 35, 0)
    pygame.draw.polygon(WINDOW, brown, ((680, 680), (780, 680), (725, 640)))


    #Larger Tree
    pygame.draw.rect(WINDOW, brown,(210,430,30,250))
    pygame.draw.circle(WINDOW, darkgreen, (210,400), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (180,420), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (210,460), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (240,470), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (280,460), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (230,445), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (260,410), 50, 0)
    pygame.draw.circle(WINDOW, darkgreen, (280,430), 50, 0)
    pygame.draw.polygon(WINDOW, brown, ((180, 680), (280, 680), (225, 640)))


    #Red Flower
    pygame.draw.line(WINDOW, darkgreen, (300, 605), (300, 665), 5)
    pygame.draw.ellipse(WINDOW, red, (290,605,20,25))
    pygame.draw.ellipse(WINDOW, red, (290,570,20,25))
    pygame.draw.ellipse(WINDOW, red, (305,590,25,20))
    pygame.draw.ellipse(WINDOW, red, (270,590,25,20))
    pygame.draw.circle(WINDOW, yellow, (300, 600), 10)


    #Pink Flower
    pygame.draw.line(WINDOW, darkgreen, (500, 605), (500, 665), 5)
    pygame.draw.ellipse(WINDOW, pink, (490,605,20,25))
    pygame.draw.ellipse(WINDOW, pink, (490,570,20,25))
    pygame.draw.ellipse(WINDOW, pink, (505,590,25,20))
    pygame.draw.ellipse(WINDOW, pink, (470,590,25,20))
    pygame.draw.circle(WINDOW, yellow, (500, 600), 10)


    #Purple Flower
    pygame.draw.line(WINDOW, darkgreen, (800, 605), (800, 665), 5)
    pygame.draw.ellipse(WINDOW, purple, (790,605,20,25))
    pygame.draw.ellipse(WINDOW, purple, (790,570,20,25))
    pygame.draw.ellipse(WINDOW, purple, (805,590,25,20))
    pygame.draw.ellipse(WINDOW, purple, (770,590,25,20))
    pygame.draw.circle(WINDOW, yellow, (800, 600), 10)


    #Turtle
    if y == 0:
        #Position One
        pygame.draw.line(WINDOW, lightgreen, (a,680), (a-10, 710),10)
        pygame.draw.line(WINDOW, lightgreen, (a+30,680), (a+40, 710),10)
        pygame.draw.line(WINDOW, lightgreen, (a+60,680), (a+50, 715),10)
        pygame.draw.line(WINDOW, lightgreen, (a+90,680), (a+100, 710),10)
        pygame.draw.ellipse(WINDOW, darkbrown, (a-5, 650, 110, 50))
        pygame.draw.circle(WINDOW, lightgreen, (a+5,650), 30, 0)
        pygame.draw.circle(WINDOW, white, (a+15,640), 8, 0)
        pygame.draw.circle(WINDOW, white, (a-5,640), 8, 0)
        pygame.draw.circle(WINDOW, black, (a+15,645), 5, 0)
        pygame.draw.circle(WINDOW, black, (a-5,645), 5, 0)
        pygame.draw.arc(WINDOW, black, (a-5,650,20,20), 3.14, 6.28,2)

        y += 1


    elif y == 1:
        #Position Two
        pygame.draw.line(WINDOW, lightgreen, (a,680), (a+20, 710),10)
        pygame.draw.line(WINDOW, lightgreen, (a+30,680), (a, 710),10)
        pygame.draw.line(WINDOW, lightgreen, (a+60,680), (a+80, 715),10)
        pygame.draw.line(WINDOW, lightgreen, (a+90,680), (a+60, 710),10)
        pygame.draw.ellipse(WINDOW, darkbrown, (a-5, 650, 110, 50))
        pygame.draw.circle(WINDOW, lightgreen, (a+5,650), 30, 0)
        pygame.draw.circle(WINDOW, white, (a+15,640), 8, 0)
        pygame.draw.circle(WINDOW, white, (a-5,640), 8, 0)
        pygame.draw.circle(WINDOW, black, (a+15,645), 5, 0)
        pygame.draw.circle(WINDOW, black, (a-5,645), 5, 0)
        pygame.draw.arc(WINDOW, black, (a-5,650,20,20), 3.14, 6.28,2)

        y -= 1


    #Person
    if y == 0:
        #Position One
        pygame.draw.line(WINDOW, beige, (120,630), (170,605), 10)
        pygame.draw.line(WINDOW, beige, (80,630), (30,605), 10)
        pygame.draw.line(WINDOW, beige, (115,740), (115,685), 10)
        pygame.draw.line(WINDOW, beige, (85,740), (85,670), 10)
        pygame.draw.circle(WINDOW, beige, (30, 605), 10)
        pygame.draw.circle(WINDOW, beige, (165, 610), 10)
        pygame.draw.rect(WINDOW,red, (75,590,50,100))
        pygame.draw.circle(WINDOW, beige, (100, 550), 45)
        pygame.draw.polygon(WINDOW,darkbrown,((50,560),(40,530),(75,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((75,510),(55,530),(70,460)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((130,525),(145,470),(100,500)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((75,510),(90,450),(115,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((87,500),(130,460),(125,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((120,510),(175,520),(150,540)),0)
        pygame.draw.ellipse(WINDOW,beige, (137, 550, 15, 10))
        pygame.draw.ellipse(WINDOW,beige, (50, 550, 15, 10))
        pygame.draw.circle(WINDOW, white, (85,540),8)
        pygame.draw.circle(WINDOW, white, (115,540),8)
        pygame.draw.circle(WINDOW, black, (85,540),2)
        pygame.draw.circle(WINDOW, black, (115,540),2)
        pygame.draw.arc(WINDOW, black, (90,560,20,20), 3.14, 6.28, 2)
        pygame.draw.arc(WINDOW, black, (97,550,10,10), 3.14, 6.38, 1)
        pygame.draw.ellipse(WINDOW, black, (70,740, 25, 10))
        pygame.draw.ellipse(WINDOW, black, (107,740, 25, 10))
        pygame.draw.rect(WINDOW,darkbrown, (75,690,20,30))
        pygame.draw.rect(WINDOW,darkbrown, (105,690,20,30))
        pygame.draw.rect(WINDOW,darkbrown, (75,690,40,15))


    elif y == 1:
        #Position Two
        pygame.draw.line(WINDOW, beige, (120,630), (170,630), 10)
        pygame.draw.line(WINDOW, beige, (80,630), (30,605), 10)
        pygame.draw.line(WINDOW, beige, (115,740), (115,685), 10)
        pygame.draw.line(WINDOW, beige, (85,740), (85,670), 10)
        pygame.draw.circle(WINDOW, beige, (30, 605), 10)
        pygame.draw.circle(WINDOW, beige, (165, 630), 10)
        pygame.draw.rect(WINDOW,red, (75,590,50,100))
        pygame.draw.circle(WINDOW, beige, (100, 550), 45)
        pygame.draw.polygon(WINDOW,darkbrown,((50,560),(40,530),(75,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((75,510),(55,530),(70,460)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((130,525),(145,470),(100,500)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((75,510),(90,450),(115,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((87,500),(130,460),(125,510)),0)
        pygame.draw.polygon(WINDOW,darkbrown,((120,510),(175,520),(150,540)),0)
        pygame.draw.ellipse(WINDOW,beige, (137, 550, 15, 10))
        pygame.draw.ellipse(WINDOW,beige, (50, 550, 15, 10))
        pygame.draw.circle(WINDOW, white, (85,540),8)
        pygame.draw.circle(WINDOW, white, (115,540),8)
        pygame.draw.circle(WINDOW, black, (85,540),2)
        pygame.draw.circle(WINDOW, black, (115,540),2)
        pygame.draw.arc(WINDOW, black, (90,560,20,20), 3.14, 6.28, 2)
        pygame.draw.arc(WINDOW, black, (97,550,10,10), 3.14, 6.38, 1)
        pygame.draw.ellipse(WINDOW, black, (70,740, 25, 10))
        pygame.draw.ellipse(WINDOW, black, (107,740, 25, 10))
        pygame.draw.rect(WINDOW,darkbrown, (75,690,20,30))
        pygame.draw.rect(WINDOW,darkbrown, (105,690,20,30))
        pygame.draw.rect(WINDOW,darkbrown, (75,690,40,15))


    #Bird
    if y == 0:
        #Position One
        pygame.draw.line(WINDOW, black, (c, 205), (c + 20, 220), 5)
        pygame.draw.line(WINDOW, black, (c + 40, 205), (c + 20, 220), 5)


    elif y == 1:
        #Position Two
        pygame.draw.line(WINDOW, black, (c, 225), (c + 20, 220), 5)
        pygame.draw.line(WINDOW, black, (c + 40, 225), (c + 20, 220), 5)


    pygame.display.update()
    fpsClock.tick(FPS)