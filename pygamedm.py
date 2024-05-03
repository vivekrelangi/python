import sys
import pygame as pg
def run_game():
    #Initialize and set up screen.
    pg.init()
    screen = pg.display.set_mode((1200,800))
    bg_color = (230,230,230)
    screen.fill(bg_color)
    screen_rect = screen.get_rect()
    screen_center = screen_rect.center
    #Individual x and y values
    """screen_rect.left, screen_rect.top,screen_rect.right,screen_rect.bottom,screen_rect.centerx,screen_rect.centery,screen_rect.width,screen_rect.height"""
    #Tuples
    """screen_rect.center,screen_rect.size"""
    bullet_rect = pg.Rect(100,100,3,15)
    color=(100,100,100)
    pg.draw.rect(screen,color,bullet_rect)
    ship = pg.image.load('images/ship.bmp')
    ship_rect = ship.get_rect()
    ship_rect.midbottom = screen_rect.midbottom
    pg.display.set_caption("Alien Invasion")

    #Start main loop.
    while True:
        #Start event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        #Refresh screen
        pg.display.flip()

run_game()