#EMH
import time as t
import random as r

def main():
    print("Welcome to the character maker!")
    t.sleep(1.5)
    stren = r.randint(5,20)
    cons = r.randint(5,20)
    dex = r.randint(5,20)
    intell = r.randint(5,20)
    rizz = r.randint(5,20)
    wis = r.randint(5,20)
    ac = r.randint(5,20)
    name = input("Please enter the name of your character!\n")
    t.sleep(1.5)
    inventory = {}
    classes = ["warrior", "rogue", "mage", "cleric"]
    weapons = {"longsword": 10,
               "dagger": 6,
               "rock": 12,
               "spear": 8,
               "small dinky hammer": 12}
    races = ["human", "elf", "half-orc", "more to come"]
    print("This is the list of classes!")
    t.sleep(1.5)
    for x in classes:
        print(x)
    t.sleep(1.5)
    while True:
        choice1 = input("Now choose your class!\n").strip().lower()
        t.sleep(1.5)
        if choice1 in classes:
            print(f"You have chosen {choice1}!")
            if choice1 == "warrior":
                dex += 3
                break
            elif choice1 == "rogue":
                wis += 3
                intell -= 3
                break
            elif choice1 == "mage":
                stren += 2
                break
            elif choice1 == "cleric":
                rizz += 3
                break
        else:
            print("That ain't a class!")
    t.sleep(1.5)
    print("Here is the list of races!")
    t.sleep(1.5)
    for x in races:
        print(x)
    t.sleep(1.5)
    while True:
        choice2 = input("Now, what race will you choose?\n").strip().lower()
        if choice2 in races:
            print(f"You have chosen {choice2}!")
            break
        else:
            print("That ain't an option!")
    t.sleep(1.5)
    print("Now finally for your weapon!")
    t.sleep(1.5)
    for x in weapons:
        print(x)
    t.sleep(1.5)
    while True:
        choice3 = input("Which one shall you choose?\n").strip().lower()
        if choice3 in weapons.keys():
            print(f"You have chosen {choice3}!")
            t.sleep(1.5)
            print("It will now be added to your inventory.")
            weap = weapons[choice3]
            inventory[choice3] = weap
            break
    t.sleep(1.5)
    print("Now you have made your basic character!")
    t.sleep(1.5)
    print(f"Here are your final stats!\nStrength is {stren}\nDexterity is {dex}\nConstitution is {cons}\nIntelligence is {intell}\nCharisma is {rizz}\nWisdom is {wis}\nArmor Class is {ac}")
main()