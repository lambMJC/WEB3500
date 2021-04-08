import pygame
import math
from polygon import *
from bullet import *


class Ship(Polygon):

    def __init__(self, x, y, world_width, world_height):
        Polygon.__init__(self, x, y, 0, 0, 0, world_width, world_height)
        Polygon.setPolygon(self, [[15, 0], [-10, 10], [-10, -10]])
        return

    def fire(self):
        point = self.rotateAndTranslatePoint(15, 0)
        self.mBullet = Bullet(point[0], point[1], self.dx, self.dy, self.rotation, self.width, self.height)
        return self.mBullet

    def evolve(self, dt):
        self.move(dt)
        return