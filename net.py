import sys
import random
import math
from graphics import *
from critter import critter
import time
import gc

gc.enable()
win = GraphWin("Net", 1000, 1000, autoflush=False)
critterlist = []
names = 1
win.getMouse()
for i in range(0,20):
	critterlist.append(critter([],names))
	names += 1
advance = True
alltime = 0
keystring = "d"
c = Circle(Point(300, 700), 10)
c.setFill("red")
c.draw(win)
while advance:
	advance = False
	for animal in critterlist:
		if keystring == "d" and animal.best:
			animal.draw(win)
			time.sleep(0.001)
		elif (keystring == "a"):
			animal.draw(win)
		if animal.alive:
			animal.calc()
			update(60)
			advance = True
	if not advance:
		advance = True
		best = 0
		second = 0
		deleted = 0
		temp = critterlist[0]
		temp2 = critterlist[0]
		for i in range(len(critterlist)):
			if critterlist[i].score > best:
				best = critterlist[i].score
				temp = critterlist[i]
			elif critterlist[i].score > second:
				second = critterlist[i].score
				temp2 = critterlist[i]
		if best > alltime:
			alltime = best
			print("	Best is: " + str(best))
			print(" Name is: " + str(temp.name))
			if keystring == "w":
				print("	Weights are: " + str(temp.weights))
				win.getMouse()
		critterlist = []
		critterlist.append(temp.clone(names))
		critterlist[0].best = True
		names += 1
		critterlist.append(temp.breed(temp2,names))
		names += 1
		for i in range(0,18):
			critterlist.append(temp.randclone(names))
			names += 1

		gc.collect()
		keystring = win.checkKey()
		if keystring == "q":
			break
win.close()    # Close window when done
