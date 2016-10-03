#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime
import numpy as np
import matplotlib.pyplot as plt

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
	#avg_users =


	for l in f:
		if l.startswith("NEW USER"):
		# Cambio de Usuario
			user = user+1
			users.append({obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0})
			temp_users.append([])
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

	colors = ['r','g','b','y','c','m','orangered','olive','indigo','lightcoral','lime','magenta','k']

	pTrials = False
	pTrials = True
	if (pTrials):
		for t in trials_c:
			highs = [0,0,0,0]
			c = 0
			gs = []
			legends = []
			for h in trials_c[t]:
				tp = trials_c[t][h][2]
				k = 1.0 * trials_c[t][h][1] / trials_c[t][h][0]
				if (tp == '0'):
					legends.append(h)
					gs.append(plt.bar((0,1,2,3), (k,0,0,0),0.2,bottom=highs,color=colors[c]))
					highs[0] += k
				elif (tp == '1'):
					legends.append(h)
					gs.append(plt.bar((0,1,2,3), (0,k,0,0),0.2,bottom=highs,color=colors[c]))
					highs[1] += k
				elif (tp == '2'):
					legends.append(h)
					gs.append(plt.bar((0,1,2,3), (0,0,k,0),0.2,bottom=highs,color=colors[c]))
					highs[2] += k
				elif (tp == '3'):
					legends.append(h)
					gs.append(plt.bar((0,1,2,3), (0,0,0,k),0.2,bottom=highs,color=colors[c]))
					highs[3] += k
				c = c+1
				if c >= len(colors):
					c = 0
			plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
			plt.title(u'Decisiones en el trial ' + t)
			plt.legend(gs,legends)
			plt.show()

	pTusers = False
	pTusers = True
	if (pTusers):
		for u in temp_users:
			if len(u) > 0:
				p = plt.plot(u,'-o')
				plt.title(u'Decisiones de un usuario en función del tiempo')
				plt.yticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
				plt.show()

	pUsers = False
	pUsers = True
	if (pUsers):
		c = 0
		for u in range(len(users)):
			if int (users[u]["TOTAL"]) > 0:
				p = plt.plot((0,1,2,3),(users[u][obj['0']],users[u][obj['1']],users[u][obj['2']],users[u][obj['3']]),colors[c])
				plt.title(u'Decisiones de los usuarios')
				plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
				c = c+1
				if c >= len(colors):
					c = 0
		plt.show()

	pGlobal = False
	pGlobal = True
	if (pGlobal):
		p = plt.bar((0,1,2,3),(alls[obj['0']],alls[obj['1']],alls[obj['2']],alls[obj['3']]),0.2)
		plt.title(u'Decisiones conjuntas de todos los trials y todos los usuarios')
		plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
		plt.show()

	gpRandom = open("random.data",'w')
	x = []
	y = []
	names = []
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
	z = "set xtics (\""
	for i in range(len(names)):
		z += names[i] + "\" " + str(i) + ", \""
	z += ")"
#	print z
