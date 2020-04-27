# item SuperClass
class Item:
    """The base class for all items"""

    def __init__(self, name, description, value, message=None):
        self.name = name
        self.description = description
        self.value = value
        self.message = message

    def __str__(self):
        return "\n{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        del self.items[item.name]

    def add_gold(self, amt):
        return int(self.items['gold'].amt) + amt

    def pretty_print_items(self):
        print('You are currently carrying the following items:\n*******\n')
        print('\t'.expandtabs(10).join(['Name', 'Value', 'Description']))
        for item in self.items.values():
            print('\t'.expandtabs(10).join([str(x) for x in [item.name, item.value, item.description]]))

    # def __str__(self):
    #     out = '\t'.join(['Name', 'Value', 'Description'])
    #     for item in self.items.values():
    #         out += '\n' + '\t'.join([str(x) for x in [item.name, item.value, item.description]])
    #     return out


# MISC items
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

    def found_gold(self, new_amt):
        self.amt += new_amt
        value = self.amt


class Note(Item):
    def __init__(self, message):
        self.message = message
        super().__init__(name="Note",
                         description="A crumpled note.",
                         value=0)

    def read_note(self):
        return self.message

    def __str__(self):
        return "\nDescription:{}\n=====\n{}\nValue: {}\nMessage: \n".format(self.description, self.value,
                                                                            self.message)


# Potions
class Potion(Item):
    def __init__(self, name, description, value, damage=0, level=0):
        self.name = name,
        self.description = description,
        self.value = value

    def __str__(self):
        return "{}\n\t=====\n\tDescription: {}\n\tValue: {}\n\t".format(self.name,
                                                                        self.description,
                                                                        self.value)


class HealthPotion(Potion):
    def __init__(self, name, description, value):
        self.name = name
        self.description = "A potion that heals your HP."
        self.value = value


class SmallHealthPotion(HealthPotion):
    def __init__(self, hp_amt, value):
        self.hp_amt = 10
        self.value = 10


class Medium(HealthPotion):
    def __init__(self, hp_amt, value):
        self.hp_amt = 20
        self.value = 20


class LargeHealthPotion(HealthPotion):
    def __init__(self, hp_amt, value):
        self.hp_amt = 30
        self.value = 30


# Shields
class Shield(Item):
    def __init__(self, name, description, value, deducts_damage, damage=0, level=1):
        self.name = name,
        self.description = description,
        self.value = value,
        self.level = level,
        self.deducts_damage=deducts_damage

    def __str__(self):
        return "\n\t{}\n\t=====\n\t{}\n\tValue: {}\n\tLevel: {}".format(self.name,
                                                                        self.description,
                                                                        self.value,
                                                                        self.level)


class BeginnersShield(Shield):
    def __init__(self, deducts_damage):
        self.deducts_damage = 5
        self.name = "Beginner's Shield"
        self.description = "A basic shield that protects from some damage."
        self.value = 5


# weapons section
class Weapon(Item):
    def __init__(self, name, description, value, damage, level=1):
        self.damage = damage
        self.level = level
        super().__init__(name, description, value)

    def __str__(self):
        return "\n\t{}\n\t=====\n\t{}\n\tValue: {}\n\tDamage: {}\n\tLevel: {}".format(self.name,
                                                                                      self.description,
                                                                                      self.value,
                                                                                      self.damage,
                                                                                      self.level)


weapon_types = ['Wand', 'Rock', 'Broomstick', 'Fists', 'Guns', 'Karate', 'NinjaStars', 'Running',
                'Sword', 'Dagger', 'Archery']


class Running(Weapon):
    def __init__(self):
        super().__init__(name="Running",
                         description="Your own two feet. Only limited by your endurance; "
                                     "impossible to sell in THIS economy.",
                         value=0,
                         damage=0,
                         level=1)


class Archery(Weapon):
    def __init__(self):
        super().__init__(name="Archery",
                         description="Good ol' fashion bow and arrow action. Like sharper, longer, slower bullets.",
                         value=12,
                         damage=40,
                         level=1)


class Guns(Weapon):
    def __init__(self):
        super().__init__(name="Guns",
                         description="Two guns. #1 choice for murder.",
                         value=25,
                         damage=40,
                         level=1)


class NinjaStars(Weapon):
    def __init__(self):
        super().__init__(name="Ninja Stars",
                         description="Painful but hard to keep track of on account of all the throwing.",
                         value=15,
                         damage=25)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="Sharp, deadly, and completely useless against guns. Thankfully, most monsters don't carry them.",
                         value=50,
                         damage=30,
                         level=1)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=1,
                         damage=5,
                         level=1)


class Wand(Weapon):
    def __init__(self):
        super().__init__(name="Wand",
                         description="Magical wand. Does lots of damage.",
                         value=10,
                         damage=10,
                         level=1)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10,
                         level=1)


class Wand(Weapon):
    def __init__(self):
        super().__init__(name="Wand",
                         description="A wand with a spell attack. More dangerous than a a dagger.",
                         value=15,
                         damage=15,
                         level=1)


class Intellect(Weapon):
    def __init__(self):
        super().__init__(name="Intellect",
                         description="Weaseling your way out with words.",
                         value=0,
                         damage=0,
                         level=1)


class Broomstick(Weapon):
    def __init__(self):
        super().__init__(name="A broomstick",
                         description="Shoots literal fireballs. Not kidding",
                         value=100,
                         damage=50)


class Karate(Weapon):
    def __init__(self):
        super().__init__(name="Karate",
                         description="Ninja fighting style that hurts more than fists but less than anything sharp.",
                         value=100,
                         damage=50,
                         level=1)
