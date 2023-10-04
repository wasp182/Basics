import random

class Enemy:
# class Enemy(object): this works the same way as above
    # This is a base class that can be inherited by different types of enemies
    def __init__(self,name="Enemy",hit_points=0,lives=1):
        self.name =name
        self.lives = lives
        self.hit_points = hit_points
        self.alive = True

    def take_damage(self,damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0 :
            self.hit_points = remaining_points
            print("{} took {} points damage with {} remaining".format(self.name,damage, remaining_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else :
                print("{0.name} is dead".format(self))
                self.alive = False


    def __str__(self):
        return "Name: {0.name} , Hit : {0.hit_points} , Lives : {0.lives}".format(self)


class Troll(Enemy):
# all trolls have 1 life and 23 hit points
    def __init__(self,name):
        # sub class method is shadowing the super class method
        # Enemy.__init__(self, name = name , lives= 1 , hit_points=23)
        # for dealing with multiples inheritance we would use super class method instead
        # super(Troll,self).__init__(name = name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("me {0.name}".format(self))


class Vampyre(Enemy):
    def __init__(self,name):
        super().__init__(name=name,lives=3,hit_points=12)

    def dodges(self):
        if random.randint(1,3)==1:
            print("***** Vampyre {0.name} dodges attack***".format(self))
            return True
        else:
            return False

    # we want to built in the dodges functionality within the game class and not to be checked in test
    # we will override the take damage method in vampyre class

    def take_damage(self,damage):
        if not self.dodges():
            super(Vampyre, self).take_damage(damage=damage)


class VampyreKing(Vampyre):
    def __init__(self,name):
        super(Vampyre, self).__init__(name=name)
        self.hit_points=140

    def take_damage(self,damage):
        super(Vampyre,self).take_damage(damage=damage//4)




