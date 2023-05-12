class Animal:
    def __init__(self, habit):
        self.habit =habit

    def print_habit(self):
        print(self.habit)

    def sound(self):
        print("some animal sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("kennel")

    def sound(self):
        print("Woof woof!")

x=Dog()
x.print_habit()
x.sound()

    
    
