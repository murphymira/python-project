class Animal:
    def __init__(self, name, age=0):
        print("from Animal")
        self.name = name
        self.age = age

    def speak(self):
        return "Animal speak"


class Dog(Animal):
    def __init__(self, name, age, type_):
        print("from Dog")
        super().__init__(name, age)
        self.type = type_
    
    def speak(self):
        super().speak()
        return "dog speak"

    
class cat (Animal):
    def __init__(self, name, age, type_):
        print("from Cat")
        super().__init__(name, age)
        self.type = type_











