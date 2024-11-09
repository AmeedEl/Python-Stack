class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.health += 10
        self.happiness += 10

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 100, 100)

    def feed(self):
        self.health += 20
        self.happiness += 5
        print(f"{self.name} The lion has been fed! Health and happiness is updated.")

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a fierce lion!!")


class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 80, 90)

    def feed(self):
        self.health += 15
        self.happiness += 15
        print(f"{self.name} the monkey has been fed!")

    def display_info(self):
        super().display_info()
        print(f"{self.name} loves to swing around!!")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 120, 80)

    def feed(self):
        self.health += 10
        self.health += 20 
        print(f"{self.name} the bear has been fed!")

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a gentle giant!!")


class Zoo: 
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.zoo_name, "-" * 30)
        for animal in self.animals:
            animal.display_info()
            print("-" * 60)


the_zoo = Zoo("The ZOO is ZOOING!!!")

lion = Lion("Simba", 10)
babylion = Lion("Laith", 2)
monkey = Monkey("Harambe", 17)
bear = Bear("Looz", 3)

the_zoo.add_animal(lion)
the_zoo.add_animal(babylion)
the_zoo.add_animal(monkey)
the_zoo.add_animal(bear)

lion.feed()
monkey.feed()
bear.feed()

the_zoo.print_all_info()