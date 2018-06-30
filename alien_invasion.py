import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化，创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    # 创建一个存储子弹的编组
    bullets = Group()

    # 开始循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
