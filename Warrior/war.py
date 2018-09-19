class Warrior:
    health = 50
    attack = 5
    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    
class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    j = True
    i = 1
    print(unit_1, unit_2)
    while (unit_1.health > 0) and (unit_2.health > 0):
        if(i%2):
            unit_2.health -= unit_1.attack
            print(unit_2, unit_2.health, i)
            i += 1
        else:
            unit_1.health -= unit_2.attack
            print(unit_1, unit_1.health, i)
            i += 1
    if(unit_1.health > 0):
        print(1)
        j = True
    else:
        print(0)
        j = False
    return j    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    
    print(chuck.is_alive)

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False    
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert chuck.is_alive == True
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
