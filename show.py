#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime, matplotlib.pyplot
from pygame.locals import *
from PIL import Image
import numpy as np

tiempo_pre_target = 10
tiempo_target = 50
tiempo_pos_target = 10

global_timer = 10 * 60 * 1

if __name__ == '__main__':

	pygame.init()

	infoObject = pygame.display.Info()
	w = infoObject.current_w
	h = infoObject.current_h

	d = datetime.datetime.now()

	screen = pygame.display.set_mode((w,h), FULLSCREEN)
	screen.fill((0,0,0))
	facebook = [pygame.image.load("img/facebook.jpg").convert_alpha(),"facebook"]
	yahoo = [pygame.image.load("img/yahoo.jpg").convert_alpha(),"yahoo"]
	ge = [pygame.image.load("img/ge.jpg").convert_alpha(),"ge"]
	fila = [pygame.image.load("img/fila.jpg").convert_alpha(),"fila"]
	firestone = [pygame.image.load("img/firestone.jpg").convert_alpha(),"firestone"]
	addidas = [pygame.image.load("img/addidas.jpg").convert_alpha(),"addidas"]
	addidas2 = [pygame.image.load("img/addidas2.jpg").convert_alpha(),"addidas2"]
	nike = [pygame.image.load("img/nike.png").convert_alpha(),"nike"]
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
	mcdonalds1 = [pygame.image.load("img/mcDonals.png").convert_alpha(),"mcdonalds1"]
	mario = [pygame.image.load("img/mario.png").convert_alpha(),"mario"]
	pam = [pygame.image.load("img/paginasAmarillas.png").convert_alpha(),"paginas amarillas"]
	cat = [pygame.image.load("img/cat.png").convert_alpha(),"cat"]
	bic = [pygame.image.load("img/bic.png").convert_alpha(),"bic"]
	fila1 = [pygame.image.load("img/fila1.png").convert_alpha(),"fila1"]
	pizzahut1 = [pygame.image.load("img/pizzahut1.jpg").convert_alpha(),"pizzahut1"]
	burgerking = [pygame.image.load("img/burgerKing.jpg").convert_alpha(),"burger king"]
	manaos = [pygame.image.load("img/manaos.png").convert_alpha(),"manaos"]
	crush = [pygame.image.load("img/crush.jpg").convert_alpha(),"crush"]
	fanta = [pygame.image.load("img/fanta.png").convert_alpha(),"fanta"]
	volkswagen = [pygame.image.load("img/volkswagen.png").convert_alpha(),"vw"]
	v = [pygame.image.load("img/v.png").convert_alpha(),"v"]
	wordpress = [pygame.image.load("img/wordpress.jpg").convert_alpha(),"word press"]
	chevrolet = [pygame.image.load("img/chevrolet.png").convert_alpha(),"chevrolet"]
	mitsubishi = [pygame.image.load("img/mitsubishi.png").convert_alpha(),"mitsubishi"]
	google = [pygame.image.load("img/googlePlus.png").convert_alpha(),"google"]
	pinterest = [pygame.image.load("img/pinterest.png").convert_alpha(),"pinterest"]
	puma = [pygame.image.load("img/puma.png").convert_alpha(),"puma"]
	ital = [pygame.image.load("img/italMexicana.jpeg").convert_alpha(),"ital"]
	wm = [pygame.image.load("img/warnerMusic.png").convert_alpha(),"warner music"]
	superman = [pygame.image.load("img/superman.jpg").convert_alpha(),"superman"]
	farmacity = [pygame.image.load("img/farmacity.png").convert_alpha(),"farmacity"]
	america = [pygame.image.load("img/america.png").convert_alpha(),"america"]
	apple2 = [pygame.image.load("img/apple.png").convert_alpha(),"apple2"]
	audi = [pygame.image.load("img/audi.png").convert_alpha(),"audi"]
	havana = [pygame.image.load("img/havanna.jpg").convert_alpha(),"havana"]
	honda = [pygame.image.load("img/honda.jpg").convert_alpha(),"honda"]
	olimpiadas = [pygame.image.load("img/olimpiadas.png").convert_alpha(),"olimpiadas"]
	sube = [pygame.image.load("img/sube.jpg").convert_alpha(),"sube"]
	toilet = [pygame.image.load("img/toilet.png").convert_alpha(),"toilet"]
	unicenter = [pygame.image.load("img/unicenter.jpg").convert_alpha(),"unicenter"]
	bic2 = [pygame.image.load("img/bic2.png").convert_alpha(),"bic2"]
	chrome = [pygame.image.load("img/chrome.png").convert_alpha(),"chrome"]
	nueve = [pygame.image.load("img/canal9.jpg").convert_alpha(),"canal9"]
	tvpublica = [pygame.image.load("img/canal7.png").convert_alpha(),"canal7"]
	cruz = [pygame.image.load("img/cruz.png").convert_alpha(),"cruz"]
	cruzroja = [pygame.image.load("img/cruzr.gif").convert_alpha(),"cruzroja"]
	drahorro = [pygame.image.load("img/drAhorro.jpg").convert_alpha(),"drahorro"]
	fantoche = [pygame.image.load("img/fantoche.jpg").convert_alpha(),"fantoche"]
	guaymallen = [pygame.image.load("img/Guaymallen.jpg").convert_alpha(),"guaymallen"]
	gamecube = [pygame.image.load("img/gameCube.jpg").convert_alpha(),"gamecube"]
	jorgito = [pygame.image.load("img/Jorgito.gif").convert_alpha(),"jorgito"]
	michelin = [pygame.image.load("img/michelin.png").convert_alpha(),"michelin"]
	xbox = [pygame.image.load("img/xbox.png").convert_alpha(),"xbox"]
	spiderman = [pygame.image.load("img/spiderman.jpg").convert_alpha(),"spiderman"]
	batman = [pygame.image.load("img/batman.gif").convert_alpha(),"batman"]
	linterna = [pygame.image.load("img/linterna.png").convert_alpha(),"linterna"]
	dot = [pygame.image.load("img/dot.jpg").convert_alpha(),"dot"]
	suzuki = [pygame.image.load("img/suzuki.jpg").convert_alpha(),"suzuki"]

	imagenes = [facebook, yahoo, ge, fila, firestone, addidas, addidas2, nike, carrefour, twitter, claro, cocacola, cocacola2, ford, whatsapp, disco, walmart, like, ferrum, pepsi, python, apple, movistar, shell, motorola, microsoft, android, mcdonalds, mcdonalds1, mario, pam, cat, bic, fila1, pizzahut1, burgerking, manaos, crush, fanta, volkswagen, v, wordpress, chevrolet, mitsubishi, google, pinterest, puma, ital, wm, superman, farmacity, america, apple, audi, havana, honda, olimpiadas, sube, toilet, unicenter, bic2, chrome, nueve, tvpublica, cruz, cruzroja, drahorro, fantoche, guaymallen, gamecube, jorgito, michelin, xbox, spiderman, batman, linterna, dot, suzuki]
	show = []
	#positions = [[x, y] for x in range(5) for y in range(3)]
	positions = [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3]]
	target = 0
	now = -1
	others = []
	in_random = False

	estado = 0
	timer = 0
	g_timer = 0
	font = pygame.font.SysFont("digital", w/10, True)

	time_left = ""

	trials = [									#CONCEPTO																			#LETRA																			#COLOR																	#RUIDO
					[movistar,				[claro],													[mcdonalds,motorola,mario],									[farmacity,sube],						[pepsi,bic,burgerking,carrefour,ge,mitsubishi,pam]],
					[claro,						[movistar],												[whatsapp,motorola,wordpress],							[firestone, honda,mitsubishi],[fila1,chevrolet,pam,addidas,farmacity,toilet]],
					[mcdonalds1,			[pizzahut1,burgerking],						[movistar,motorola,mario],									[pam,cat,bic],							[addidas2,nike,fila,twitter,volkswagen,farmacity]],
					[cocacola,				[manaos,crush,fanta],							[motorola,whatsapp,volkswagen,wordpress],		[honda,mitsubishi,firestone],[addidas2,walmart,bic,sube,facebook,toilet]],
					[volkswagen,			[chevrolet,mitsubishi,honda,ford],[v,cocacola,disco,wordpress,whatsapp],			[addidas2,twitter,ferrum,carrefour],[superman,android,unicenter,havana,fanta]],
					[facebook,				[whatsapp,google,pinterest],			[fila1,firestone],													[motorola,addidas2,volkswagen],[bic,crush,pam,superman,honda,mitsubishi]],
					[addidas,					[fila,nike,puma],									[ital,wm],																	[toilet,wordpress,v],				[apple2,android,superman,crush,firestone,disco]],
					[america,					[nueve,tvpublica],								[gamecube],																	[olimpiadas,microsoft,apple2,chrome],[toilet,puma,wordpress]],
					[android,					[apple2,microsoft],								[toilet,michelin,bic2],											[farmacity,xbox],								[disco,superman,volkswagen,ge,pam,bic]],
					[audi,						[honda,chevrolet,mitsubishi],			[olimpiadas],																[puma,fila1,addidas],						[carrefour,movistar,microsoft,farmacity]],
					[disco,						[carrefour,walmart],							[motorola,volkswagen,wordpress],						[honda,mcdonalds],						[pam,toilet,android,nike,twitter]],
					[chevrolet,				[ford,honda,volkswagen,mitsubishi],[cruz,farmacity,cruzroja],									[cat,pam,mcdonalds1],					[unicenter,twitter,pepsi,android,yahoo]],
					[cocacola2,				[pepsi,manaos,crush],							[ford],																			[pinterest,mitsubishi],				[motorola,facebook,whatsapp,america]],
					[farmacity,				[drahorro],												[havana,cruz,chevrolet],										[movistar,whatsapp],					[mcdonalds1,pepsi,audi,mitsubishi,burgerking]],
					[honda,						[chevrolet,volkswagen,ford,audi],	[havana,ferrum,twitter,pam,fila1],					[mario,disco,pinterest,claro],[whatsapp,addidas2,bic,ge]],
					[havana,					[jorgito,guaymallen,fantoche],		[honda,farmacity,cruz,sube],								[cat,shell,bic,pam,superman],	[twitter,nike,volkswagen,movistar,yahoo]],
					[superman,				[spiderman,batman,linterna],			[suzuki],																		[shell,mcdonalds],						[like,toilet,walmart,wordpress]],
					[unicenter,				[dot],														[sube],																			[movistar,android,whatsapp],	[ferrum,volkswagen,ital]]
					]
	random.shuffle(trials)

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					now = imagenes[0]
					sy = h
					sx = now[0].get_rect().w*h/now[0].get_rect().h
					imagenes.remove(now)
					target = pygame.transform.scale(now[0], (sx, sy))
					screen.fill((255,255,255))
					screen.blit(target, Rect(w/2-target.get_rect().w/2,0,1,1))
					pygame.display.update()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F8:
					sys.exit()
