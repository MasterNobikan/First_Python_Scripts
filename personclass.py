class Person: # capitalize class names
    def __init__(self, name, age, shirt_color): # self precedes all else
        self.name = name
        self.age = age
        self.shirt_color = shirt_color

    def getAge(self):  # accessor
        return self.age

    def getName(self):
        return self.name

    def sayHello(self): # general method
        print('Hello, my name is', self.name)

class Dog:
    def __init__(self, name, owner): # constructor
        self.name = name
        self.owner = owner

    def set_owner(self, new_owner): # mutator
        self.owner = new_owner

    def get_owner(self):
        return self.owner
    

def main():
    person1 = Person('Beau', 31, 'black')
    person2 = Person('Bob', 50, 'red')

    dog1 = Dog('Fido', None)
    dog1.set_owner(person2)
    
    print(dog1.get_owner().getName())
    
    print(person2.getAge())
    person2.sayHello()
    
main()
