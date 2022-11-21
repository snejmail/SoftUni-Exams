from project.core.validator import Validator


class Player:
    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_number_is_below_12(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_if_number_is_not_in_range(value, self.min_stamina, self.max_stamina, "Stamina not valid!")
        self.__stamina = value

    @property
    def min_stamina(self):
        return 0

    @property
    def max_stamina(self):
        return 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
