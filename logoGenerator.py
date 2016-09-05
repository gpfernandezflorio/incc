#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, random, pygame, datetime, matplotlib.pyplot
from pygame.locals import *
from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
	
	files = [f for f in listdir("./img/") if isfile(join("./img/", f))]
	for f in files:
		names = str(f).split(".")
		im = Image.open("./img/" + str(f))	
		if (names[1]=="jpg"):
			r, g, b = im.split()
			a = np.zeros_like(b)
			a[b < 100] = 255
			new_im = Image.fromarray(np.dstack([item for item in (b,r,g,a)]))
			new_im.save("./img/new/" + names[0] + "-c1." + names[1])
			new_im = Image.fromarray(np.dstack([item for item in (g,b,r,a)]))
			new_im.save("./img/new/" + names[0] + "-c2." + names[1])
			new_im = Image.fromarray(np.dstack([item for item in (r,b,g,a)]))
			new_im.save("./img/new/" + names[0] + "-c3." + names[1])
			new_im = Image.fromarray(np.dstack([item for item in (b,g,r,a)]))
			new_im.save("./img/new/" + names[0] + "-c4." + names[1])
			new_im = Image.fromarray(np.dstack([item for item in (g,r,b,a)]))
			new_im.save("./img/new/" + names[0] + "-c5." + names[1])
