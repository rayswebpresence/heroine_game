from heroine_game.items import Inventory
from heroine_game.setup_and_helper_functions import *


class Location:
    def __init__(self,
                 name,
                 description,
                 current_location,
                 enemies=[],
                 north="There's nothing to the North.",
                 south="There's nothing to the South.",
                 east="There's nothing to the East.",
                 west="There's nothing to the West."
                 ):
        self.name = name
        self.description = description
        self.current_location = current_location
        self.directions = {'North': north,
                           'South': south,
                           'West': west,
                           'East': east,
                           'CurrentLocation': current_location}

        self.inventory = Inventory()
        self.enemies = enemies
        self.enemies = enemies

    def remove_enemy(self, enemy):
        del self.enemies[enemy]

    def __str__(self):
        return "\n{}\n=====\nDescription of Current Location: {}\n\nLocations Nearby\n*****\nTo the North: {}\nTo the" \
               " South: {}\nTo the East: {}\nTo the West: {}".format(self.name,
                                                                     self.description,
                                                                     self.directions['North'],
                                                                     self.directions['South'],
                                                                     self.directions['East'],
                                                                     self.directions['West'],
                                                                     self.directions['CurrentLocation'])

    def pretty_print_location_items(self):
        location = self.inventory.items
        print('There are currently the following items here:\n*******\n')
        print('\t'.expandtabs(10).join(['Name', 'Value', 'Description']))
        for item in self.inventory.items.values():
            print('\t'.expandtabs(10).join([str(x) for x in [item.name, item.value, item.description]]))

    def remove_from_ground(self, item):
        if item in self.ground:
            retrieved_item = item
            self.ground.remove(item)
            return retrieved_item

    def find_by_location(self, direction):
        # set to title case
        direction = direction.title()
        if direction == "N":
            direction = "North"
        elif direction == "W":
            direction = "West"
        elif direction == "S":
            direction = "South"
        elif direction == "E":
            direction = "East"
        # on error, stay put
        else:
            stay_put = "CurrentLocation"
            return
        new_direction = self.directions[direction]
        if new_direction == "There's nothing to the " + direction + ".":
            return self.current_location
        else:
            return new_direction


class Store(Location):
    def __init__(self, name, description,
                 ground=["There's nothing on the ground."],
                 north="There's nothing to the North.",
                 south="The exit is to the South.",
                 east="There's nothing to the East.",
                 west="There's nothing to the West."):
        self.name = name
        self.description = description
        self.directions['North'] = north
        self.directions['South'] = south
        self.directions['West'] = west
        self.directions['East'] = east
        self.ground = ground
