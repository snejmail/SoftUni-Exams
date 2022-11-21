from project.supply.drink import Drink
from project.supply.food import Food


class SustenanceFactory:
    sustenance_types = {
        'Food': Food,
        'Drink': Drink
    }

    def create_sustenance(self, sustenance_type,):
        if sustenance_type in self.sustenance_types:
            return self.sustenance_types[sustenance_type]

