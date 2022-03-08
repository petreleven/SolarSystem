from sun import Sun
from planetClass import Planet
from solarSystem import SolarSystem
from moon import Moon

def CreateSolarSystem():
    ss = SolarSystem(2,2)
    '''
    sun = Sun("Sun", 696340, 1,5000)
    venus = Planet('venus', 6051, 4.85e24, 0.2, 0.0, 0.1, 'orange')

    earth = Planet('Earth', 6371, 5.972e24, 0.3, 0.0, 0.1, 'blue')

    mars = Planet('Mars', 3390, 6.39e23, 0.4, 0.0, 0.1, 'red')

    saturn = Planet('Saturn',58232, 5.6683e26, 0.66, 0.0, 0.1, 'green')

    jupiter = Planet('Jupiter', 69911, 1.898e27, 0.7, 0.0, 0.1,'grey')
    '''
    sun = Sun("Sun", 20, 3, 5000)

    mercury = Planet('mercury', 20, 0.6, 0.2, 0.0, 3, 'green')
    venus = Planet('venus', 20, 0.6, 0.26, 0.0, 2, 'orange')
    moon = Moon("moon",10,10,0.7,0.0,0.4,"white")
    earth = Planet('Earth', 30, 1, 0.5, 0.0, 0.9, 'blue')
    jupiter = Planet('Jupiter', 70, 20, 0.8, 0.0, 0.7,'grey')
    planet9 = Planet('planet9', 70, 10, 1, 0.0, 0.7,'white')


    ss.addSun(sun)
    ss.addPlanets(mercury)
    ss.addPlanets(venus)
    ss.addPlanets(earth)
    ss.addPlanets(planet9)
    ss.addMoon(moon)
    #ss.addPlanets(mars)
    #ss.addPlanets(saturn)
    ss.addPlanets(jupiter)
    
    
    
    
    numofTimePeriods = 20000
    for period in range (numofTimePeriods):
        ss.movePlanets()
        #ss.moveMoon()
    
    ss.freeze()

CreateSolarSystem()