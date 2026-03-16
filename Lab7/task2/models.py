class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return "..."

    def get_info(self):
        return f"{self.name} is a {self.age} year old {self.species}."

    def __str__(self):
        return f"[{self.species}] {self.name}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}."

    def __str__(self):
        return f"[{self.species} - {self.breed}] {self.name}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def speak(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring loudly."

    def __str__(self):
        return f"[{self.species} - {self.color}] {self.name}"