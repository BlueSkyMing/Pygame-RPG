#coding=utf-8
import pygame
import sys
import csv
from PIL import Image

#一些定义
tilesmapSize=(16,16) #Tilesmap的行列数
tileSize=16 #一个Tile块的边长
tileScale=2

#定义函数
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
#定义类
pass
#关于Pygame的初始化
print('-=- Init Pygame -=-')
pygame.init()
screen=pygame.display.set_mode((960,640))
clock=pygame.time.Clock()
#加载Tile
tileImg = []
for i in range(tilesmapSize[0]):
    for j in range(tilesmapSize[1]):
        tileImg.append(getTileImage('assets/tiles.png',tileSize,i,j,tileScale))
#主程序
print('-=- Load Map -=-')
map=loadMap('maps/testmap.csv')

mapPos=[0,0]

print('-=- Game Start -=-')
while True:
    #帧相关（丝滑60fps
    clock.tick(60)

    #按键监测
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        mapPos[0]+=5
    if keys_pressed[pygame.K_RIGHT]:
        mapPos[0]-=5
    if keys_pressed[pygame.K_UP]:
        mapPos[1]+=5
    if keys_pressed[pygame.K_DOWN]:
        mapPos[1]-=5

    #绘制部分
    screen.fill((0, 0, 0))
    for i in range(len(map)):
        for j in range(len(map[0])):
            screen.blit(
                # getTileImage('tiles.png',tileSize,int(map[i][j])//tileSize,int(map[i][j])%tileSize,tileScale), #过时的垃圾
                tileImg[int(map[i][j])],
                (j*tileSize*tileScale+mapPos[0],i*tileSize*tileScale+mapPos[1])
                        )
    # screen.blit(getTileImage('tiles.png',16,2,1,3),(mapPos[0],mapPos[1])) #测试getTileImage函数
    
    #万事俱备，只欠update
    pygame.display.update()