#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ir: Índice de relación en un trial = 1/tiempo.
# Ir_uxc: Índice de relación de un usuario respecto a una de las cuatro clases = Sum Ir de los trials de ese usuario en los que eligió la clase c.
# Ir_cxt: Índice de relación de un choice respecto a un target = Sum Ir de los trials con el target t en los que se eligió el choice c.
# Ir_l1xl2: Índice de relación de un logo respecto a otro = Sum Ir de los trials con target l1 en los que se eligió a l2.

# Irr_uxc: Índice de relación reativa de un usuario respecto a una de las cuatro clases = Ir_uxc / cantidad de trials que el usuario eligió la clase c.
# Irr_cxt: Índice de relación reativa de un choice respecto a un target = Ir_cxt / cantidad de veces que apareció el choice c


# Ordenar el randoms por tamaño de globos.
# El de pTarget, hacerlo de dos dimensiones: En el eje y poner las 4 clases y en el eje z (color/tamaño) el índice NORMALIZADO.
# Definir índice normalizado.

import sys, math, random, datetime, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib._png import read_png

if __name__ == '__main__':

	f = open("trials.txt", 'r')

	obj = {'0':"CONCEPTO",'1':"LETRA/FORMA",'2':"COLOR",'3':"RUIDO",'4':"?"}
	trials_c = {}
	users = []
	temp_users = []
	user = -1
	alls = {obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0}
	randoms = {}
	rand_int = 0
	# TODO: agregar al último gráfico el promedio (y la varianza) de las elecciones de los usuarios.
	avg_users = [[],[],[],[]]


	for l in f:
		if l.startswith("NEW USER"):
		# Cambio de Usuario
			user = user+1
			users.append({obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0})
			temp_users.append([])
			avg_users[0].append(0)
			avg_users[1].append(0)
			avg_users[2].append(0)
			avg_users[3].append(0)
		elif l[0] == '>':
		# Random trial
			trial = l[1:].split('|')
			time = float(trial[5])
			if not trial[0] in randoms:
				randoms[trial[0]] = [rand_int,{}]
				rand_int += 1
			if not trial[1] in randoms[trial[0]][1]:
				randoms[trial[0]][1][trial[1]] = [1,1/time]
			else:
				randoms[trial[0]][1][trial[1]][0] += 1
				randoms[trial[0]][1][trial[1]][1] += 1/time
			for i in range(2,5):
				if not trial[i] in randoms[trial[0]][1]:
					randoms[trial[0]][1][trial[i]] = [1,0]
				else:
					randoms[trial[0]][1][trial[1]][0] += 1
		elif l[0] != '<':
		# Set trial
			trial = l.split('|')
			time = float(trial[6])
			if not trial[0] in trials_c:
				trials_c[trial[0]] = {}

			# Elegida:
			if not trial[1] in trials_c[trial[0]]:
				trials_c[trial[0]][trial[1]] = [1,1/time,trial[2]]
			else:
				# Le sumo 1 a cant apariciones
				trials_c[trial[0]][trial[1]][0] += 1
				# Le sumo 1 a cant elegida
				trials_c[trial[0]][trial[1]][1] += 1/time
				if trials_c[trial[0]][trial[1]][2] == '4':
					trials_c[trial[0]][trial[1]][2] = trial[2]

			# El resto
			for j in range(3,6):
				if not trial[j] in trials_c[trial[0]]:
					# Le sumo 1 a cant apariciones
					trials_c[trial[0]][trial[j]] = [1,0,'4']
				else:
					# Le sumo 1 a cant apariciones
					trials_c[trial[0]][trial[j]][0] += 1
			temp_users[user].append(trial[2])
			users[user][obj[trial[2]]] += 1/time
			users[user]["TOTAL"] += 1
			alls[obj[trial[2]]] += 1/time
			alls["TOTAL"] += 1
			avg_users[int(trial[2])][user] += 1/time
	colors = ['r','g','b','gold','c','purple','darkorange','darkblue','olive','mediumpurple','lightcoral','yellowgreen','saddlebrown','dodgerblue','lightpink','darkgrey','k']

	names = []
	ir = []

	pTrials = False
