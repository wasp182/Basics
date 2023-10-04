class Kettle():
    # class attributes are shared by all instances of class -
    # similair to static variables
    power_source ="electricity"
    def __init__(self,make,price):
        self.make= make
        self.price=price
        self.on = False

    def switch_on(self):
        self.on=True


kenwood = Kettle("Kenwood",10)
print(kenwood.price)

hamilton = Kettle("hamilton",15)

kenwood.switch_on()
print(kenwood.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power=1.5
print(kenwood.power)

kenwood.power_source="atomic"
Kettle.power_source="nuclear"
print(kenwood.power_source)
# op is atomic , python chooses local value of kenwood power source ,
# in second line we have only updated the genberal class attribute
#below will print nuclear
print(hamilton.power_source)
