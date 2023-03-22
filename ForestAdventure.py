from lib import classes
import random

give_it_a_try = 0

while give_it_a_try == 0:
  print("Hello adventurer! Welcome to your conquest!")
  print("Try to see how many enemies from the forest your hero can defeat before taking fatal damage!")
  hero_name = input("What is the name of this hero?\n" )
  hero_role = input("What class would you like your hero to be: Rogue, Warrior, Mage?\n" )

  hero = classes.Player(hero_name, hero_role)
  while hero.health > 0:
    enemy = classes.Enemy()
    print(f"{enemy.name} has come from the forest before you to fight!")
    while enemy.health > 0 and hero.health > 0 and enemy.leaving == 0:
      turn_count = 0
      hero_move = 1
      while hero_move != 0:
        print(f"{hero.name} has {hero.health} health left!")        
        hero_input = input("What would you like to do: Attack, Use Items, or See hero stats?\n")
        if hero_input == "Attack":
          hero.hero_attack(enemy)
          hero_move = 0
        if hero_input == "Use Items":
          hero.hero_items()
          hero_move = 0
        if hero_input == "See hero stats":
          hero.__repr__()
          hero_move = 1
      if enemy.health > 0:
        enemy_move = random.randint(1, 100)
        if enemy_move < 6:
          enemy.tell_enemy_your_tale(hero)
        elif enemy_move < 20:
          enemy.sleep()
        else:
          enemy.enemy_attack(hero)
      else:
        print(f"{enemy.name} has been defeated!")
        classes.Enemy.defeated += 1
      print("-------------------------------------------------------------------------------------------------")
  continue_input = input("Oh no your hero has died... Would you like to find a new hero and continue? (Yes or No)\n")
  if continue_input == "Yes":
    give_it_a_try = 0
    print(f"{hero.name} defeated {classes.Enemy.defeated} enemies!")
    classes.Enemy.defeated = 0

  else:
    give_it_a_try = 1
    print(f"{hero.name} defeated {classes.Enemy.defeated} enemies!")
    print("Have a great day adventurer!")