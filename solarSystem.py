from re import S
import turtle
import math

from numpy import dtype

class SolarSystem:
    def __init__(self , width,height):
        self.__theSun = None
        self.__planets = []
        self.__moon = None
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.bgcolor("black")
        self.__ssScreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)

    def addMoon(self,Moon):
        self.__moon = Moon


    def addPlanets(self, aPlanet):
        self.__planets.append(aPlanet)
    
    def addSun(self,Sun):
        self.__theSun = Sun

    def showPlanets(self):
        for planet in self.__planets:
            print (planet)
    
    def freeze(self):
        self.__ssScreen.exitonclick()
    
    def movePlanets(self):
        G = 1
        dt = 0.01

        #planets_copy = self.__planets
        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getVelX()
                    ,p.getYPos() + dt * p.getVelY())
            
            rx =  self.__theSun.getXPos() - p.getXPos()
            ry = self.__theSun.getYPos() - p.getYPos()
            r =  math.sqrt(rx ** 2 + ry ** 2)

            accX = G * self.__theSun.getMass() * rx / r**3
            accY = G * self.__theSun.getMass() * ry / r**3

            '''for  otherP in planets_copy:
                if otherP.getName() != p.getName():
                    rx =  otherP.getXPos() - p.getXPos()
                    ry =  otherP.getYPos() - p.getYPos()
                    r =  math.sqrt(rx ** 2 + ry ** 2)

                    if r < 0.3:
                        accX += G * 0.3 *otherP.getMass() * rx /r **3
                        accY += G * 0.3 * otherP.getMass() * ry /r **3'''

            p.setVelX(p.getVelX() + dt * accX)
            p.setVelY(p.getVelY() + dt * accY)
        
    def moveMoon(self):
        dt = 0.01
        G = 1
        planets_copy = self.__planets

        for p in planets_copy:
            if p.getName() == 'Earth':
                self.__moon.moveTo(p.getXPos() + dt * p.getVelX()
                                  ,p.getYPos() + dt * p.getVelY())
                rx =  p.getXPos() - self.__moon.getXPos()
                ry =  p.getYPos() - self.__moon.getYPos()
                r =  math.sqrt(rx ** 2 + ry ** 2)

                accX = G * p.getMass() * rx / r**3
                accY = G * p.getMass() * ry / r**3   
        
        p.setVelX(p.getVelX() + dt * accX)
        p.setVelY(p.getVelY() + dt * accY)


            
    
    