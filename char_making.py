#EMH
import sys as s
import time as t
import secrets

def typing(text, delay=0.03):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)

def main():
    typing("Welcome to the character maker!")
    name = input("Please enter the name of you character\n")
    classes = ["Warrior", "rogue", "mage", "cleric"]
    weapons = {"longsword": 10,
               "dagger": 6,
               "rock": 12,
               "spear": 8,
               "small dinky hammer": 12}
    