__doc__ = "Client class that builds the application menus"

from Menu import Menu
from Actions import *
from BuildingManager import *
from ResourceManager import *
from Clock import Clock
import threading


Rm = ResourceManager()
Bm = BuildingManager(Rm)

Bm.add_available_building(Farm())

# Menus
main = Menu("Main Menu")
building = BuildMenu("Building", Bm, Rm)

main.addItem(building)

version = PrintVersionAction("Print Version")

main.addItem(version)


c = Clock(1)
c.add_worker(Bm)
c.start()

main.execute()

c.stop()


