import random
from pathlib import Path
import json
import os

class Player:
  
  def __init__(self, input_name, input_role):
    self.items = {}
    with open("lib\items.json") as f:
        items = json.load(f)
        for key in items.values():
           for key1, value1 in key.items():
            self.items[key1] = value1
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
      print(self.items)
      # print(f"{item}: {self.items[item]}")
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
  
  defeated = 0

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
      print(f"{self.name} wishes to tell you their story!")
      filepath = Path(__file__).parent/"Lord_Farquad.txt"
      with open(filepath) as f:
        n = 0
        for i in f:
            print(i.strip("\n"))
            n+= 1
            if n == 2:
                cont = input("Do you care to continue hearing their story? (Yes or No) ")
                if cont == "Yes":
                    self.leaving = 1
                else:
                    print(f"{self.name} smirks.")
                    break
    elif character == "Dog, Kell of Barkus":
      print(f"{self.name} wishes to tell you their story!")
      filepath = Path(__file__).parent/"Dog.txt"
      with open(filepath) as f:
        n = 0
        for i in f:
            print(i.strip("\n"))
            n+= 1
            if n == 2:
                cont = input("Do you care to continue hearing their story? (Yes or No) ")
                if cont == "Yes":
                    self.leaving = 1
                else:
                    print(f"{self.name} whines.")
                    break
    elif character == "The Metal, Vessel of Hell":
      print(f"{self.name} wishes to tell you their story!")
      filepath = Path(__file__).parent/"The_Metal.txt"
      with open(filepath) as f:
        n = 0
        for i in f:
            print(i.strip("\n"))
            n+= 1
            if n == 2:
                cont = input("Do you care to continue hearing their story? (Yes or No) ")
                if cont == "Yes":
                    self.leaving = 1
                else:
                    print(f"{self.name} giggles.")
                    break
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