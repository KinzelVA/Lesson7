"""1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`)."""

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











