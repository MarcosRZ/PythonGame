from Exceptions import *
import DependencyInjector as DI
class BuildingManager:

    def __init__(self):
        self.availableBuildings = []
        self.buildings = []

    def work(self):
        for b in self.buildings:
            try:
                # IoC FTW!! If not enough resources, exception is raised and harvest does not take place
                DI.get("resourceManager").apply_cost(b.work())
                b.harvest()
            except NotEnoughResourcesException:
                print("Not enough resources to work!")

    def collect(self):
        for b in self.buildings:
            # If we'd not enough resources to work, harvest is zero
            DI.get("resourceManager").add_resources(b.collect())

    def add_building(self, building):
        self.buildings.append(building)
        print ("A brand new {} was added to production chain!".format(building.name))

    def add_available_building(self, building):
        self.availableBuildings.append(building)
        print ("A brand new {} was added to available buildings!".format(building.name))

class Farm:

    def __init__(self):
        self.name = "Farm"
        self.buildingCost = 100
        self.productionCost = 10
        self.production = 50

        self.harvestAmount = 0

    def work(self):
        return self.productionCost

    def harvest(self):
        self.harvestAmount = self.production
        #print("Harvest for {}[{}] is {}".format(self.name, self, self.harvestAmount))
    # Tock returns the harvest made in the last tick
    def collect(self):
        self.r = self.harvestAmount
        self.harvestAmount = 0
        return self.r

