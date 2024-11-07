# raise error example 1
# NotImplementedError 
# abstract method 

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this func in subclass')  #1

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return 'bhau bhau'

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'
doggy = Dog('boony' ,'pug')
print(doggy.sound())
cat1 = Cat('avoony' ,'russian')
print(cat1.sound())

# here we raised a NotImplementedError to print the sound of the respected animal
# and we called abstract method to 1 its not a python method but a java script method
#  