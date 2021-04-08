import pygame
import math
import random
import sched, time
from circle import Circle


class Star(Circle):

    def __init__(self, x, y, world_width, world_height):
        Circle.__init__(self, x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = random.randint(0, 255)
        self.mColor = (self.getBrightness(), self.getBrightness(), self.getBrightness())
        return

    def getBrightness(self):
        return self.mBrightness

    def setBrightness(self, brightness):
        if 0 <= brightness:
            if brightness <= 255:
                self.mBrightness = brightness
                self.mColor = (self.getBrightness(),
                               self.getBrightness(),
                               self.getBrightness())
        return

    def evolve(self, dt):
        randNum = random.randint(0, 2)
        if randNum == 0:
            if 0 <= self.mBrightness+10:
                if self.mBrightness+10 <= 255:
                    self.mBrightness += 10
        if randNum == 1:
            if 0 <= self.mBrightness-10:
                if self.mBrightness-10 <= 255:
                    self.mBrightness -= 10
        if randNum == 2:
            self.mBrightness = self.mBrightness
        self.mColor = (self.getBrightness(), self.getBrightness(), self.getBrightness())
        return