import pickle

class Animal:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def make_sound(self):
       raise NotImplementedError("Subclasses must implemented this method")

   def eat(self):
       print(f"{self.name} они едят")

class Bird(Animal):
   def make_sound(self):
       print(f"{self.name} чирик чирик!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} гав гав!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} щщщщщщ")

def animal_sound(animals):
  for animal in animals:
     animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, a {animal.__class__.__name__.lower()}, is {animal.age} years old.")
    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, a {staff.__class__.__name__.lower()}.")

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump((self.animals, self.staff),file)

    def load_from_file(self, filename):
        with open(filename, "rb") as file:
            self.animals, self.staff = pickle.load(file)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

        #Создаем объекты
zoo = Zoo()
bird = Bird("Беркут", 3)
mammal = Mammal("Трезор", 5)
reptile = Reptile("Питон", 20)

zookeeper = ZooKeeper("Григорий")
veterinarian = Veterinarian("Валентина")

        #Добавляем сотрудников и животных в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

      #полиморфизм
animal_sound(zoo.animals)

       #информация о зоопарке
zoo.show_animals()
zoo.show_staff()

zookeeper.feed_animal(mammal)
veterinarian.heal_animal(bird)

               #сохранение текущего состояния зоопарка
zoo.save_to_file("zoo_state.pkl")

new_zoo = Zoo()
new_zoo.load_from_file("zoo_state.pkl")
new_zoo.show_animals()
new_zoo.show_staff()




