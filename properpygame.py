class person:
    head = 1 
    legs = 2
    arms = 2


    def __init__(self, name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def details(self):
        print("My name is ",self.name)
        print("I am ",self.age,"years old")
        print("My weight is",self.weight)
    def modify(self):
        firstname = input("enter your name: ")    
        age = int(input("enter your age: "))
        weight = int(input("enter your weight: "))    
        self.name = firstname
        self.age = age
        self.weight = weight




p1 = person("Viktor",99,3,50)
p2 = person("Danstan",200,7,53)


#print(p1.name)
#print(p2.age)
p1.modify()
p1.details()










