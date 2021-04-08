import pygame
import math

class Movable:

    def __init__(self, x, y, dx, dy, width, height):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self. width = width
        self.height = height
        self.mActive = True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDX(self):
        return self.dx

    def getDY(self):
        return self.dy

    def getWorldWidth(self):
        return self.width

    def getWorldHeight(self):
        return self.height

    def move(self, dt):
        newx = self.x + dt * self.dx
        newy = self.y + dt * self.dy
        if newx < 0:
            newx += self.width
        if newy < 0:
            newy += self.height
        if newx >= self.width:
            newx -= self.width
        if newy >= self.height:
            newy -= self.height
        self.x = newx
        self.y = newy

    def getActive(self):
        return self.mActive

    def setActive(self, active):
        self.mActive = active
        return

    def hits(self, other):
        distance = math.sqrt((other.getX()-self.getX())**2 + (other.getY()-self.getY())**2)
        if distance <= (other.getRadius() + self.getRadius()):
            return True
        return False

    def getRadius(self):
        raise NotImplementedError
        return

    def accelerate(self, delta_velocity):
        raise NotImplementedError
        return

    def evolve(self, dt):
        raise NotImplementedError
        return

    def draw(self, surface):
        raise NotImplementedError
        return