#	pTrials = True
	for t in trials_c:
		highs = [0,0,0,0]
		c = 0
		gs = []
		legends = []
		names.append(t)
		for h in trials_c[t]:
			tp = trials_c[t][h][2]
			# k = Ir_t de h / cant apariciones de h en t
			k = 1.0 * trials_c[t][h][1] / trials_c[t][h][0]
			if (tp == '0'):
				legends.append(h)
				if (pTrials):
					gs.append(plt.bar((-0.1,0.9,1.9,2.9), (k,0,0,0),0.2,bottom=highs,color=colors[c]))
				highs[0] += k
			elif (tp == '1'):
				legends.append(h)
				if (pTrials):
					gs.append(plt.bar((-0.1,0.9,1.9,2.9), (0,k,0,0),0.2,bottom=highs,color=colors[c]))
				highs[1] += k
			elif (tp == '2'):
				legends.append(h)
				if (pTrials):
					gs.append(plt.bar((-0.1,0.9,1.9,2.9), (0,0,k,0),0.2,bottom=highs,color=colors[c]))
				highs[2] += k
			elif (tp == '3'):
				legends.append(h)
				if (pTrials):
					gs.append(plt.bar((-0.1,0.9,1.9,2.9), (0,0,0,k),0.2,bottom=highs,color=colors[c]))
				highs[3] += k
			c = c+1
			if c >= len(colors):
				c = 0
		ir.append(highs[0])
		if (pTrials):
			plt.xticks((-0.5,0,1,2,3,3.5),("",obj["0"],obj["1"],obj["2"],obj["3"],""))
			plt.title(u'Índice de relación relativa por choice del target ' + t,fontsize=20)
			plt.ylabel(u'Índice de relación relativa',fontsize=20)
			plt.legend(gs,legends,bbox_to_anchor=(1.1, 1.05))
			plt.grid()
			plt.show()

	pTarget = False
	pTarget = True
	if (pTarget):
		plt.xticks(range(len(names)),names)
		plt.bar(range(len(names)),ir)
		plt.show()

	pTusers = False
#	pTusers = True
	c = 0
	if (pTusers):
		for u in temp_users:
			if len(u) > 0:
				plt.plot(u,'-o',color=colors[c])
				plt.yticks((-0.5,0,1,2,3,3.5),("",obj["0"],obj["1"],obj["2"],obj["3"],""))
				plt.title(u'Decisiones de un usuario en función del tiempo',fontsize=20)
				plt.xlabel(u'Número de trial',fontsize=20)
				plt.show()
				c = c+1
				if c >= len(colors):
					c = 0

	pUsers = False
#	pUsers = True
	if (pUsers):
		c = 0
		l = 1.0/(len(users)+10)
		for u in range(len(users)):
			if int (users[u]["TOTAL"]) > 0:
				#p = plt.plot((0+u*l,1+u*l,2+u*l,3+u*l),(users[u][obj['0']],users[u][obj['1']],users[u][obj['2']],users[u][obj['3']]),colors[c])
				p = plt.bar((0+u*l,1+u*l,2+u*l,3+u*l),(users[u][obj['0']],users[u][obj['1']],users[u][obj['2']],users[u][obj['3']]),width=l,color=colors[c])
				#p = plt.bar((0+u*l,1+u*l,2+u*l,3+u*l),(users[u][obj['0']]/users[u]["TOTAL"],users[u][obj['1']]/users[u]["TOTAL"],users[u][obj['2']]/users[u]["TOTAL"],users[u][obj['3']]/users[u]["TOTAL"]),width=l,color=colors[c])
				plt.title(u'Índice de relación de los usuarios por cada clase',fontsize=20)
				#plt.title(u'Índice de relación relativa de los usuarios por cada clase',fontsize=20)
				plt.ylabel(u'Índice de relación',fontsize=20)
				#plt.ylabel(u'Índice de relación relativa',fontsize=20)
				plt.xticks((0+l*len(users)/2,1+l*len(users)/2,2+l*len(users)/2,3+l*len(users)/2),(obj["0"],obj["1"],obj["2"],obj["3"]))
				c = c+1
				if c >= len(colors):
					c = 0
		plt.show()

	pGlobal = False
#	pGlobal = True
	if (pGlobal):
#		plt.bar((0,1,2,3),(alls[obj['0']],alls[obj['1']],alls[obj['2']],alls[obj['3']]),0.2)
#		plt.title(u'Decisiones conjuntas de todos los trials y todos los usuarios')
#		plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
#		plt.show()
		means = map(lambda x : np.mean(x), avg_users)
		yu = map(lambda x : np.mean(x) + 0.1, avg_users)
		yd = map(lambda x : np.mean(x) - 0.1, avg_users)
		plt.errorbar((0,1,2,3),means, yerr=[yu,yd], capthick=5, fmt=' r')
		plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
		plt.bar((0,1,2,3),means,0.2)
		plt.show()

	gpRandom = open("random.data",'w')
	x = []
	y = []
	names = []
	full = []
	for r in randoms:
		index = randoms[r][0]
		while len(names) <= index:
			names.append("?")
		names[index] = r
		for v in randoms[r][1]:
			if v in randoms:
				val = randoms[v][0]
				res = randoms[r][1][v][1] / randoms[r][1][v][0]
				gpRandom.write(str(val) + " " + str(index) + " " + str(res) + "\n")
				full.append([index,val,res])
	z = "set xtics (\""
	for i in range(len(names)):
		z += names[i] + "\" " + str(i) + ", \""
	z += ")"
#	print z
	full = sorted(full, key=lambda x : x[2])
	#for r in full:
	#	if (r[2] > 0):
	#		print names[r[0]] + " -> " + names[r[1]] + ": " + str(r[2])
