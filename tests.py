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
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison


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
	avg_users_quantity = [[],[],[],[]]
	avg_users_time = [[],[],[],[]]


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

			avg_users_quantity[0].append(0)
			avg_users_quantity[1].append(0)
			avg_users_quantity[2].append(0)
			avg_users_quantity[3].append(0)


			avg_users_time[0].append(0)
			avg_users_time[1].append(0)
			avg_users_time[2].append(0)
			avg_users_time[3].append(0)

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
			avg_users_quantity[int(trial[2])][user] += 1
			avg_users_time[int(trial[2])][user] += time


	colors = ['r','g','b','gold','c','purple','darkorange','darkblue','olive','mediumpurple','lightcoral','yellowgreen','saddlebrown','dodgerblue','lightpink','darkgrey','k']




#	F, p = stats.f_oneway(avg_users_time[0],avg_users_time[1], avg_users_time[2], avg_users_time[3])
#	print "Relativo tiempo"
#	print p


#	F, p = stats.f_oneway(avg_users[0],avg_users[1], avg_users[2], avg_users[3])
#	print "Anova RI"
#	print p


	F, p = stats.f_oneway(avg_users_quantity[0],avg_users_quantity[1], avg_users_quantity[2], avg_users_quantity[3])
	print "Anova Cantidad de elecciones de un usuario por clase"
	print p


	print("-------------------------------------------------------------------------")
	print("*************************************************************************")
	print("-------------------------------------------------------------------------")


	arrayAux1  = np.concatenate((np.array(avg_users_quantity[0]), np.array(avg_users_quantity[1])), axis=0)
	arrayAux2  = np.concatenate((np.array(avg_users_quantity[2]), np.array(avg_users_quantity[3])), axis=0)
	arrayTotal  = np.concatenate((arrayAux1, arrayAux2), axis=0)


	arr1 = np.array(map(lambda x: "concepto", range(len(avg_users_quantity[0]))))
	arr2 = np.array(map(lambda x: "letra/forma", range(len(avg_users_quantity[1]))))
	arr3 = np.array(map(lambda x: "color", range(len(avg_users_quantity[2]))))
	arr4 = np.array(map(lambda x: "ruido", range(len(avg_users_quantity[3]))))

	arrAux1  = np.concatenate((arr1, arr2), axis=0)
	arrAux2  = np.concatenate((arr3, arr4), axis=0)
	arrTotal  = np.concatenate((arrAux1, arrAux2), axis=0)


	mc = MultiComparison(arrayTotal, arrTotal)
	result = mc.tukeyhsd()

	print(result)
	print(mc.groupsunique)
	print("-------------------------------------------------------------------------")
	print("*************************************************************************")
	print("-------------------------------------------------------------------------")




	avg_users_jugadas = map(lambda x: users[x]["TOTAL"], range(len(users)))

	avg_users_relativos0 = map(lambda x: avg_users[0][x]/avg_users_jugadas[x], range(len(users)))
	avg_users_relativos1 = map(lambda x: avg_users[1][x]/avg_users_jugadas[x], range(len(users)))
	avg_users_relativos2 = map(lambda x: avg_users[2][x]/avg_users_jugadas[x], range(len(users)))
	avg_users_relativos3 = map(lambda x: avg_users[3][x]/avg_users_jugadas[x], range(len(users)))

	arrayAux0  = np.concatenate((np.array(avg_users_relativos0), np.array(avg_users_relativos1)), axis=0)
	arrayAux1  = np.concatenate((np.array(avg_users_relativos2), np.array(avg_users_relativos3)), axis=0)
	arrayTotal  = np.concatenate((arrayAux0, arrayAux1), axis=0)


	mc = MultiComparison(arrayTotal, arrTotal)
	result = mc.tukeyhsd()

	F, p = stats.f_oneway(avg_users_relativos0,avg_users_relativos1, avg_users_relativos2, avg_users_relativos3)
	print "Anova Cantidad de elecciones de un usuario por clase / cantidad de jugadas del usuario"
	print p


	print(result)
	print(mc.groupsunique)

 
	#chi2, p, dof, expected = stats.chi2_contingency(np.array([avg_users_relativos0, avg_users_relativos1, avg_users_relativos2, avg_users_relativos3]))
	#print p
	#normalizamos la distribucion tomando logaritmo del tiempo
	
