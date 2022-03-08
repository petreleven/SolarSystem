import math
import turtle

class Sun:
    def __init__(self,iName,iRad,iM,Temperature):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temperature = Temperature
        self.__x = 0
        self.__y = 0

        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")
    
    def __str__(self):
        return self.__name

    def setName(self,newName):
        self.__name = newName

    def getName(self):
        return self.__name
    
    def getRadius(self):
        return self.__radius
    
    def getMass(self):
        return self.__mass
    
    def getVolume(self):
        v = 4/3 * math.pi * self.__radius **3
        return  v
    
    def getSurfaceArea(self):
        sa = 4 * math.pi * self.__radius ** 2
        return sa
    
    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d
    
    def getTemperature(self):
        return self.__temperature
    
    def getXPos(self):
        return self.__x
    
    def getYPos(self):
        return self.__y

    