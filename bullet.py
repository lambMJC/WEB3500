import pygame
import math
import time
from circle import Circle

class Bullet(Circle):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        Newdx = dx + 100. * math.cos(math.radians(rotation))
        Newdy = dy + 100. * math.sin(math.radians(rotation))
        Circle.__init__(self, x + 0.1 * Newdx, y + 0.1 * Newdy, Newdx, Newdy, rotation, 3, world_width, world_height)
        self.mAge = 0
        return

    def getAge(self):
        return self.mAge

    def setAge(self, age):
        if age > 0:
            if age < 6:
                self.mAge = age
        return

    def evolve(self, dt):
        self.move(dt)
        if self.mAge <= 6:
            self.mAge += dt
            self.mActive = True
        if self.mAge > 6:
            self.mAge = dt
            self.mActive = False
        return
