from sun import Sun
from planetClass import Planet
from solarSystem import SolarSystem
from moon import Moon

def CreateSolarSystem():
    ss = SolarSystem(2,2)
    
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
