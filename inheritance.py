class Pet:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

class Cat(Pet):
        def __init__(self, name, age, color):
          super().__init__(name, age)
          self.color = color
        def speak(self):
           print("meow")
        def show(self):
           print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")
    
        def show(self):
          print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 12)
p.show()
c = Cat("Bill", 13, "Red")
print(c.color())
c.show()
d = Dog("Tom", 18)
d.speak()
d.show()
