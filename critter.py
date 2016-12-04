import sys
import random
import math
from graphics import *

mutationrate = 200
interlength = 6

class critter(object):
	def __init__(self, newweights = [], id = 0):
		self.best = False
		self.name = id		
		self.drawn = False
		self.alive = True
		self.energy = 2000
		self.score = 0
		self.color = [0,0,0]
		self.target = [300,700]
		self.pos = [500,500]
		self.dir = 0
		self.inputs = [0,0,0,0,1]
		self.outputs = [0,0,0,0,0]
		self.c = Circle(Point(self.pos[0], self.pos[1]), 5)
		if newweights:
			self.weights = newweights
		else:
			self.weights = []
			for i in range(0,(len(self.inputs)*interlength+interlength*interlength+interlength*len(self.outputs))):
				self.weights.append(random.uniform(-1,1))

	def calcinputs(self):
		self.inputs[0] = self.pos[0]		
		self.inputs[1] = self.pos[1]
		self.inputs[2] = self.outputs[0]
		self.inputs[3] = self.outputs[1]

	def calcpos(self):
		speed = math.fmod(self.outputs[0],3)
		distance = math.sqrt(math.pow((self.pos[0] - self.target[0]),2) + math.pow((self.pos[1] - self.target[1]),2))
		self.pos[0] += speed*math.cos(self.outputs[1])
		self.pos[1] += speed*math.sin(self.outputs[1])
		self.c.move(speed*math.cos(self.outputs[1]),speed*math.sin(self.outputs[1]))
		if distance < 10:
			self.energy -= 1
			self.score += 10*speed
		else:
			self.score += speed + min(100,1000/distance)
			self.energy -= 10
		if (self.pos[0] < 1) or (self.pos[0] > 999) or (self.pos[1] < 1) or (self.pos[1] > 999):
			self.energy = 0
		
	
	def calcoutputs(self):
		inter = [0] * interlength 
		inter2 = [0] * interlength		
		position = 0
		for i in range(len(inter)):
			for j in range(len(self.inputs)):
				inter[i] += self.inputs[j]*self.weights[position]
				position += 1

		for i in range(len(inter2)):
			for j in range(len(inter)):
				inter2[i] += inter[j]*self.weights[position]
				position += 1
	
		for i in range(len(self.outputs)):
			self.outputs[i] = 0
			for j in range(len(inter2)):
				self.outputs[i] += inter2[j]*self.weights[position]
				position += 1
		self.color[0] = self.outputs[2]%255
		self.color[1] = self.outputs[3]%255
		self.color[2] = self.outputs[4]%255
		self.c.setFill(color_rgb(self.color[0],self.color[1],self.color[2]))

	def calc(self):
		if (self.energy > 1):
			self.calcinputs()
			self.calcoutputs()
			self.calcpos()
		else:
			self.alive = False
		
	def breed(self, mate, name):
		new = []
		for i in range(len(self.weights)):
			new.append((self.weights[i] + mate.weights[i])/2)
		return critter(new, name)

	def draw(self, window):
		if not self.drawn:
			self.c.draw(window)
			self.drawn = True

	def clone(self, name):
		return critter(self.weights, name)

	def randclone(self, name):
		new = []
		pos = random.randint(0,len(self.weights))
		for i in range(len(self.weights)):
			if i == pos:
				new.append(self.weights[i]+random.uniform(-0.01,0.01))
			else:
				new.append(self.weights[i])
		return critter(new, name)


