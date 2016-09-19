#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime, matplotlib.pyplot
from pygame.locals import *
from PIL import Image
import numpy as np

tiempo_pre_target = 10
tiempo_target = 50
tiempo_pos_target = 10

global_timer = 10 * 60 * 100

if __name__ == '__main__':

	pygame.init()

	infoObject = pygame.display.Info()
	w = infoObject.current_w
	h = infoObject.current_h

	f = open("data.txt", 'a')
	d = datetime.datetime.now()
	f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + ">\n")
	f.write("NEW USER\n")

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
	wordpress = [pygame.image.load("img/wordpress.png").convert_alpha(),"word press"]
	chevrolet = [pygame.image.load("img/chevrolet.png").convert_alpha(),"chevrolet"]
	mitsubishi = [pygame.image.load("img/mitsubishi.png").convert_alpha(),"mitsubishi"]
	google = [pygame.image.load("img/googlePlus.png").convert_alpha(),"google"]
	pinterest = [pygame.image.load("img/pinterest.png").convert_alpha(),"pinterest"]
	puma = [pygame.image.load("img/puma logo.gif").convert_alpha(),"puma"]
	ital = [pygame.image.load("img/italMexicana.png").convert_alpha(),"ital"]
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

	trials = []
	show = []
	#positions = [[x, y] for x in range(5) for y in range(3)]
	positions = [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3]]
	target = 0
	now = -1
	others = []

	estado = 0
	timer = 0
	g_timer = global_timer
	font = pygame.font.SysFont("digital", w/10, True)

	time_left = ""

	trials = [									#CONCEPTO																			#LETRA																			#COLOR																	#RUIDO
					[movistar,				[claro],													[mcdonalds,motorola,mario],									[farmacity,sube],						[pepsi,bic,burgerking,carrefour,ge,mitsubishi,pam]],
					[claro,						[movistar],												[whatsapp,motorola,wordpress],							[firestone, honda,mitsubishi],[fila1,chevrolet,pam,addidas,farmacity,toilet]],
					[mcdonalds1,			[pizzahut1,burgerking],						[movistar,motorola,mario],									[pam,cat,bic],							[addidas2,nike,fila,twitter,volkswagen,farmacity]],
					[cocacola,				[manaos,crush,fanta],							[motorola,whatsapp,volkswagen,wordpress],		[honda,mitsubishi,firestone],[addidas2,walmart,bic,sube,facebook,toilet]],
					[volkswagen,			[chevrolet,mitsubishi,honda,ford],[v,cocacola,disco,wordpress,whatsapp],			[addidas2,twitter,ferrum,carrefour],[superman,android,unicenter,havana,fanta]],
					[facebook,				[whatsapp,google,pinterest],			[fila1,firestone],													[motorola,addidas2,volkswagen],[bic,crush,pam,superman,honda,mitsubishi]],
					[addidas,					[fila,nike,puma],									[ital,wm],																	[toilet,wordpress,v,puma],			[apple2,android,superman,crush,firestone,disco]],
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
					show.append([[pos[1],pos[0]],i[1],i[2]])
					screen.blit(i[0], (pos[1]*w/5,pos[0]*h/3))
					x = x + w/5
					positions.remove(pos)
					positions.append(pos)
				random.shuffle(positions)
				estado = 4
		elif estado==4:
			screen.fill((255,255,255),(w*2/5,h*1/3,w/5,h/3))
			hour = 0
			mint = 0
			sec = g_timer/100
			if sec >= 60:
				mint = sec / 60
				sec = sec % 60
			if mint >= 60:
				hour = mint / 60
				mint = mint % 60
			if hour < 10:
				hour = "0"+str(hour)
			if sec < 10:
				sec = "0"+str(sec)
			if mint < 10:
				mint = "0"+str(mint)
			new_time = str(hour) + ":" + str(mint) + ":" + str(sec)
			if new_time != time_left:
				label = pygame.transform.scale(font.render(new_time, True, (0,0,0)),(w/6,h/3))
				screen.blit(label, (w/2-label.get_rect().w/2,h/2-label.get_rect().h/2))
				pygame.display.update()
				time_left = new_time
			#TODO: ver que pasa si llega a cero.

		timer = timer-1
		g_timer = g_timer-10
		pygame.time.wait(10)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					done = False
					x = -1
					y = -1
					if estado==0:
						g_timer = global_timer
						done = True
					elif estado==4:
						pos = pygame.mouse.get_pos()
						x = pos[0]*5/w
						y = pos[1]*3/h
						for i in show:
							if (i[0][0]==x and i[0][1]==y):
								f.write(str(now[1]) + "|" + i[1] + "|" + str(i[2]))
								for j in show:
									if i != j:
										f.write("|" + j[1])
								f.write("|"+time_left+"\n")
								done = True
								positions.remove([y,x])
								break
					if (done):
						show = []
						random.shuffle(positions)
						if (x>=0 and y>=0):
							positions.append([y,x])
						trial = trials[0]
						trials.remove(trial)
						trials.append(trial)
						now = trial[0]
						sy = h
						sx = now[0].get_rect().w*h/now[0].get_rect().h
						target = pygame.transform.scale(now[0], (sx, sy))
						others = []
						for i in range(4):
							t = random.choice(trial[i+1])
							if t[0].get_rect().w > t[0].get_rect().h:
								sx = w/5
								sy = t[0].get_rect().h*w/5/t[0].get_rect().w
								others.append([pygame.transform.scale(t[0], (sx, sy)),t[1],i])
							else:
								sy = h/3
								sx = t[0].get_rect().w*h/3/t[0].get_rect().h
								others.append([pygame.transform.scale(t[0], (sx, sy)),t[1],i])
						timer = 1
						estado = 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F8:
					f.close()
					sys.exit()
				elif event.key == pygame.K_F5:
					f.write("NEW USER\n")
					screen.fill((0,0,0))
					pygame.display.update()
					estado = 0
