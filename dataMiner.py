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
	user = -1
	alls = {obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0}
	randoms = {}
	rand_int = 0

	for l in f:
		if l.startswith("NEW USER"):
			user = user+1
			users.append({obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0})
		elif l[0] == '>':
			trial = l[1:].split('|')
			if not trial[0] in randoms:
				randoms[trial[0]] = [rand_int,{}]
				rand_int += 1
			if not trial[1] in randoms[trial[0]][1]:
				randoms[trial[0]][1][trial[1]] = 1
			else:
				randoms[trial[0]][1][trial[1]] += 1
		elif l[0] != '<':
			trial = l.split('|')
			if not trial[0] in trials_c:
				trials_c[trial[0]] = {}
			if not trial[1] in trials_c[trial[0]]:
				trials_c[trial[0]][trial[1]] = [1,1,trial[2]]
			else:
				trials_c[trial[0]][trial[1]][0] += 1
				trials_c[trial[0]][trial[1]][1] += 1
				if trials_c[trial[0]][trial[1]][2] == '4':
					trials_c[trial[0]][trial[1]][2] = trial[2]
			for j in range(3,6):
				if not trial[1] in trials_c[trial[0]]:
					trials_c[trial[0]][trial[1]] = [0,1,'4']
				else:
					trials_c[trial[0]][trial[1]][1] += 1
			users[user][obj[trial[2]]] += 1
			users[user]["TOTAL"] += 1
			alls[obj[trial[2]]] += 1
			alls["TOTAL"] += 1

	for t in trials_c:
		highs = [0,0,0,0]
		colors = ['r','g','b','y','c','m','orangered','olive','indigo','lightcoral','lime','magenta','k']
		c = 0
		gs = []
		legends = []
		for h in trials_c[t]:
			tp = trials_c[t][h][2]
#			k = trials_c[t][h][0]
			k = 1.0 * trials_c[t][h][0] / trials_c[t][h][1]
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
		plt.title(u'Desiciones en el trial ' + t)
		plt.legend(gs,legends)
		plt.show()
	print "------------------------------------------------"
	for u in range(len(users)):
		if int (users[u]["TOTAL"]) > 0:
#			print "User " + str(u) + ": " + str(users[u])
			print "User " + str(u) + ": " + str(int((100.0 * float (users[u][obj['0']]) / float (users[u]["TOTAL"])))) + "%"
			p = plt.bar((0,1,2,3),(users[u][obj['0']],users[u][obj['1']],users[u][obj['2']],users[u][obj['3']]),0.2)
			plt.title(u'Desiciones del usuario ' + str(u))
			plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
			plt.show()
	print "------------------------------------------------"
#	print "ALL: " + str(alls)
	print "ALL: " + str(int((100.0 * float (alls[obj['0']]) / float (alls["TOTAL"])))) + "%"
	p = plt.bar((0,1,2,3),(alls[obj['0']],alls[obj['1']],alls[obj['2']],alls[obj['3']]),0.2)
	plt.title(u'Desciciones conjuntas de todos los trials y todos los usuarios')
	plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
	plt.show()

#	print str(randoms)

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
				for i in range(randoms[r][1][v]):
					y.append(index)
					x.append(val)
	plt.xticks(range(len(names)),names,rotation=90)
	plt.yticks(range(len(names)),names[::-1])
	plt.grid(True)
	plt.hist2d(x, y, bins=len(names))
	plt.show()
