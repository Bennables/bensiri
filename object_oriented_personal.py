class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed



    def bark(self):
        print("bark bark bark")

    def printInfo(self):
        print(f"Name: {self.name} Age: {self.age} Breed {self.breed}")

    def increaseage(self):
        self.age += 1
#or
    def increase_age(self,addage):
        self.age += addage





dog1 = Dog("Wilbur",3,"Dawg")
dog2 = Dog("Doug",4,"Sheep")

print(dog1.name)
print(dog1.age)
print(dog1.breed)
dog1.bark()
dog2.bark()
dog1.printInfo()
dog2.printInfo()
dog1.increaseage()
dog1.printInfo()
dog1.increase_age(1)

b = []
b.append (dog1.name)
print (b)


class criminal_children:
    def __init__(self, name, months, age, parents):
        self.name = name
        self.months = months
        self.age = age
        self.parents = parents
    
    def printall(self):
        print(self.name)
        print(self.months)
        print(self.age)
        print(self.parents)
    
    def add_time(self):
        self.time += 1
    
    def add_age(self):
        self.age += 1
    
    def dead_parents(self):
        if self.parents == "alive":
            self.parents = ("killed")

child1 = criminal_children("Henry", 5, 12, "alive")
child2 = criminal_children("Mary", 3, 9, "dead")

child1.printall()

class parents(criminal_children):
    def __init__(self,job,age,height):
        self.job = job
        self. age = age
        self.height = height

