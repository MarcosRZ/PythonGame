__doc__ = "Menu class that represents a MenuComponent. It has a list of items, that could be other MenuComponents, or Actions(leafs)"

class GenericMenuItem:

    def __init__(self, label = "No Label"):
        self.label = label

    def execute(self):
        pass

class Menu(GenericMenuItem):

    def __init__(self, label):
        GenericMenuItem.__init__(self, label)
        self.items = []
        self.items.append(GoBackAction())

    def execute(self):
        i = 0
        op = -1

        while op != 0:
            print("")
            print(self.label)
            print("---")
            for item in self.items:
                print("{} - {}".format(i, item.label))
                i += 1

            op = input("Select an option:")

            try:
                op = int(op)
                self.items[op].execute()
            except:
                print("")
                print ("@#|@~€#~ >> That wasn't a number, you bastard!")

            i = 0

    def addItem(self, item):
        self.items.append(item)


# This action is common for all menus. Good place to define it
class GoBackAction:

    def __init__(self, label = "Go back"):
        self.label = label

    def execute(self):
        pass
