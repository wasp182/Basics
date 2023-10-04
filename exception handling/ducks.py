class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    def __init__(self):
        self.fly=self.aviate

    def aviate(self):
        print('fly without wings')

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

class Mallard(Duck):
    pass

class flock():
    def __init__(self):
        self.flock=[]

    def add_duck(self,duck: Duck)-> None:
        # if type(duck) is Duck:
        # if isinstance(duck,Duck):
        # above methods are not pythonic , we want to check if duck can fly to apply this function in migrate()
        # getattr will check object dictionary to check if it has the fly attribute
        # if no attr then we get error , callable checks if fly method is callable
        if callable(getattr(duck,'fly',None)):
            self.flock.append(duck)
        else:
            raise TypeError("check correct type, input  might be "+ str(type(duck).__name__))

    def migrate(self):
        problem = None
        for ducks in self.flock:
            try:
                ducks.fly()
            except AttributeError as e:
                print('one duck down')
                problem = e
        if problem:
            raise problem

if __name__ == '__main__':
    donald = Duck()
    donald.fly()


