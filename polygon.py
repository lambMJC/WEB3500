import rotatable
import pygame
import math


class Polygon(rotatable.Rotatable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.original_polygon = []
        self.color = (255, 255, 255)
        return

    def getPolygon(self):
        return self.original_polygon

    def getColor(self):
        return self.color

    def setPolygon(self, point_list):
        self.original_polygon = point_list

    def setColor(self, color):
        self.color = color
        return

    def draw(self, surface):
        pointlist = self.rotateAndTranslatePointList(self.original_polygon)
        pygame.draw.polygon(surface, self.color, pointlist, 1)
        return

    def getRadius(self):
        PointList = []
        dList = []
        for point in self.original_polygon:
            PointList.append(point)
        for point in PointList:
            distance = math.sqrt((point[0]-0)**2 + (point[1]-0)**2)
            dList.append(distance)
        if len(PointList) > 0:
            return (sum(dList))/len(dList)
        else:
            return 0