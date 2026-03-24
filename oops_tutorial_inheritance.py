class Animal:
    def __init__(self,a):
        self.age = a
        print(self.age/7)
    def feed(self):
        print("Dog is feeeding.")

class dog(Animal):
    def bark(self):
        print("Dog is barking.")
b = int(input())
d = dog(b)
d.bark()
d.feed()

