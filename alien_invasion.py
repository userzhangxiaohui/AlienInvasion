import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
def run_game():
    #初始化并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_heigh))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    #创建子弹组
    bullets = Group()
    #创建外星人
    alien = Alien(ai_settings,screen)
    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,alien,bullets)

run_game()