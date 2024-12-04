class person:
    def __init__ (self,name):
        self.name = name
    age = 0
    hight = 0
    weight = 0 
data = []
p1 = person(input("Enter the number : "))
person.age(int(input ("Enter the age : ")))
person.hight(float(input("Enter the hight in Cm : ")))
person.weight(float (input("Enter the weight in Kg :")))
data.append(p1)
print(data)


