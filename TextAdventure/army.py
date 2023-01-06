# Base class for all items
class Army():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Treasure class will be a child or subclass of the superclass Item
class Treasure(Army):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Treasure",
                         description="A heap of diamonds {} in the Port city".format(str(self.amt)),
                         value=self.amt)

class Type_of_army(Army):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Dhotraki(Type_of_army):
    def __init__(self):
        super().__init__(name="Dhotraki",
                         description="nomadic horse-mounted warriors",
                         value=0,
                         damage=1500)
 
class Dragons(Type_of_army):
    def __init__(self):
        super().__init__(name="Dragons",
                         description="Dragons are massive, flying reptiles that can breathe fire.",
                         value=10,
                         damage=5000)
class Unsullied(Type_of_army):
    def __init__(self):
        super().__init__(name="Unsullied",
                         description="Unsullied are are slave-soldiers famed for their skills and discipline in battle.",
                         value=1,
                         damage=1000)