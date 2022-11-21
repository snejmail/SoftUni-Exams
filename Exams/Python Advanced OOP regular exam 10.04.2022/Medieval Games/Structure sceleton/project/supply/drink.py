from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name):
        super(Drink, self).__init__(name, 15)

    def details(self):
        return f"{__class__.__name__}: {self.name}, {self.energy}"
