import random, sys, copy, os, time, textwrap, cmd
from heroine_game.character import *
from heroine_game.items import *
from heroine_game.locations import *

# setup
directions = ["N", "E", "S", "W"]
monster_types = ['Dragon', 'Troll', 'Warlock']
heroine_types = {'W': Witch(), 'Witch': Witch(), 'G': Gunslinger(), 'Gunslinger': Gunslinger(), 'G': Gunslinger(),
                 'Ninja': Ninja(), 'N': Ninja(), 'P': Pacifist, 'Pacifist': Pacifist(), 'A': Amazon(),
                 'Amazon': Amazon()}
# player options
response_options = {'object_choices': ['o', 'objects'],
                    'direction_choices': ['n', 's', 'e', 'w', 'north', 'east', 'south', 'west'],
                    'quit_choices': ['quit', 'q', 'qui'],
                    'inventory_choices': ['i', 'inventory'],
                    'heroine_choices': ['witch', 'gunslinger', 'ninja', 'pacifist', 'amazon', 'w', 'a', 'g', 'n', 'p'],
                    }

typing_speed = {'slow': 65, 'medium': 80, 'fast': 100, 'very fast': 140, 'max': 10000}
SCREEN_WIDTH = 80
decoration = '====='
inventory = ['README Note']  # start with blank inventory
turn = 0

# initiate evil characters
ogre = Ogre()
dragon = Dragon()
warlock = Warlock()
troll = Troll()

# initiate good characters

witch = Witch()
ninja = Ninja()
pacifist = Pacifist()
amazon = Amazon()
gunslinger = Gunslinger()

# initiate weapons
wand = Wand()
running = Running()
archery = Archery()
ninja_star = NinjaStars()
sword = Sword()
rock = Rock()
dagger = Dagger()

heroine = Witch()


def type_text(t, speed=typing_speed['medium']):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / speed)
    print('')


def flip_coin(p):
    result = np.random.binomial(1, p)
    return result


def initiate_objects():
    items_in_location = []
    result = flip_coin(.5)
    while items_in_location < 1:
        gold = Gold(random.randint(1, 10))  # initiate random amount of gold
        items_in_location.append(gold)
    return items_in_location


def initiate_enemies(level=1):
    result = flip_coin(.5)

    def make_dragon():
        dragon = Dragon()
        return dragon

    def make_ogre():
        ogre = Ogre()
        return ogre

    def make_warlock():
        warlock = Warlock()
        return warlock

    def make_troll():
        troll = Troll()
        return troll

    enemies = []
    enemy_factory = [make_troll(), make_warlock(), make_ogre(), make_dragon()]

    if level == 1:
        while len(enemies) < 1:
            new_enemy = random.choice(enemy_factory)
            enemies.append(new_enemy)
        print("There is {} {} nearby.".format(len(enemies), enemies[0].name))
        print("\n")
        for this_enemy in enemies:
            print(this_enemy)
            print("*****\n")
    if level == 2:
        while len(enemies) < 2:
            new_enemy = random.choice(enemy_factory)
            enemies.append(new_enemy)
        print("There is {} {} nearby.".format(len(enemies), enemies[0].name))
        print("\n")
        for this_enemy in enemies:
            print(this_enemy)
            print("*****\n")
    if level == 3:
        while len(enemies) < 3:
            new_enemy = random.choice(enemy_factory)
            enemies.append(new_enemy)
        print("There is {} {} nearby.".format(len(enemies), enemies[0].name))
        print("\n")
        for this_enemy in enemies:
            print(this_enemy)
            print("*****\n")

    return enemies


def get_input():
    response = (input('\n\n>'))
    return response


def battle_scene(player, enemy, enemies):
    print("An enemy {} has appeared . . .".format(enemy.name))
    # combat loop
    while player.hp > 0 and enemy.hp > 0:
        player.attack(enemy, player.current_weapon)
        print("The health of the {} is now {}.".format(enemy.name, enemy.hp))
        if enemy.hp <= 0:
            break
        enemy.attack(player)
        print("Your health is now {}".format(player.hp))
    if player.hp > 0:
        print("You have defeated the {}.".format(enemy))
        enemies.remove_enemy(enemy)
    elif enemy.hp > 0:
        print("The {} defeated you.".format(enemy))


# initiate misc
gold = Gold(random.randint(18, 20))  # initiate random amount
starting_note = Note(message="To whomever finds this note, head these words - these woods are dangerous and all isn't "
                             "what it seems.")


def initialize_location(heroine):
    gold = Gold(random.randint(18, 20))  # initiate random amount
    starting_note = Note(
        message="To whomever finds this note, head these words - these woods are dangerous and all isn't "
                "what it seems.")
    heroine.current_location.inventory.add_item(gold)
    heroine.current_location.inventory.add_item(starting_note)


locations = {'town hall': Location(name='Town Hall',
                                   description='You are in the town hall.\n A fountain bubbles nearby and there are '
                                               'some shops nearby.',
                                   east='woods',
                                   west='lake',
                                   current_location='town hall'),
             'woods': Location(name='The Woods',
                               description='You are in the woods, surrounded on all sides by Trees',
                               north="open road",
                               current_location='woods'),
             'lake': Location(name='The Lake',
                              description='You are by the Lake. It is as wet as one might assume.',
                              east='town hall',
                              south='open road',
                              current_location='lake'),
             'open road': Location(name='The Open Road',
                                   description='You are on an open road, it stretches on as long as your eye can see.',
                                   north='lake',
                                   south='woods',
                                   current_location='open road'),
             'Not on Map': Location(name='Not on Map',
                                    description='Default for characters. Impossible to get to. Not on map.',
                                    current_location='Not on Map'
                                    )}


