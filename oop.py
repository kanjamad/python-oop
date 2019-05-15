class Dog():
    # class
    total_dogs = 0
    def __init__(self, name="", age=1, color=""):
        # instantiated memory
        self.name = name
        self.age = age
        self.color = color        
        Dog.total_dogs += 1
        print(name, "create =>", self)
    
    def __str__(self):
        return 'Dog -> name: {}, age: {}'.format(self.name, self.age)

    def bark_hello(self):
        print('Woof! I am {} called {} and I am {} human-years old'.format(self.color, self.name, self.age))
        print('There are {} dogs total'.format(Dog.total_dogs))

gracie = Dog('Gracie',8)
spitz = Dog('Spitz',5)
buck = Dog('Buck', 5)
gracie.bark_hello()
spitz.bark_hello()
buck.bark_hello()
print(Dog.total_dogs)




# ----------------------------------------------

class Parent():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print('Parent initialized ', self)

    def say_hello(self):
        print('Hello, I am {}'.format(self.first_name))

class Child():
    def __init__(self, first_name, last_name='Gilmore'):
        Parent.__init__(self)
        self.first_name = first_name
        print('Child initialized ', self)

    def say_hello(self):
        print('Hey I am {}, gotta go!'. format)


lorelei = Parent('Lorelei', 'G')
lorelei.say_hello()
rory = Child('Rory')