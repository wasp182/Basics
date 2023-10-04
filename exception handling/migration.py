import ducks

flock= ducks.flock()
d1 = ducks.Duck()
d2 = ducks.Duck()
d3 = ducks.Duck()
percy = ducks.Penguin()
d4 = ducks.Duck()

flock.add_duck(d1)
flock.add_duck(d2)
flock.add_duck(d3)
flock.add_duck(percy)
flock.add_duck(d4)

flock.migrate()

