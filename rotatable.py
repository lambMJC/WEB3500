import movable
import math


class Rotatable(movable.Movable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.rotation = rotation

    def getRotation(self):
        return self.rotation

    def rotate(self, delta_rotation):
        self.rotation = (self.rotation + delta_rotation) % 360

    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        dx = math.cos(math.radians(rotation)) * delta_velocity
        dy = math.sin(math.radians(rotation)) * delta_velocity
        return dx, dy

    def accelerate(self, delta_velocity):
        dx, dy = self.splitDeltaVIntoXAndY(self.rotation, delta_velocity)
        self.dx += dx
        self.dy += dy

    def rotatePoint(self, x, y):
        angle = math.atan2(y, x)
        new_angle = angle + math.radians(self.rotation)
        d = math.sqrt(x**2 + y**2)
        newx = math.cos(new_angle) * d
        newy = math.sin(new_angle) * d
        return newx, newy

    def translatePoint(self, x, y):
        newx = x + self.x
        newy = y + self.y
        return newx, newy

    def rotateAndTranslatePoint(self, x, y):
        newx, newy = self.rotatePoint(x, y)
        newx, newy = self.translatePoint(newx, newy)
        return newx, newy

    def rotateAndTranslatePointList(self, points):
        newpoints = []
        for (x, y) in points:
            newpoint = self.rotateAndTranslatePoint(x, y)
            newpoints.append(newpoint)
        return newpoints