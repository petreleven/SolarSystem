import turtle

class Moon:
    def __init__(self,iName,iRad,iM,iDist,ivelX, ivelY,color):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__x = self.__distance
        self.__y = 0
        self.__color = color

        self.__pTurtle = turtle.Turtle()
        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.pendown()

        self.__velx = ivelX
        self.__vely = ivelY

    
    def __str__(self):
        return self.__name
    
    def __lt__(self,OtherPlanet):
        return self.__distance < OtherPlanet.getDistance()

    def __gt__(self,OtherPlanet):
        return self.__distance > OtherPlanet.getDistance()

    def setName(self,newName):
        self.__name = newName

    def getName(self):
        return self.__name
    
    def getRadius(self):
        return self.__radius
    
    def getMass(self):
        return self.__mass
    
    def getDistance(self):
        return self.__distance
    
    def getVolume(self):
        import math
        v = 4/3 * math.pi * self.__radius **3
        return  v
    
    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius ** 2
        return sa
    
    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def getXPos(self):
        return self.__x
    
    def getYPos(self):
        return self.__y
    
    def moveTo(self,newX,newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x,self.__y)
    
    def getVelX(self):
        return self.__velx
    
    def getVelY(self):
        return self.__vely

    def setVelX(self,newVX):
        self.__velx = newVX
    
    def setVelY(self,newVY):
        self.__vely = newVY




