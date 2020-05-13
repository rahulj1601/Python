# Classes and Objects

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "xxxx"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()

class Vehicle:
    name = ""
    kind = ""
    colour = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.colour, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.colour = "red"
car1.kind = "convertible"
car1.value = 10000.00

car2 = Vehicle()
car2.name = "Jump"
car2.colour = "blue"
car2.kind = "van"
car2.value = 60000.00

print(car1.description())
print(car2.description())
