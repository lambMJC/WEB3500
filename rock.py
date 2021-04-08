import pygame
import math
import random
from polygon import Polygon

class Rock(Polygon):
    def __init__(self,x,y,world_width,world_height):
        self.mSpinRate = random.uniform(-90,90)
        Polygon.__init__(self,x,y,0,0,random.uniform(0, 359.9), world_width,world_height)
        Polygon.setPolygon(self,self.createRandomPolygon(30,6))
        randDX = random.randint(8, 14)
        randDY = random.randint(8, 14)
        fooX = random.randint(0, 1)
        fooY = random.randint(0, 1)

        if fooX == 0:
            randDX = -1*randDX
        if fooY == 0:
            randDX = -1*randDY
        self.dx = randDX
        self.dy = randDY
        return

    def createRandomPolygon(self, radius, number_of_points):
        points = []
        count = 1
        for num in range(number_of_points):
            newRadius = random.uniform(.7*radius, 1.3*radius)
            theta = math.radians(count*(360/number_of_points))
            x = newRadius * math.cos(theta)
            y = newRadius * math.sin(theta)
            points.append(tuple((x, y)))
            count += 1
        return points

    def getSpinRate(self):
        return self.mSpinRate

    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate
        return

    def evolve(self, dt):
        self.rotation = (self.getRotation( ) + self.getSpinRate( ) * dt ) % 360
        self.move(dt)
        return