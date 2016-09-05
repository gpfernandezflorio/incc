#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime, matplotlib.pyplot
from pygame.locals import *
from PIL import Image
import numpy as np

tiempo_pre_target = 10
tiempo_target = 50
tiempo_pos_target = 10

if __name__ == '__main__':

	pygame.init()

	infoObject = pygame.display.Info()
	w = infoObject.current_w
	h = infoObject.current_h

	f = open("data.txt", 'a')
	d = datetime.datetime.now()
	f.write(str(d.day) + "/" + str(d.month) + "/" + str(d.year) + "\n")

	screen = pygame.display.set_mode((w,h), FULLSCREEN)
	screen.fill((0,0,0))
	facebook = [pygame.image.load("img/facebook.png").convert_alpha(),"facebook"]
	yahoo = [pygame.image.load("img/yahoo.jpg").convert_alpha(),"yahoo"]
	ge = [pygame.image.load("img/ge.jpg").convert_alpha(),"ge"]
	addidas = [pygame.image.load("img/addidas.gif").convert_alpha(),"addidas"]
	nike = [pygame.image.load("img/nike.jpg").convert_alpha(),"nike"]
	carrefour = [pygame.image.load("img/carrefour.png").convert_alpha(),"carrefour"]
	twitter = [pygame.image.load("img/twitter.png").convert_alpha(),"twitter"]
	claro = [pygame.image.load("img/claro.png").convert_alpha(),"claro"]
	cocacola = [pygame.image.load("img/cocacola.png").convert_alpha(),"cocacola"]
	disco = [pygame.image.load("img/disco.jpg").convert_alpha(),"disco"]
	walmart = [pygame.image.load("img/walmart.png").convert_alpha(),"walmart"]
	like = [pygame.image.load("img/like.png").convert_alpha(),"like"]
	ferrum = [pygame.image.load("img/ferrum.png").convert_alpha(),"ferrum"]
	pepsi = [pygame.image.load("img/pepsi.jpg").convert_alpha(),"pepsi"]
	python = [pygame.image.load("img/python.png").convert_alpha(),"python"]
	movistar = [pygame.image.load("img/movistar.jpg").convert_alpha(),"movistar"]
	mcdonalds = [pygame.image.load("img/mcdonalds.jpg").convert_alpha(),"mcdonalds"]
	mcdonalds-f = [pygame.transform.flip(pygame.image.load("img/mcdonalds.jpg").convert_alpha(),False,True),"mcdonalds"]

	tries = []
	show = []
	#positions = [[x, y] for x in range(5) for y in range(3)]
	positions = [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3]]
	target = 0
	now = -1
	others = []

	estado = -1
	timer = 0

	while 1:
		if estado==-1:
			if timer <= 0:
				tries = [[0,facebook[0],[like,ferrum,ge,addidas]],
						 [1,disco[0],[carrefour,cocacola,pepsi,claro]],
						 [2,claro[0],[movistar,pepsi,disco,carrefour]],
						 [3,movistar[0],[claro,mcdonalds_flip,python]],
						 [4,twitter[0],[facebook,motorola,nike,addidas]]
						]
				random.shuffle(tries)
				estado = 0
		if estado==1:
			if timer <= 0:
				screen.fill((255,255,255))
				screen.blit(target, Rect(w/2-target.get_rect().w/2,0,1,1))
				pygame.display.update()
				timer = tiempo_target
				estado = 2
		elif estado==2:
			if timer <= 0:
				screen.fill((0,0,0))
				pygame.display.update()
				timer = tiempo_pos_target
				estado = 3
		elif estado==3:
			if timer <= 0:
				screen.fill((255,255,255))
				x = 0
				for i in others:
					pos = positions[0]
					show.append([[pos[1],pos[0]],i[1]])
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
					done = False
					if estado==0:
						done = True
					elif estado==4:
						pos = pygame.mouse.get_pos()
						x = pos[0]*5/w
						y = pos[1]*3/h
						for i in show:
							if (i[0][0]==x and i[0][1]==y):
								f.write(str(now) + " - " + i[1] + "\n")
								done = True
								break
					if (done):
						if len(tries) == 0:
							screen.fill((0,0,0))
							pygame.display.update()
							timer = tiempo_pre_target
							tries = [[0,facebook[0],[like,ferrum,ge,addidas]],
									 [1,disco[0],[cocacola,contramano,claro,carrefour]],
									 [2,claro[0],[pepsi,disco,movistar,carrefour]],
									 [3,movistar[0],[claro,mcdonalds,python]]
									]
							random.shuffle(tries)
						show = []
						random.shuffle(positions)
						trie = tries[0]
						now = trie[0]
						sy = h
						sx = trie[1].get_rect().w*h/trie[1].get_rect().h
						target = pygame.transform.scale(trie[1], (sx, sy))
						others = []
						sx = w/5
						for i in trie[2]:
							sy = i[0].get_rect().h*w/5/i[0].get_rect().w
							others.append([pygame.transform.scale(i[0], (sx, sy)),i[1]])
						tries.remove(trie)
						timer = 1
						estado = 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F8:
					f.close()
					sys.exit()
