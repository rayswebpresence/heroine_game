from heroine_game.character import *
from heroine_game.setup_and_helper_functions import *

entered_new_room = False
next_location = "go"

turn = 1
while next_location != "quit":
    if turn == 1:
        # get player's name
        heroine_name = type_intro()

        # get desired hero type
        heroine_type = get_heroine_type(heroine_name)

        # initialize hero
        heroine = initiate_player(heroine_type)

        # set current weapon to user's choice
        heroine.current_weapon = get_weapon_choice(heroine, heroine_type)

        # intialize current location
        initialize_location(heroine)

        turn += 1
    else:
        print(heroine.current_location)
        # print options for character
        describe_response_options()
        response = input(str("> "))
        if response.lower() == "i":
            heroine.inventory.pretty_print_items()
        elif response.lower() == "o":
            heroine.current_location.pretty_print_location_items()
        elif response in heroine.current_location.directions.keys():
            next_location = response
            heroine.move_character(next_location)
            heroine.current_location.enemies = initiate_enemies(1)
            enemies = heroine.current_location.enemies
            print("You can choose to fight or flee. Type in 'fight' to fight or 'evade' to try to run away.")
            response = get_input().lower()
            if response.lower[0] == 'f':
                while len(heroine.current_location.enemies) > 0:
                    enemy = heroine.current_location.enemies[0]
                    battle_scene(heroine, enemy, heroine.current_location.enemies)
        else:
            describe_response_options()
        turn += 1






# result = lambda bullets dragons: (bullets - (dragons * 2)) if (bullets / 2) >= dragons else 0
# global heroine_name
#
# start_bullets = int(random.randrange(20, 40, 1))
# global start_bullets
#
# start_dragons = int(random.randrange(1, 10, 1))
# global start_dragons
#
#
# def inventory_and_dragons(heroine_name, bullets, dragons, turn): if turn == 1: start_msg = "Your heroine {} is
# traveling in an expansive, dangerous place. Will she defeat the dragons after " \ "her?".format(heroine_name,
# bullets) bullets_msg = "\nShe checks her inventory and sees she has {} bullets.".format(bullets) dragons_msg =
# "Suddenly, {} dragons appear.".format(dragons)
#
# return start_msg, bullets_msg, dragons_msg else: bullets_msg = "Your heroine {} checks her inventory and sees she
# has {} bullets.".format(heroine_name, bullets) dragons_msg = "Suddenly, {} dragons appear.".format(dragons) return
# "", bullets_msg, dragons_msg
#
#
# def battle_result(heroine_name, bullets, dragons, remaining_bullets):
#     if remaining_bullets > 0:
#         result = "Our heroine {} has survived the battle! There's {} bullets left.".format(heroine_name, int(
#             round(remaining_bullets, 0)))
#         return result
#     else:
#         result = "Our heroine {} was overwhelmed by the dragons. The {} bullets only killed {} dragons.".format(
#             heroine_name, bullets, abs((dragons * 2) - bullets))
#         return result
#
#
# def new_dragons_bullets():
#     new_dragons = random.randrange(1, 10, 1)
#     found_bullets = random.randrange(5, 10, 1)
#     found_msg = "{} found {} bullets.".format(heroine_name, found_bullets)
#     return new_dragons, found_bullets, found_msg
#
#
# def take_turn(bullets, dragons, turn):
#     if turn == 1:
#         start_msg, bullets_msg, dragons_msg = inventory_and_dragons(heroine_name, start_bullets, start_dragons, turn)
#         remaining_bullets = result(start_bullets, start_dragons)
#         outcome = battle_result(heroine_name, start_bullets, start_dragons, remaining_bullets)
#         new_dragons, found_bullets, found_msg = new_dragons_bullets()
#         current_bullets = bullets + (found_bullets + remaining_bullets)
#
# turn += 1 return found_msg, start_msg, bullets_msg, dragons_msg, remaining_bullets, outcome, new_dragons,
# found_bullets, current_bullets, turn start_msg, bullets_msg, dragons_msg = inventory_and_dragons(heroine_name,
# bullets, dragons, turn) remaining_bullets = result(bullets, dragons) outcome = battle_result(heroine_name, bullets,
# dragons, remaining_bullets) new_dragons, found_bullets, found_msg = new_dragons_bullets() current_bullets = bullets
# + (found_bullets + remaining_bullets) turn += 1
#
# return found_msg, "", bullets_msg, dragons_msg, remaining_bullet s, outcome, new_dragons, found_bullets,
# current_bullets, turn
#
#
# def start_game():
#     current_bullets = 0
#
# # total is before battle, remaining is after turn = 1 while True: found_msg, start_msg, bullets_msg, dragons_msg,
# remaining_bullets, outcome, new_dragons, found_bullets, current_bullets, turn = take_turn( turn, start_bullets,
# start_dragons) if turn == 1: print("After surviving {}'s first battle, she finds {} bullets.".format(heroine_name,
# found_bullets)) print(start_msg) print(bullets_msg) print(dragons_msg) print(outcome) print(found_msg) turn += 1
# else: print(bullets_msg) print(dragons_msg) turn += 1
#
#             if remaining_bullets == 0:
#                 print("{}'s adventure ended after {} turns.".format(heroine_name, turn))
#                 break
#             else:
#                 print(outcome)
#                 print(found_msg)
#
#
# if __name__ == '__main__':
#     start_game()
