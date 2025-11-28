import pygame as pg
import time
import random
import sys
height, width = 1000, 1300
option_selected = False
screen_selectionSamurai = pg.Rect(100,435, 360,60)
screen_selectionSamurai = pg.Rect(100,435, 360,60)
sys.setrecursionlimit(5000)
pg.init()
gameScreen = pg.display.set_mode((width,height))
br = pg.transform.scale(pg.image.load("images.jpg"), (width,height))
pg.display.set_caption("I the samurai")
font = pg.font.SysFont("Comic_sans", 100)
font2 = pg.font.SysFont("Comic_sans", 60)
font3 = pg.font.SysFont("Comic_sans", 40)
font4 = pg.font.SysFont("Comic_sans", 20)
selection_rect = pg.Rect(450,435, 360,60)
selection_rect2 = pg.Rect(1500,435, 150,60)
SAMWA1 = pg.image.load("SAMWA1.png")
SB1 = pg.transform.scale(pg.image.load("SpeechBubble.png"),(400,90))
def graphics():
    global br
    global option_selected
    if option_selected == False:
        gameScreen.blit(br, (0,0))
        pg.draw.rect(gameScreen, "black", selection_rect)
        pg.draw.rect(gameScreen, "black", selection_rect2)
        Selection_text = font.render("Press Play to Start", 1, "maroon")
        Samurai_text = font2.render("Play", 1, "red")
        Description_text = font3.render("Samurai Would Do Anything To defend their Shogun," , 1, "brown")
        Description_textl2 = font3.render(" Failing to do so would result in the act of ritual sucide" , 1 , "brown")
        Description_textl3 = font3.render("and or the inability to be happy due to", 1 ,"brown")
        Description_textl4 = font3.render("shame as instructed by the code of bushido", 1, "brown")
        SST1l1 = font4.render("Now Where is My honorable", 1 , "red")
        SST1l2 = font4.render("shogun Mutsu Shinto", 1 , "red")
        gameScreen.blit(Selection_text, (200,40))
        gameScreen.blit(Samurai_text, (590,420))
        pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if selection_rect.collidepoint(pos):
                option_selected=True
                if option_selected == True:
                    print("23e")
                    br = pg.transform.scale(pg.image.load("download-1.jpg"), (width,height)) 
                    gameScreen.blit(br, (0,0))
                    gameScreen.blit(SAMWA1, (440,470))
                    gameScreen.blit(SB1, ((440+50+200),(440+200-130)))
                    gameScreen.blit(Description_text, (230,80))
                    gameScreen.blit(Description_textl2, (230,110))
                    gameScreen.blit(Description_textl3, (230,140))
                    gameScreen.blit(Description_textl4, (230,170))
                    time.sleep(5)
                    gameScreen.blit(SST1l1, ((440+50+20+270),(440+200-120)))
                    gameScreen.blit(SST1l2, ((440+50+20+270),(440+200-120+15)))


    pg.display.update()

def main():
     run = True
     while run:
        graphics()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run=False
                break
        pg.event.get()
if __name__ == "__main__" :
    main()
