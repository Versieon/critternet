import sys
import random
import math
from graphics import *
from critter import critter
import gc
from pympler.tracker import SummaryTracker
			
gc.enable()
win = GraphWin("Net", 1000, 1000)
critterlist = []
names = 1
win.getMouse()
for i in range(0,10):
	critterlist.append(critter([],names))
	names += 1
	
advance = True
alltime = 0
check = 0
keystring = "d"
while advance:
	check += 1
	advance = False
	for animal in critterlist:
		if animal.alive:
			animal.calc()
			if keystring == "d":
				animal.draw(win)
				
			advance = True	
	if check == 100:
		check = 0
		best = 0
		second = 0
		deleted = 0
		temp = critterlist[0]
		for i in range(len(critterlist)):
			if critterlist[i].score > best:
				best = critterlist[i].score
				temp = critterlist[i]
#			elif critterlist[i].score > second:
#				second = critterlist[i].score
#				temp[1] = critterlist[i]
		if best > alltime:
			alltime = best
			print("	Best is: " + str(best))
			print(" Name is: " + str(temp.name))
			if keystring == "w":
				print("	Weights are: " + str(temp.weights))
				win.getMouse()
		critterlist = []
		temp.energy = 100
		temp.score = 0
		temp.pos = [500,500]
		temp.alive = True
		critterlist.append(temp)
		critterlist.append(temp.breed(temp,names))
		names += 1
		if len(critterlist) < 10:
			deleted = 10 - len(critterlist)
			for i in range(0,deleted):
				critterlist.append(temp.breed(temp, names))
				names += 1
		gc.collect()
		keystring = win.checkKey()
		if keystring == "q":
			break
win.close()    # Close window when done
