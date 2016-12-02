import sys
import random
import math
from graphics import *

mutationrate = 50
interlength = 6

class critter(object):
	def __init__(self, newweights = [], id = 0):
		self.name = id		
		self.alive = True
		self.energy = 100
		self.score = 0
		self.color = [0,0,0]
		self.startpos = [500,500]
		self.pos = [500,500]
		self.dir = 0
		self.inputs = [0,0,0,0,1]
		self.outputs = [0,0,0,0,0]
		if newweights:
			self.weights = newweights
		else:
			self.weights = []
			for i in range(0,(len(self.inputs)*interlength+interlength*len(self.outputs))):
				self.weights.append(random.uniform(-1,1))

	def calcinputs(self):
		self.inputs[0] = self.pos[0]		
		self.inputs[1] = self.pos[1]
		self.inputs[2] = self.outputs[0]
		self.inputs[3] = self.outputs[1]

	def calcpos(self):
		self.pos[0] += (self.outputs[0]%5)*math.cos(self.outputs[1])
		self.pos[1] += (self.outputs[0]%5)*math.sin(self.outputs[1])
		self.score += self.outputs[0]%5 + 100/math.sqrt(math.pow((self.pos[0] - 700),2) + math.pow((self.pos[1] - 800),2))
		self.energy -= 1
		if (self.pos[0] < 1) or (self.pos[0] > 999) or (self.pos[1] < 1) or (self.pos[1] > 999):
			self.energy = 0

	def calcoutputs(self):
		inter = [0] * interlength 
		position = 0
		for i in range(len(inter)):
			for j in range(len(self.inputs)):
				inter[i] += self.inputs[j]*self.weights[position]
				position += 1
	
		for i in range(len(self.outputs)):
			self.outputs[i] = 0
			for j in range(len(inter)):
				self.outputs[i] += inter[j]*self.weights[position]
				position += 1
		self.color[0] = self.outputs[2]%255
		self.color[1] = self.outputs[3]%255
		self.color[2] = self.outputs[4]%255

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
			if random.randrange(0,mutationrate) == 0:
				new[i] += random.uniform(-1,1)
		return critter(new, name)

	def draw(self, window):
		c = Circle(Point(self.pos[0], self.pos[1]), 5)
		c.setFill(color_rgb(self.color[0],self.color[1],self.color[2]))
		c.draw(window)

