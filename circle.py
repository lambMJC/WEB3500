import pygame
import math
from rotatable import Rotatable

class Circle(Rotatable):
    def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
        Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)
        return

    def getRadius(self):
        return self.mRadius

    def getColor(self):
        return self.mColor

    def setRadius(self, radius):
        if radius >= 1:
            self.mRadius = radius
        else:
            return
        return

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):
        XY = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.mColor, XY, self.mRadius, 0)
        return
