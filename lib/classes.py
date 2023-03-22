import random

class Player:
  
  def __init__(self, input_name, input_role):
    self.items = {"Healing Potion": 3}
    self.damage = 15
    self.name = input_name
    if input_role == "Rogue":
      self.role = "Rogue"
      self.attack = 120
      self.health = 90
      self.magic_power = 15
    elif input_role == "Warrior":
      self.role = "Warrior"
      self.attack = 90
      self.health = 100
      self.magic_power = 15
    elif input_role == "Mage":
      self.role = "Mage"
      self.attack = 50
      self.health = 75
      self.magic_power = 150

  def __repr__(self):
    stats = f"{self.name} is a {self.role} with {self.health} health, {self.attack} attack, and {self.magic_power} magic power."
    print(stats)

  def hero_attack(self, enemy):
    if self.role == "Rogue":
      damage = int((self.damage * (self.attack / 100)))
      print(f"{self.name} hit {enemy.name} for {damage} damage!")
      enemy.health = (enemy.health - damage)
    if self.role == "Warrior":
      damage = int(self.damage * (self.attack / 100))
      print(f"{self.name} hit {enemy.name} for {damage} damage!")
      enemy.health = (enemy.health - damage)
    if self.role == "Mage":
      damage = int((self.damage * (self.magic_power / 100)))
      print(f"{self.name} hit {enemy.name} for {damage} damage!")
      enemy.health = (enemy.health - damage)

  def hero_items(self):
    for item in self.items:
      print(f"{item}: {self.items[item]}")
    item_to_use = input("Please pick an item to use:\n")
    if item_to_use == "Healing Potion" and self.items[item] > 0:
      self.health += 50
      print("Your health went up by 50")
      self.items["Healing Potion"] = self.items["Healing Potion"] - 1
    else:
      print("Oh no, you have no Healing Potions left!")

  def stats(self):
    self.__repr__()

class Enemy:
  
  def __init__(self):
    random_name = random.randint(2, 4)
    #if random_name == 0:
      #self.name = "Corn Flakis, Kell of Ogs"
    #elif random_name == 1:
      #self.name = "Gibble, The Taken Hand"
    if random_name == 2:
      self.name = "Lord Farquad, The Short King"
    elif random_name == 3:
      self.name = "Dog, Kell of Barkus"
    elif random_name == 4:
      self.name = "The Metal, Vessel of Hell"
    #elif random_name == 5:
      #self.name = ""
    #elif random_name == 6:
      #self.name = ""
    #elif random_name == 7:
      #self.name = ""
    self.health = random.randint(1, 100)
    self.damage = random.randint(1, 15)
    self.leaving = 0
    
  def __repr__(self):
    character = self.name
    #if character == "Corn Flakis, Kell of Ogs":
      #print("")
      #print("")
      #cont.input("Do you care to continue hearing their story? (Yes or No)")
      #if cont == "Yes":
        #print("")
        #print("")
        #print("Thank you for listening to my story, adventurer. For now I will retreat but I leave you with this:")
      #else:
        #continue
    #elif character == "Gibble, The Taken Hand":
      #print("")
      #print("")
      #cont.input("Do you care to continue hearing their story? (Yes or No)")
      #if cont == "Yes":
        #print("")
        #print("")
        #print("Thank you for listening to my story, adventurer. For now I will retreat but I leave you with this:")
      #else:
        #continue
    if character == "Lord Farquad":
      print("When I was a young lad my height caused laughter")
      print("I spent my young adult years wearing false legs and collecting loyal servants")
      cont = input("Do you care to continue hearing their story? (Yes or No)")
      if cont == "Yes":
        print("My fortress was built and gained success in the kingdom")
        print("Now that I am rich I must catfish myself a tall, beautiful princess to marry")
        print("Thank you peasant for listening to my story. I leave you with this:")
        self.leaving = 1
      else:
        print(f"{self.name} smirks.")
    elif character == "Dog, Kell of Barkus":
      print("Bark")
      print("Bark")
      cont = input("Do you care to continue hearing their story? (Yes or No)")
      if cont == "Yes":
        print("Bark")
        print("Lick")
        self.leaving = 1
      else:
        print(f"{self.name} whines.")
    elif character == "The Metal, Vessel of Hell":
      print("Many foes sought my demise, many tried to kill me; but I cannot die.")
      print("They attempted to dethrone an immortal king.")
      cont = input("Do you care to continue hearing their story? (Yes or No)")
      if cont == "Yes":
        print("But they failed, as they were stricken down to the ground.")
        print("No one can destroy The Metal.")
        print("Thank you for listening to my story, adventurer. For now I will retreat but I leave you with this:")
        self.leaving = 1
      else:
        print(f"{self.name} giggles.")
    #elif character == 
    #elif character == 
    #elif character == 
    #elif character == 
  
  def enemy_attack(self, enemy):
    print(f"{self.name} decided to attack!")
    print(f"{self.name} hit {enemy.name} for {self.damage} damage!")
    enemy.health = enemy.health - self.damage

  def sleep(self):
    print(f"{self.name} decided the best choice to take right now was take a nap?")
    print(f"{self.name} healed some health!")
    self.health += (self.health / 2)

  def tell_enemy_your_tale(self, enemy):
    decision = self.__repr__()