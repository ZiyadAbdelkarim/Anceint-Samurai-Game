import pygame as pg
import time
import random
import sys
height, width = 1000, 2000
option_selected = False
screen_selectionSamurai = pg.Rect(1500,435, 360,60)
screen_selectionSamurai = pg.Rect(100,435, 360,60)
sys.setrecursionlimit(5000)
pg.init()
gameScreen = pg.display.set_mode((width,height))
br = pg.transform.scale(pg.image.load("br.jpg"), (width,height))
pg.display.set_caption("I the samurai")
font = pg.font.SysFont("Comic_sans", 100)
font2 = pg.font.SysFont("Comic_sans", 60)
selection_rect = pg.Rect(100,435, 360,60)
selection_rect2 = pg.Rect(1500,435, 360,60)
def graphics ():
    global br
    global option_selected
    if option_selected == False:
        gameScreen.blit(br, (0,0))
        pg.draw.rect(gameScreen, "black", selection_rect)
        pg.draw.rect(gameScreen, "black", selection_rect2)
        Selection_text = font.render("Choose your Path", 1, "maroon")
        Samurai_text = font2.render("Be a Samurai", 1, "red")
        Shogun_text = font2.render("Be a Shogun", 1, "red")
        gameScreen.blit(Selection_text, (650,40))
        gameScreen.blit(Samurai_text, (100,420))
        gameScreen.blit(Shogun_text, (1500,420))
        pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if screen_selectionSamurai.collidepoint(pos):
                option_selected=True
                if option_selected == True:
                    print("23e")
                    br = pg.transform.scale(pg.image.load("SamuraiBackround.jpg"), (width,height)) 
            gameScreen.blit(br, (0,0))
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
