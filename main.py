#coding=utf-8
import pygame
import sys
#初始化
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()