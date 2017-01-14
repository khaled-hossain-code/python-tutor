class Animal(object):
    def __init__(self):
        print "Animal created"
    def eat(self):
        return "Eating"

class Dog(Animal):
    #class object attribute, this variable is available to all the instance of this class
    species = "mamal" #this is a public variable

    def __init__(self,breed,name='doggy'):
        Animal.__init__(self)
        self.breed = breed #this variables can be accessed from outside of class
        self.name = name
    
    def greet(self):   
        return "hello "+ Dog.species
    
    def __str__(self):
        return "Name: {name}, ".format(name=self.name)
    
    def __len(self):
        return "length of this object is 2"
    
    def __del__(self):
        return "A dog is gone"


puppy = Dog(name="chuchu", breed = "puppy")
print puppy
print puppy.name
puppy.name = "puppy2"
print puppy.name
print puppy.breed
print puppy.species
print puppy.eat()


tommy = Dog("alsetian")
print tommy.breed
print tommy.name
print tommy.greet()