import pygame, sys
from random import randint
import pygame
import numpy as np
from mapcreator import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)
		self.image = pygame.image.load('graphics/player.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.direction = pygame.math.Vector2()
		self.speed = 5

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def update(self):
		self.input()
		self.rect.center += self.direction * self.speed


class Tree(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)
		self.image = pygame.transform.scale(pygame.image.load('graphics/tree.png').convert_alpha(),(64,64))
		self.rect = self.image.get_rect(topleft = pos)
class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,image_int,main_group, sub_group=""):
        super().__init__()
        if image_int ==1:
            self.image = pygame.image.load ("graphics/water.png")
        elif image_int ==2:
            self.image = pygame.image.load ("graphics/land.png")
            sub_group.add(self)

        main_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2
	
	def center_target_camera(self,target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h

	def custom_draw(self,player):
		#ground
		self.center_target_camera(player)

		#active
		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)


pygame.init()
vector = pygame.math.Vector2
screen = pygame.display.set_mode((960,640))
clock = pygame.time.Clock()

main_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
land_tile_group = pygame.sprite.Group()

camera_group = CameraGroup()
tile_map = map_creator()
for i in range(0,tile_map.shape[0]):
    for j in range (0,tile_map.shape[1]):
        if tile_map [i][j]==1 or tile_map [i][j]==0:
            Tile(j*64,i*64, 1,camera_group,water_tile_group)
        elif tile_map[i][j]==2:
            Tile(j*64,i*64,2,camera_group,land_tile_group)

for i in range(20):
	random_x = randint(0,1000)
	random_y = randint(0,1000)
	Tree((random_x,random_y),camera_group)

player = Player((640,360),camera_group)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	camera_group.update()
	camera_group.custom_draw(player)

	pygame.display.update()
	clock.tick(60)