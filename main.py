#coding=utf-8
import pygame
import sys
import csv
from PIL import Image

#一些定义 - Configs
tilesmapSize=(16,16) #Tilesmap的行列数
tileSize=16 #一个Tile块的边长
tileScale=2

#定义函数 - Functions
def loadMap(data_path):
    '''加载地图 - Load a map'''
    tuples=[]
    with open(data_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            tuples.append(tuple(row))
    return tuple(tuples)
def getTileImage(master_image_path,size,line,column,scale=1.0):
    '''获取一个Tile的图片 - Get the image of a tile'''
    img=Image.open(master_image_path)
    tile_img=img.crop((column*size,line*size,
                       column*size+size,line*size+size))
    tile_img=tile_img.resize((int(size*scale),int(size*scale)),resample=Image.BOX) #这里的重采样使用BOX是为了更有原来像素的味道
    image_data = tile_img.tobytes()
    image_dimensions = tile_img.size
    return pygame.image.fromstring(image_data,image_dimensions,'RGBA')
#定义类 - Classes
pass
#关于Pygame的初始化 - Pygame Init
pygame.init()
screen=pygame.display.set_mode((960,640))
clock=pygame.time.Clock()
#主程序 - Main
map=loadMap('maps/testmap.csv')
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(len(map)):
        for j in range(len(map[0])):
            screen.blit(
                getTileImage('tiles.png',tileSize,int(map[i][j])//tileSize,int(map[i][j])%tileSize,tileScale),
                (j*tileSize*tileScale,i*tileSize*tileScale)
                        )
    # screen.blit(getTileImage('tiles.png',16,2,1,3),(0,0)) #测试getTileImage函数
    pygame.display.flip()