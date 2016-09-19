#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

	f = open("data.txt", 'r')

	obj = {'0':"CONCEPTO",'1':"LETRA/FORMA",'2':"COLOR",'3':"RUIDO"}
	trials = {}
	trials_c = {}
	users = []
	user = -1
	alls = {obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0}

	for l in f:
		if l.startswith("NEW USER"):
			user = user+1
			users.append({obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0})
		elif l[0] != '<':
			trial = l.split('|')
			if not trial[0] in trials:
				trials[trial[0]] = {obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0}
				trials_c[trial[0]] = {}
			if not trial[1]+"|"+trial[2] in trials_c[trial[0]]:
				trials_c[trial[0]][trial[1]+"|"+trial[2]] = 1
			else:
				trials_c[trial[0]][trial[1]+"|"+trial[2]] += 1
			trials[trial[0]][obj[trial[2]]] += 1
			trials[trial[0]]["TOTAL"] += 1
			users[user][obj[trial[2]]] += 1
			users[user]["TOTAL"] += 1
			alls[obj[trial[2]]] += 1
			alls["TOTAL"] += 1

#	for t in trials:
#		print t + ": " + str(trials[t])
#		print t + ": " + str(int((100.0 * float (trials[t][obj['0']]) / float (trials[t]["TOTAL"])))) + "%"
#		p = plt.bar((0,1,2,3),(trials[t][obj['0']],trials[t][obj['1']],trials[t][obj['2']],trials[t][obj['3']]),0.2)
#		plt.title(u'Desiciones globales en el trial ' + t)
#		plt.xticks((0,1,2,3),(obj["0"],obj["1"],obj["2"],obj["3"]))
#		plt.show()
	for t in trials_c:
#		print t + ": " + str(trials_c[t])
		highs = [0,0,0,0]
		colors = ['r','y','b','g']
		c = 0
		gs = []
		legends = []
		for h in trials_c[t]:
#			print str(h) + " " + str(trials_c[t][h])
			tp = h.split("|")[1]
			if (tp == '0'):
				legends.append(h.split("|")[0])
				gs.append(plt.bar((0,1,2,3), (trials_c[t][h],0,0,0),0.2,bottom=highs,color=colors[c]))
				highs[0] += trials_c[t][h]
			elif (tp == '1'):
				legends.append(h.split("|")[0])
				gs.append(plt.bar((0,1,2,3), (0,trials_c[t][h],0,0),0.2,bottom=highs,color=colors[c]))
				highs[1] += trials_c[t][h]
			elif (tp == '2'):
				legends.append(h.split("|")[0])
				gs.append(plt.bar((0,1,2,3), (0,0,trials_c[t][h],0),0.2,bottom=highs,color=colors[c]))
				highs[2] += trials_c[t][h]
			elif (tp == '3'):
				legends.append(h.split("|")[0])
				gs.append(plt.bar((0,1,2,3), (0,0,0,trials_c[t][h]),0.2,bottom=highs,color=colors[c]))
				highs[3] += trials_c[t][h]
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
