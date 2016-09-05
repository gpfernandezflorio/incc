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
	facebook = [pygame.image.load("img/facebook.jpg").convert_alpha(),"facebook"]
	facebook_f = [pygame.transform.flip(pygame.image.load("img/facebook.jpg").convert_alpha(),False,True),"facebook_f"]
	facebook_c = [pygame.image.load("img/mod/facebook.jpg").convert_alpha(),"facebook_c"]
	yahoo = [pygame.image.load("img/yahoo.jpg").convert_alpha(),"yahoo"]
	ge = [pygame.image.load("img/ge.jpg").convert_alpha(),"ge"]
	fila = [pygame.image.load("img/fila.jpg").convert_alpha(),"fila"]
	firestone = [pygame.image.load("img/firestone.jpg").convert_alpha(),"firestone"]
	addidas = [pygame.image.load("img/addidas.jpg").convert_alpha(),"addidas"]
	addidas2 = [pygame.image.load("img/addidas2.jpg").convert_alpha(),"addidas2"]
	nike = [pygame.image.load("img/nike.jpg").convert_alpha(),"nike"]
	carrefour = [pygame.image.load("img/carrefour.jpg").convert_alpha(),"carrefour"]
	twitter = [pygame.image.load("img/twitter.jpg").convert_alpha(),"twitter"]
	claro = [pygame.image.load("img/claro.jpg").convert_alpha(),"claro"]
	claro_c = [pygame.image.load("img/mod/claro.jpg").convert_alpha(),"claro_c"]
	claro_f = [pygame.transform.flip(pygame.image.load("img/claro.jpg").convert_alpha(),True,False),"claro_f"]
	cocacola = [pygame.image.load("img/cocacola.jpg").convert_alpha(),"cocacola"]
	cocacola2 = [pygame.image.load("img/cocacola2.jpg").convert_alpha(),"cocacola2"]
	ford = [pygame.image.load("img/ford.jpg").convert_alpha(),"ford"]
	whatsapp = [pygame.image.load("img/whatsapp.jpg").convert_alpha(),"whatsapp"]
	disco = [pygame.image.load("img/disco.jpg").convert_alpha(),"disco"]
	walmart = [pygame.image.load("img/walmart.jpg").convert_alpha(),"walmart"]
	like = [pygame.image.load("img/like.jpg").convert_alpha(),"like"]
	ferrum = [pygame.image.load("img/ferrum.jpg").convert_alpha(),"ferrum"]
	pepsi = [pygame.image.load("img/pepsi.jpg").convert_alpha(),"pepsi"]
	python = [pygame.image.load("img/python.jpg").convert_alpha(),"python"]
	apple = [pygame.image.load("img/apple.jpg").convert_alpha(),"apple"]
	movistar = [pygame.image.load("img/movistar.jpg").convert_alpha(),"movistar"]
	shell = [pygame.image.load("img/shell.jpg").convert_alpha(),"shell"]
	motorola = [pygame.image.load("img/motorola.jpg").convert_alpha(),"motorola"]
	microsoft = [pygame.image.load("img/microsoft.jpg").convert_alpha(),"microsoft"]
	android = [pygame.image.load("img/android.jpg").convert_alpha(),"android"]
	mcdonalds = [pygame.image.load("img/mcdonalds.jpg").convert_alpha(),"mcdonalds"]
	mcdonalds_f = [pygame.transform.flip(pygame.image.load("img/mcdonalds.jpg").convert_alpha(),False,True),"mcdonalds"]

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
			if timer <= 0:					#CONCEPTO	#LETRA		#COLOR		#RUIDO
				tries = [[0,facebook[0],	[whatsapp,	firestone,	ge,			shell]],
						 [1,facebook[0],	[whatsapp,	fila,		ge,			shell]],
						 [2,facebook[0],	[whatsapp,	ford,		ge,			shell]],
						 [3,facebook[0],	[whatsapp,	firestone,	motorola,	shell]],
						 [4,facebook[0],	[whatsapp,	fila,		motorola,	shell]],
						 [5,facebook[0],	[whatsapp,	ford,		motorola,	shell]],
						 [6,facebook[0],	[whatsapp,	firestone,	addidas2,	shell]],
						 [7,facebook[0],	[whatsapp,	fila,		addidas2,	shell]],
						 [8,facebook[0],	[whatsapp,	ford,		addidas2,	shell]],
						 [9,facebook_f[0],	[whatsapp,	firestone,	ge,			shell]],
						[10,facebook_f[0],	[whatsapp,	fila,		ge,			shell]],
						[11,facebook_f[0],	[whatsapp,	ford,		ge,			shell]],
						[12,facebook_f[0],	[whatsapp,	firestone,	motorola,	shell]],
						[13,facebook_f[0],	[whatsapp,	fila,		motorola,	shell]],
						[14,facebook_f[0],	[whatsapp,	ford,		motorola,	shell]],
						[15,facebook_f[0],	[whatsapp,	firestone,	addidas2,	shell]],
						[16,facebook_f[0],	[whatsapp,	fila,		addidas2,	shell]],
						[17,facebook_f[0],	[whatsapp,	ford,		addidas2,	shell]],
						[18,facebook_c[0],	[whatsapp,	firestone,	shell,		ge]],
						[19,facebook_c[0],	[whatsapp,	fila,		shell,		ge]],
						[20,facebook_c[0],	[whatsapp,	ford,		shell,		ge]],
						[21,facebook_c[0],	[whatsapp,	firestone,	shell,		motorola]],
						[22,facebook_c[0],	[whatsapp,	fila,		shell,		motorola]],
						[23,facebook_c[0],	[whatsapp,	ford,		shell,		motorola]],
						[24,facebook_c[0],	[whatsapp,	firestone,	shell,		addidas2]],
						[25,facebook_c[0],	[whatsapp,	fila,		shell,		addidas2]],
						[26,facebook_c[0],	[whatsapp,	ford,		shell,		addidas2]],
#						[11,claro[0],		[movistar,	disco,		cocacola,	pepsi]],
#						[12,claro[0],		[movistar,	apple,		cocacola,	mcdonalds]],
#						[13,claro[0],		[movistar,	shell,		disco,		mcdonalds]],
#						[14,claro_f[0],		[movistar,	shell,		apple,		mcdonalds]],
#						[15,claro_f[0],		[movistar,	disco,		cocacola,	pepsi]],
#						[16,claro_c[0],		[movistar,	disco,		cocacola,	pepsi]],
#						[17,claro_c[0],		[movistar,	ge,			apple,		pepsi]],
#						[18,claro_c[0],		[movistar,	disco,		twitter,	pepsi]],
#						[19,claro_c[0],		[movistar,	facebook,	apple,		mcdonalds]]
#						 [1,disco[0],[carrefour,cocacola,pepsi,claro]],
#						 [2,claro[0],[movistar,pepsi,disco,carrefour]],
#						 [3,movistar[0],[claro,mcdonalds_f,python]],
#						 [4,twitter[0],[facebook,motorola,nike,addidas]],
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
						random.shuffle(tries)
						show = []
						random.shuffle(positions)
						trie = tries[0]
						now = trie[0]
						sy = h
						sx = trie[1].get_rect().w*h/trie[1].get_rect().h
						target = pygame.transform.scale(trie[1], (sx, sy))
						others = []
						for i in trie[2]:
							if i[0].get_rect().w > i[0].get_rect().h:
								sx = w/5
								sy = i[0].get_rect().h*w/5/i[0].get_rect().w
								others.append([pygame.transform.scale(i[0], (sx, sy)),i[1]])
							else:
								sy = h/3
								sx = i[0].get_rect().w*h/3/i[0].get_rect().h
								others.append([pygame.transform.scale(i[0], (sx, sy)),i[1]])
						timer = 1
						estado = 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F8:
					f.close()
					sys.exit()
