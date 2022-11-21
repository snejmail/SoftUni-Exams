from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, energy=25):
        super(Food, self).__init__(name, energy)

    def details(self):
        return f"{__class__.__name__}: {self.name}, {self.energy}"
