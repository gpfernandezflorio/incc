#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime, matplotlib.pyplot
from PIL import Image
import numpy as np

if __name__ == '__main__':

	f = open("data.txt", 'r')

	obj = {'0':"CONCEPTO",'1':"LETRA/FORMA",'2':"COLOR",'3':"RUIDO"}
	trials = {}

	for l in f:
		if l[0] != '<':
			trial = l.split('|')
			if not trial[0] in trials:
				trials[trial[0]] = {obj['0']:0,obj['1']:0,obj['2']:0,obj['3']:0,"TOTAL":0}
			trials[trial[0]][obj[trial[2]]] += 1
			trials[trial[0]]["TOTAL"] += 1

	for t in trials:
		#print t + ": " + str(trials[t])
		print t + ": " + str(int((100.0 * float (trials[t][obj['0']]) / float (trials[t]["TOTAL"])))) + "%"
