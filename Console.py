__doc__ = "Client class that builds the application menus"
import DependencyInjector as DI

from Actions import *
from BuildingManager import *
from ResourceManager import *
from Clock import Clock


Rm = ResourceManager()
Bm = BuildingManager()

# Timing engine
c = Clock(1)
c.add_worker(Bm)

# Enable dependency injector
DI.addDep("resourceManager", Rm)
DI.addDep("buildingManager", Bm)
DI.addDep("clock", c)

Bm.add_available_building(Farm())

# Menus
main = Menu("Main Menu")

# First Level Menus
building = BuildMenu("Building")
infrastructure = Menu("Infrastructure")
resources = Menu("Resources")
version = PrintVersionAction("Print Version")

# Infrastructure Menus
infrastructure.addItem(ShowInfrastructureAction())

# Resources Menus
resources.addItem(ShowResourcesAction())

main.addItem(building)
main.addItem(infrastructure)
main.addItem(resources)
main.addItem(version)





# GO!
c.start()

main.execute()

c.stop()


