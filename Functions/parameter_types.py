def func(p1,p2,*args,k,k1,**kwargs):
    print("positional.......{},{}".format(p1,p2))
    print("var-positional...{}".format(*args))
    print("keyword..........{0},{1}".format(k,k1))
    print("var keyword......{}".format(kwargs))


func(1,2,4,5,6,7,k=78,k1=89,k2=55)
