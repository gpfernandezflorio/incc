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
	facebook = [pygame.image.load("facebook.png").convert_alpha(),"facebook"]
	yahoo = [pygame.image.load("yahoo.jpg").convert_alpha(),"yahoo"]
	ge = [pygame.image.load("ge.jpg").convert_alpha(),"ge"]
	addidas = [pygame.image.load("addidas.gif").convert_alpha(),"addidas"]
	nike = [pygame.image.load("nike.jpg").convert_alpha(),"nike"]
	carrefour = [pygame.image.load("carrefour.png").convert_alpha(),"carrefour"]
	twitter = [pygame.image.load("twitter.png").convert_alpha(),"twitter"]
	claro = [pygame.image.load("claro.png").convert_alpha(),"claro"]
	cocacola = [pygame.image.load("cocacola.png").convert_alpha(),"cocacola"]
	contramano = [pygame.image.load("contramano.jpg").convert_alpha(),"contramano"]
	disco = [pygame.image.load("disco.jpg").convert_alpha(),"disco"]
	walmart = [pygame.image.load("walmart.png").convert_alpha(),"walmart"]
	like = [pygame.image.load("like.png").convert_alpha(),"like"]
	ferrum = [pygame.image.load("ferrum.png").convert_alpha(),"ferrum"]


	tries = [[0,facebook[0],[like,ferrum,ge,addidas]],
			 [1,disco[0],[cocacola,contramano,claro,walmart,carrefour]]]
	results = []
	show = []
	#positions = [[x, y] for x in range(5) for y in range(3)]
	positions = [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3]]
	random.shuffle(tries)
	target = 0
	now = -1
	others = []

	estado = 0
	timer = 100

	while 1:
		if estado==1:
			if timer <= 0:
				screen.fill((0,0,0))
				screen.blit(target, Rect(0,0,1,1))
				pygame.display.update()
				timer = 10
				estado = 2
		elif estado==2:
			if timer <= 0:
				screen.fill((0,0,0))
				pygame.display.update()
				timer = 10
				estado = 3
		elif estado==3:
			if timer <= 0:
				screen.fill((255,255,255))
				x = 0
				for i in others:
					pos = positions[0]
					show.append([pos,i[1]])
					screen.blit(i[0], (pos[1]*w/5,pos[0]*h/3))
					x = x + w/5
					positions.remove(pos)
					positions.append(pos)
				pygame.display.update()
				random.shuffle(positions)
				estado = 4

		timer = timer-1
		pygame.time.wait(10)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					pos = pygame.mouse.get_pos()
					x = pos[0]*5/w
					y = pos[1]*3/h
					for i in show:
						if (i[0][0]==x and i[0][1]==y):
							print("Apretaste " + i[1])
#					results.append()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F8:
					sys.exit()
				elif event.key == pygame.K_RETURN:
					#if (estado==0):
					if len(tries) > 0:
						show = []
						random.shuffle(positions)
						trie = tries[0]
						now = trie[0]
						target = pygame.transform.scale(trie[1], (w, h))
						others = []
						sx = w/5
						for i in trie[2]:
							sy = i[0].get_rect().h*w/5/i[0].get_rect().w
							others.append([pygame.transform.scale(i[0], (sx, sy)),i[1]])
						tries.remove(trie)
						timer = 1
						estado = 1
