#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime
from pygame.locals import *

if __name__ == '__main__':

	pygame.init()

	infoObject = pygame.display.Info()
	w = infoObject.current_w
	h = infoObject.current_h

	screen = pygame.display.set_mode((w,h), FULLSCREEN)
	screen.fill((0,0,0))
	background = pygame.image.load("background.jpg").convert()
	background = pygame.transform.scale(background, (w, h))
	facebook = pygame.image.load("facebook.png").convert_alpha()
	facebook = pygame.transform.scale(facebook, (w, h))
	yahoo = pygame.image.load("yahoo.jpg").convert_alpha()
	yahoo = pygame.transform.scale(yahoo, (w/3, h/3))
	ge = pygame.image.load("ge.jpg").convert_alpha()
	ge = pygame.transform.scale(ge, (w/3, h/3))
	addidas = pygame.image.load("addidas.gif").convert_alpha()
	addidas = pygame.transform.scale(addidas, (w/3, h/3))
	nike = pygame.image.load("nike.jpg").convert_alpha()
	nike = pygame.transform.scale(nike, (w/3, h/3))
	carrefour = pygame.image.load("carrefour.png").convert_alpha()
	carrefour = pygame.transform.scale(carrefour, (w/3, h/3))
	twitter = pygame.image.load("twitter.png").convert_alpha()
	twitter = pygame.transform.scale(twitter, (w/3, h/3))


	estado = 0

	while (1):
		if (estado==0):
			pygame.time.wait(1000)
			screen.fill((0,0,0))
			screen.blit(facebook, Rect(0,0,1,1))
			pygame.display.update()
			pygame.time.wait(100)
			screen.fill((0,0,0))
			pygame.display.update()
			estado = 1
		elif (estado==1):
			screen.fill((255,255,255))
			screen.blit(yahoo, yahoo.get_rect())
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				sys.exit()

