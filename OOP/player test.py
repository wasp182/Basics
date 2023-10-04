from player import player
from enemy import Enemy, Troll , Vampyre , VampyreKing

tim= player("tim")
random_monster = Enemy("jackass", 12,1)
print(tim)
print(random_monster)

ugly_troll = Troll("first one")
print(ugly_troll)
#
# another_troll = Troll("troll1")
# print(another_troll)
#
# brother_troll = Troll("bro troll")
# print(brother_troll)

# no overloading in python , we dont have to specify each constructor with
# with optional arguments but python doesnt require this overloading
vamps = Vampyre("vlad")
print(vamps)

while vamps.alive:
    vamps.take_damage(1)
    print(vamps)

king = VampyreKing("king")
print(king)
king.take_damage(15)
print(king)