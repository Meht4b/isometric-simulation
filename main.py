import pygame
import math
import random

pygame.init()

window = pygame.display.set_mode((1500,750))

window.fill((100,100,100))

def drawLine(coords,length,angle):
    #pygame.draw.aaline(window,(0,0,0),coords,(coords[0]+length*math.cos(math.radians(angle)),coords[1]+length*math.sin(math.radians(angle))))
    return (coords[0]+length*math.cos(math.radians(angle)),coords[1]+length*math.sin(math.radians(angle)))

def drawRhomb(center,length,angle,color):
    c1 = drawLine(center,length,angle)
    c2 = drawLine(c1,length,angle+60)
    c3 =drawLine(center,length,angle+60)
    c4 = drawLine(c3,length,angle)
    pygame.draw.polygon(window,color,(center,c1,c2,c3),0)
    pygame.draw.aalines(window,(150,150,150),True,[center,c1,c2,c3])
    return c1,c3,c2

def drawHex(center,length,angle):

    if angle==0:
        drawRhomb(center,length,angle-30,(255,255,255)) #brigtest
        a = drawRhomb(center,length,angle-90,(230,230,230)) #second brightest 
        drawRhomb(a[2],length,angle +30,(200,200,200)) #least brightest
    else:
        drawRhomb(center,length,angle-30,(200,200,200)) #third
        a = drawRhomb(center,length,angle-90,(255,255,255)) #brigthest
        drawRhomb(a[2],length,angle +30,(230,230,230)) #second

def drawGrid(lis,xinit,yinit,length):

    x,y = 0,yinit

    for j in range(len(lis)):
        if j&1:
            x = xinit + length*math.cos(math.radians(30))
        else:
            x = xinit
        for i in lis[j]:
            if i:
                drawHex((x,y),length,60)
            else:
                drawHex((x,y+length),length,0)
            x+=2*length*math.cos(math.radians(30))

        y+=length+length*math.sin(math.radians(30))

def drawRandGrid(rows,columns,xinit,yinit,length):
    x,y = 0,yinit
    lis = []

    for j in range(rows):
        lis.append([])
        if j&1:
            x = xinit + length*math.cos(math.radians(30))
        else:
            x = xinit
        for i in range(columns):

            i = random.randint(0,1)
            lis[-1].append(i)
            if i:
                drawHex((x,y),length,60)
            else:
                drawHex((x,y+length),length,0)
            x+=2*length*math.cos(math.radians(30))

        y+=length+length*math.sin(math.radians(30))
    return lis

def createRandGrid(rows,column):
    lis = []
    for j in range(rows):
        lis.append([])
        for i in range(column):
            lis[-1].append(random.randint(0,1))
    return lis

xinit = -50
yinit = 0
length = 50

lis =drawRandGrid(20,20,xinit,yinit,length)



print(2*length*math.cos(math.radians(30)))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                x = pygame.mouse.get_pos()[0]-xinit
                y = pygame.mouse.get_pos()[1]-yinit
                width = 2*length*math.cos(math.radians(30))
                height = length+length*0.5
                yval = (abs(abs(width/2-(x%width))-width/2)/(width/2))/((y%height-50)/(height-50))
                
                if (y//height)%2:
                    yval = (abs(abs(width/2-(x%width)))/(width/2))/((y%height-50)/(height-50))
                if y%height<=50:
                    yind = math.floor(y/height)
                elif yval>1:
                    yind = math.floor(y/height)
                else:
                    yind = math.ceil(y/height)

                if yind%2:
                    xind = math.floor((x-width/2)/width)
                else:
                    xind = math.floor(x/width)
                print(yind,xind)
                print(lis)
                if yind>=0 and xind>=0 and yind<len(lis) and xind<len(lis[0]):
                    if lis[yind][xind]:
                        lis[yind][xind] = 0
                    else:
                        lis[yind][xind] = 1
            except ZeroDivisionError:
                pass

    window.fill((100,100,100))
    drawGrid(lis,xinit,yinit,length)
    pygame.display.update()
      