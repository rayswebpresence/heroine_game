import numpy as np  # for coin_flip
import random  # for enemy_factory
from heroine_game.items import Inventory
from heroine_game.items import *

weapon_objects = {'Wand': Wand(), 'Rock': Rock(), 'Broomstick': Broomstick(), 'Dagger': Dagger(), 'Sword': Sword(),
                  'NinjaStar': NinjaStars(), 'Running': Running(), 'Archery': Archery(), 'Guns': Guns(),
                  'Intellect': Intellect(), 'Karate': Karate()}


# superclass
class Character:
    """The base class for all Characters (Heroines or Enemies)"""

    def __init__(self, name, description, character_type, possible_weapon_types):
        self.name = name
        self.description = description
        self.character_type = character_type
        self.possible_weapon_types = possible_weapon_types

    def __str__(self):
        return "\n{}\n=====\n{}\nType: {}\nWeapons Available: {}\n".format(self.name,
                                                                           self.description,
                                                                           self.character_type,
                                                                           self.possible_weapon_types)

    def attack(self, other):
        raise NotImplementedError


class Enemy(Character):
    def __init__(self, name, hp, damage, reward, description, current_location='Not on Map'):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.reward = reward
        self.description = description
        self.current_location = current_location
        self.character_type = 'Enemy'

    def is_alive(self):
        return self.hp > 0

    def attack(self, hero):
        hero.hp = hero.hp - self.damage

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class HeroineType(Character):
    def __init__(self, name,
                 damage,
                 description,
                 possible_weapon_types,
                 hp=100,
                 stamina=100,
                 xp=0,
                 current_weapon=Rock(),
                 changed_locations=False,
                 current_location='Not on Map'):
        self.current_location = current_location
        self.name = name
        self.damage = damage
        self.description = description
        self.character_type = 'Heroine'
        self.possible_weapon_types = possible_weapon_types
        self.hp = hp
        self.stamina = stamina
        self.xp = xp
        self.current_weapon = current_weapon
        self.changed_locations = changed_locations
        self.inventory = Inventory()

    def get_health(self):
        return self.hp

    def change_weapon(self, new_weapon):
        self.current_weapon = new_weapon

    # todo add potions class then potions for replenishing health/stamina - each have replenish points
    def replenish_health(self, health_potion):
        return self.hp + health_potion.replenish_points

    def replenish_stamina(self, stamina_potion):
        return self.stamina + stamina_potion.repenish_points

    def attack(self, opponent, current_weapon):
        answer = input("Would you like to flee or fight?")
        if answer.lower() == "fight":
            opponent.hp = opponent.hp - current_weapon.damage
        else:
            # todo running should cost HP or endurance so the running 'weapon' has advantage
            print("You've fled the scene.")

    def move_character(self, direction):
        self.changed_locations = False
        if direction.title() not in ['N', 'E', 'W', 'S']:
            print("Invalid direction!")
            return
        else:
            changed_room = True
            print("Moving {} from {} to {}.".format(direction, self.current_location,
                                                    self.current_location.directions[direction]))

            self.current_location = self.current_location.directions[direction]
            self.changed_locations = Trueo

    def __str__(self):
        return "\n==========" \
               "\n{}" \
               "\n==========\nDescription: {}\n" \
               "HP: {}\n" \
               "Damage: {}\n" \
               "Current Weapon: {}\n" \
               "Current Location: {}\n".format(self.name,
                                               self.description,
                                               self.hp,
                                               self.damage,
                                               self.current_weapon.name,
                                               self.current_location)

    def get_possible_weapons(self):
        for x in self.possible_weapon_types:
            if x in weapon_objects:
                print("\n\t" + "*" * 50 + "\n")
                print(weapon_objects[x])


class Witch(HeroineType):
    def __init__(self):
        super().__init__(name="Witch", hp=100, damage=2, description='A magical Witch.',
                         possible_weapon_types=['Wand', 'Rock',
                                                'Broomstick'])


class Gunslinger(HeroineType):
    def __init__(self):
        super().__init__(name="Gunslinger", hp=100, damage=7, description='A gunslinger.', possible_weapon_types=['Guns',
                                                                                                                 'Rock',
                                                                                                                 'Fists'])


class Ninja(HeroineType):
    def __init__(self):
        super().__init__(name="Ninja", hp=100, damage=18, description='A sneaky ninja.', possible_weapon_types=[
            'Rock',
            'Ninja Stars'])


class Pacifist(HeroineType):
    def __init__(self):
        super().__init__(name="Pacifist", hp=100, damage=1, description='A loving pacifist',
                         possible_weapon_types=['Intellect',
                                                'Running'])


class Amazon(HeroineType):
    def __init__(self):
        super().__init__(name="Amazon", hp=100, damage=20, description='A beautiful female warrior.',
                         possible_weapon_types=['Fists', 'Sword', 'Archery'])


class Troll(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=5, damage=2, reward=5, description='A green troll.')


class Warlock(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=7, reward=30, description='A  warlock practicing evil magic.')


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15, reward=30, description='Giant Ogre.')


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=100, damage=20, reward=100, description='Fire breathing dragon.')
