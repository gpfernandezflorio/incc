#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ir: Índice de relación en un trial = 1/tiempo.
# Ir_uxc: Índice de relación de un usuario respecto a una de las cuatro clases = Sum Ir de los trials de ese usuario en los que eligió la clase c.
# Ir_cxt: Índice de relación de un choice respecto a un target = Sum Ir de los trials con el target t en los que se eligió el choice c.
# Ir_l1xl2: Índice de relación de un logo respecto a otro = Sum Ir de los trials con target l1 en los que se eligió a l2.

# Irr_uxc: Índice de relación reativa de un usuario respecto a una de las cuatro clases = Ir_uxc / cantidad de trials que el usuario eligió la clase c.
# Irr_cxt: Índice de relación reativa de un choice respecto a un target = Ir_cxt / cantidad de veces que apareció el choice c

# El de pTarget, hacerlo de dos dimensiones: En el eje y poner las 4 clases y en el eje z (color/tamaño) el índice NORMALIZADO.
# Definir índice normalizado.

import sys, math, random, datetime, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib._png import read_png

def maximox(dic):
	iMax = [0,0]
	for i in dic:
		if dic[i][1] / dic[i][0] > iMax[1]:
			iMax = [i,dic[i][1] / dic[i][0]]
	return iMax[1]

def maximoy(l):
	greatsort = map(lambda x : [x[0],0,x[1][0]], l)
	for i in l:
		for j in i[1][1]:
			x = i[1][1][j][1] / i[1][1][j][0]
			for h in greatsort:
				if h[0] == j:
					if x > h[1]:
						h[1] = x
	greatsort = sorted(greatsort, key=lambda x : x[1])
	ysort = range(len(greatsort))
	for i in range(len(greatsort)):
		ysort[greatsort[i][2]] = i
	return ysort

if __name__ == '__main__':

	f = open("trials.txt", 'r')

	obj = {'0':"CONCEPTO",'1':"LETRA/FORMA",'2':"COLOR",'3':"RUIDO",'4':"?"}
	apariciones_trials = {}
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
			if (user != -1 and users[user]["TOTAL"]!=0):
				avg_users[0][user] /= users[user]["TOTAL"]
				avg_users[1][user] /= users[user]["TOTAL"]
				avg_users[2][user] /= users[user]["TOTAL"]
				avg_users[3][user] /= users[user]["TOTAL"]
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
			if not trial[0] in apariciones_trials:
				apariciones_trials[trial[0]] = 0
			else:
				apariciones_trials[trial[0]] += 1
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
	ir = [[],[],[],[]]

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
		#ir[0].append(highs[0])
		#ir[1].append(highs[1])
		#ir[2].append(highs[2])
		#ir[3].append(highs[3])
		ir[0].append(highs[0]/apariciones_trials[t])
		ir[1].append(highs[1]/apariciones_trials[t])
		ir[2].append(highs[2]/apariciones_trials[t])
		ir[3].append(highs[3]/apariciones_trials[t])
		if (pTrials):
			plt.xticks((-0.5,0,1,2,3,3.5),("",obj["0"],obj["1"],obj["2"],obj["3"],""))
			plt.title(u'Índice de relación relativa por choice del target ' + t,fontsize=20)
			plt.ylabel(u'Índice de relación relativa',fontsize=20)
			plt.legend(gs,legends,bbox_to_anchor=(1.1, 1.05))
			plt.grid()
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
	pUsers = True
	if (pUsers):
		c = 0
		l = 1.0/(len(users)+8)
		center = l*len(users)/2
		for u in range(len(users)):
			if int (users[u]["TOTAL"]) > 0:
				#p = plt.bar((1.2+u*l,2.2+u*l,3.2+u*l,4.2+u*l),(users[u][obj['0']],users[u][obj['1']],users[u][obj['2']],users[u][obj['3']]),width=l,color=colors[c])
				p = plt.bar((1.2+u*l,2.2+u*l,3.2+u*l,4.2+u*l),(users[u][obj['0']]/users[u]["TOTAL"],users[u][obj['1']]/users[u]["TOTAL"],users[u][obj['2']]/users[u]["TOTAL"],users[u][obj['3']]/users[u]["TOTAL"]),width=l,color=colors[c])
				#plt.title(u'Índice de relación de los usuarios por cada clase',fontsize=40)
				plt.title(u'Índice de relación relativa de los usuarios por cada clase',fontsize=40)
				#plt.ylabel(u'Índice de relación',fontsize=40)
				plt.ylabel(u'Índice de relación relativa',fontsize=40)
				c = c+1
				if c >= len(colors):
					c = 0

		#plt.ylim(-0.1, 60)
		plt.ylim(-0.002, 0.75)
		plt.xticks((),(obj["0"],obj["1"],obj["2"],obj["3"],""),fontsize=20)
		plt.axvline(x=1.85, ymin=-0.1, ymax = 60, linewidth=1, color='k')
		plt.axvline(x=2.85, ymin=-0.1, ymax = 60, linewidth=1, color='k')
		plt.axvline(x=3.85, ymin=-0.1, ymax = 60, linewidth=1, color='k')
		avg_users.append([0])
		plt.boxplot(avg_users,widths=(0.23,0.23,0.23,0.23,0))
		plt.show()

	pTarget = False
#	pTarget = True
	greatsort = []
	for i in range(len(names)):
		greatsort.append([names[i],ir[0][i],i])
	greatsort = sorted(greatsort, key=lambda x : x[1])
	xsort = range(len(names))
	for i in range(len(greatsort)):
		xsort[greatsort[i][2]] = i
	M = len(xsort)
	xsort = map(lambda x : M-x, xsort)
	if (pTarget):
		gpTarget = open("target.data",'w')
		z = "set xtics (\""
		for i in range(len(ir[0])):
			gpTarget.write(str(xsort[i]) + " " + str(0) + " " + str(ir[0][i]) + "\n")
			gpTarget.write(str(xsort[i]) + " " + str(1) + " " + str(ir[1][i]) + "\n")
			gpTarget.write(str(xsort[i]) + " " + str(2) + " " + str(ir[2][i]) + "\n")
			gpTarget.write(str(xsort[i]) + " " + str(3) + " " + str(ir[3][i]) + "\n")
			z += names[i] + "\" " + str(xsort[i]) + ", \""
		gpTarget.close()
		z += ") rotate by -45"
		print z

	#RANDOMS:
	list_random = []
	for i in randoms.keys():
		list_random.append([i,randoms[i]])
	great_sortx = sorted(map(lambda x : [x[0],maximox(x[1][1]),x[1][0]], list_random), key=lambda x : x[1])
	xsort = range(len(great_sortx))
	for i in range(len(great_sortx)):
		xsort[great_sortx[i][2]] = i
	ysort = maximoy(list_random)
	M = len(xsort)
	xsort = map(lambda x : M-x, xsort)
	M = len(ysort)
	ysort = map(lambda x : M-x, ysort)

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
				gpRandom.write(str(ysort[val]) + " " + str(xsort[index]) + " " + str(res) + "\n")
				full.append([index,val,res])
	z = "set ytics (\""
	for i in range(len(names)):
		z += names[i] + "\" " + str(xsort[i]) + ", \""
	z += ")"
#	print z
	z = "set xtics (\""
	for i in range(len(names)):
		z += names[i] + "\" " + str(ysort[i]) + ", \""
	z += ") rotate by -45"
#	print z
	full = sorted(full, key=lambda x : x[2])
#	for r in full:
#		if (r[2] > 0):
#			print names[r[0]] + " -> " + names[r[1]] + ": " + str(r[2])
