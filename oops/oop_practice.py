class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}says wooff!")
    
    def have_birthday(self):
        self.age = self.age + 1
        print(f"{self.name} is now {self.age} year old")


rex = Dog("Rex", 5)
rex.bark()

bella = Dog("bella", 3)
bella.have_birthday()
mimi = Dog("Mimi", 2)

print(rex.name, rex.age)
print(bella.name, bella.age)
print(mimi.name, mimi.age)