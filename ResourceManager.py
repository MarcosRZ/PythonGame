from Exceptions import *


class ResourceManager:

    def __init__(self, initialResources = 200):
        self.resources = initialResources

    def apply_cost(self, cost):
        if self.resources >= cost:
            self.resources -= cost
            #print ("Cost applied [{}] -> Resources: {}".format(cost, self.resources))
        else:
            raise NotEnoughResourcesException()

    def add_resources(self, resources):
        self.resources += resources
        #print ("Resources added [{}] -> Resources: {}".format(resources, self.resources))

