__doc__ = "This file defines a set of Actions corresponding to the leafs in Composite Pattern"
from Menu import Menu
from Exceptions import *
import copy
class BuildMenu(Menu):

    def __init__(self, label, buildingManager, resourceManager):

        Menu.__init__(self, label)

        self.buildingManager = buildingManager
        self.resourceManager = resourceManager

        for b in buildingManager.availableBuildings:
            self.items.append(BuildAction(b, buildingManager, resourceManager))

class BuildAction:

    def __init__(self, building, buildingManager,resourceManager):

        self.building = building
        self.label = building.name
        self.resourceManager = resourceManager
        self.buildingManager = buildingManager

    def execute(self):
        try:
            self.resourceManager.apply_cost(self.building.buildingCost)
            self.buildingManager.add_building(copy.copy(self.building))
        except NotEnoughResourcesException:
            print("Not enough resources to build!")

class PrintVersionAction:

    def __init__(self, label):
        self.label = label

    def execute(self):
        print("")
        print (">> Menu built with Composite Pattern. v1.0")