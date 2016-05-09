__doc__ = "This file defines a set of Actions corresponding to the leafs in Composite Pattern"
from Menu import Menu
from Exceptions import *
import copy
import DependencyInjector as DI
class BuildMenu(Menu):

    def __init__(self, label):

        Menu.__init__(self, label)
        for b in DI.get("buildingManager").availableBuildings:
            self.items.append(BuildAction(b))

class BuildAction:

    def __init__(self, building):
        self.building = building
        self.label = building.name

    def execute(self):
        try:
            DI.get("resourceManager").apply_cost(self.building.buildingCost)
            DI.get("buildingManager").add_building(copy.copy(self.building))
        except NotEnoughResourcesException:
            print("Not enough resources to build!")

class ShowResourcesAction:

    def __init__(self,):
        self.label = "Show Resources"

    def execute(self):
        print("Resources: {} units".format(DI.get("resourceManager").resources))

class ShowInfrastructureAction:

    def __init__(self):
        self.label = "Show Infrastructure"

    def execute(self):
        print("[")
        for b in DI.get("buildingManager").buildings:
            print(b.name + ",")
        print("]")
class PrintVersionAction:

    def __init__(self, label):
        self.label = label

    def execute(self):
        print("")
        print (">> Menu built with Composite Pattern. v1.0")