def initiate_player(player):
    player.inventory.add_item(gold)
    player.current_location = locations['woods']
    player.inventory.add_item(starting_note)
    return player


def random_loc_inventory():
    new_gold = Gold(random.randint(1, 10))  # initiate random amount


# level_1_enemy = initiate_enemies(1)

# STORY
# introduction

intro_message_overview = "\nYou are a heroine in this adventure story.\n\n" \
                         "You find yourself trapped in an unfamiliar land.\n" \
                         "You aren't scared, though.\nYou know if you use your wit, " \
                         "that you will survive."
intro_message_current_location = "\nYou've started your adventure in the forest, surrounded by trees, making it " \
                                 "difficult to tell what danger may await you."
intro_hear_noise = "You hear something near by to your east. \nOr, wait. . .  is it your west?\n"
intro_urgent = "Either way, it's time to move! \nQuickly, hero, what is your name?"


# type intro
def type_intro():
    type_text(intro_message_overview, typing_speed['max'])  # slow
    type_text(intro_message_current_location, typing_speed['max'])  # medium
    type_text(intro_hear_noise, typing_speed['max'])  # fast
    type_text(intro_urgent, typing_speed['max'])  # very fast
    name = get_input()
    return name


def get_hero(heroine_type, obj=0, typ=0):
    if obj == 1:
        return heroine_types[heroine_type]
    elif typ == 1:
        return heroine_types[heroine_type].get_possible_weapons()
    else:
        return None


def get_heroine_type(heroine_name):
    response_handler = "Great, thank you, {}, the pleasure is all mine. Who am I? Well, we will have more time to " \
                       "discuss that later. For now, what kind of heroine are you, anyway? Witch, Gunslinger, Ninja, " \
                       "Pacifist, Amazon? \n Type in the first letter of the heroine Type and press enter to get a " \
                       "description.".format(heroine_name)
    type_text(response_handler, typing_speed['max'])  # very fast
    heroine_check = "n"

    while heroine_check[0].lower() != "y":
        heroine_check = get_input()
        if heroine_check.lower() in response_options['heroine_choices'] or heroine_check in heroine_types.keys():
            if heroine_check[0].title() == "W":
                print(get_hero('Witch', obj=1))
                print("\n\n\t" + "*" * 50)
                print("\n" +("\t"*5)+"POSSIBLE WEAPON TYPES")
                print(get_hero('Witch', typ=1))
            elif heroine_check[0].title() == "G":
                print(get_hero('Gunslinger', obj=1))
                print("\n\n\t" + "*" * 50)
                print("\n" +("\t"*5)+"POSSIBLE WEAPON TYPES")
                print(get_hero('Gunslinger', typ=1))
            elif heroine_check[0].title() == "N":
                print(get_hero('Ninja', obj=1))
                print("\n\n\t" + "*" * 50)
                print("\n" +("\t"*5)+"POSSIBLE WEAPON TYPES")
                print(get_hero('Ninja', typ=1))
            elif heroine_check[0].title() == "A":
                print(get_hero('Amazon', obj=1))
                print("\tPOSSIBLE WEAPON TYPES")
                print(get_hero('Amazon', typ=1))
            elif heroine_check[0].title() == "P":
                print(get_hero('Pacifist', obj=1))
                print("\n" +("\t"*5)+"POSSIBLE WEAPON TYPES")
                print(get_hero('Pacifist', typ=1))
            else:
                "Invalid Response."
        print("\nEnter 'Y' to exit if you decide your choice. Otherwise enter another choice")
    type_text("Okay, hero do you want to be? Type the full name.", typing_speed['max'])
    heroine_type = input(str("> "))
    if heroine_type.title() in heroine_types.keys():
        heroine = heroine_types[heroine_type.title()]
        print(heroine)
    return heroine


def get_weapon_choice(heroine, heroine_type):
    type_text("What weapon do you want to start with? Here are your choices again.")
    print(heroine.get_possible_weapons())
    weapon_start = get_input()
    type_text("Fantastic. You're a {} and you've brought along a {} -- you'll be even more handy than I "
              "thought!".format(heroine_type.name, weapon_start), typing_speed['max'])
    type_text("Time to go though. Take a look around but make it fast.")
    return weapon_start


def get_current_status(heroine):
    heroine.hp
    heroine.xp
    heroine.current_weapon
    heroine.current_location
    heroine.inventory.items['gold']
    print('Character Status:\n'
          '*****************'
          'HP: {}\n'
          'XP: {}\n'
          'Current Weapon: {}\n'
          'Current Location: {}\n'
          'Gold: {}')


def describe_response_options():
    print("There are some objects near by. If you would like to see objects, type in 'O' or 'Objects.")
    print('If not, what direction would you like to go? Type first letter ("N","S","E","W").')
    print("At any point you can check your inventory by typing in 'I' and pressing enter.")