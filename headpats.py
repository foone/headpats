#!/usr/bin/python
import pygame,math
from pygame.constants import *
import sys

BACKGROUND_IMAGE = 'bg.jpg'
HAND_IMAGE = 'hand.png'

TIME_DIV=100.0
PAT_MULT=30
PAT_OFFSET=-40

class Game(object):
	def __init__(self):
		background_surf = pygame.image.load(BACKGROUND_IMAGE)
		pygame.init()
		pygame.display.set_caption('HEADPATS.EXE')
		flags=0
		if '-f' in sys.argv or '--fullscreen' in sys.argv:
			flags|=FULLSCREEN
		self.screen=pygame.display.set_mode(background_surf.get_size(),flags)
		self.bg=background_surf.convert()
		self.hand=pygame.image.load(HAND_IMAGE).convert_alpha()
		self.hand_y=0
	def draw(self):
		screen = self.screen
		screen.blit(self.bg, (0,0))
		screen.blit(self.hand, (160,self.hand_y))
		pygame.display.flip()
	def update(self):
		self.hand_y = PAT_OFFSET + PAT_MULT * math.sin(pygame.time.get_ticks()/TIME_DIV)
	def main_loop(self):
		self.running=True
		while self.running:
			self.update()
			self.draw()
			for event in pygame.event.get():
				if event.type==QUIT:
					self.running=False
				elif event.type==KEYUP:
					if event.key==K_ESCAPE:
						self.running=False
if __name__=='__main__':
	Game().main_loop()
