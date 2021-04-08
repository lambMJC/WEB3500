import pygame
import sys
import random
import movable, rotatable, polygon, ship, rock
import circle, bullet, star

class Asteroids:

    def __init__(self, world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mRocks = []
        self.mStars = []
        self.mBullets = []
        self.mObjects = []
        self.mShip = ship.Ship(world_width/2, world_height/2,
                               self.mWorldWidth,
                               self.mWorldHeight)
        for i in range(20):
            self.mStars.append(star.Star(random.randrange(0, 700), random.randrange(0, 700), self.mWorldWidth, self.mWorldHeight))
        for s in self.mStars:
            self.mObjects.append(s)

        for i in range(10):
            self.mRocks.append(rock.Rock(random.randrange(0,700), random.randrange(0,700), self.mWorldWidth, self.mWorldHeight))
        for r in self.mRocks:
            self.mObjects.append(r)

        self.mObjects.append(self.mShip)
        return

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getBullets(self):
        return self.mBullets

    def getStars(self):
        return self.mStars

    def getObjects(self):
        return self.mObjects

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
        return

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
        return

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
        return

    def fire(self):
        if self.mShip.getActive() == True:
            if len(self.mBullets) < 40 :
                b = self.mShip.fire()
                self.mBullets.append(b)
                self.mObjects.append(b)
        return

    def evolveAllObjects(self,dt):
        for obj in self.mObjects:
            if obj.mActive == True:
                obj.evolve(dt)
        return

    def collideShipAndBullets(self):
        for b in self.mBullets:
            if self.mShip.hits(b) == True:
                self.mShip.mActive = False
                b.mActive = False
                sys.exit("You were hit by a bullet!")
        return

    def collideShipAndRocks(self):
        for r in self.mRocks:
            if r.getActive() == True:
                if self.mShip.hits(r) == True:
                    self.mShip.mActive = False
                    sys.exit("HAHA, You were hit by an asteroid!")
        return

    def collideRocksAndBullets(self):
        for r in self.mRocks:
            if r.getActive() == True:
                for b in self.mBullets:
                    if b.hits(r) == True:
                        r.mActive = False
                        b.mActive = False
        return

    def removeInactiveObjects(self):
        for obj in self.mObjects:
            if obj.mActive == False:
                del self.mObjects[self.mObjects.index(obj)]
        for b in self.mBullets:
            if b.mActive == False:
                del self.mBullets[self.mBullets.index(b)]
        for r in self.mRocks:
            if r.mActive == False:
                del self.mRocks[self.mRocks.index(r)]
        return

    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.removeInactiveObjects()
        self.collideShipAndRocks()
        self.collideShipAndBullets()
        self.collideRocksAndBullets()
        if len(self.mRocks) == 0:
            sys.exit("You got lucky this time!")
        return

    def draw(self, surface):
        background = (0, 0, 0)
        surface.fill(background)
        for obj in self.mObjects:
            if obj.mActive == True:
                obj.draw(surface)
        return
