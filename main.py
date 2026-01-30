import pakistans_functions as pf
import time as t
import random as r

#Character Stats
# All character stats are referenced by name
stats = {"John Test III": {'strength': 9, 'dexterity': 9, 'constitution': 15, 'intelligence': 15, 'charisma': 12, 'wisdom': 16, 'armor class': 7, 'xp': 0, 'weapon': 12, 'class': 'mage', 'race': 'elf'}}
names = ["John Test III"]

inventories = {}

warrior_skills = {"Power Strike", "Shield Block", "Whirlwind", "Battle Cry"}
rogue_skills   = {"Backstab", "Lockpick", "Evasion", "Shadow Step"}
mage_skills    = {"Magic Missile", "Arcane Focus", "Mana Surge", "Fireball"}
cleric_skills  = {"Heal", "Smite", "Divine Shield", "Greater Heal"}
skill_data = {
    "Power Strike": {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"strength": 5}},
    "Shield Block": {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 4}},
    "Battle Cry":   {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"strength": 4}}, 
    "Whirlwind":    {"class": "Warrior", "min_level": 5, "prereq": {"Power Strike"}, "required_stats": {"strength": 10}},
    "Backstab":     {"class": "Rogue", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 5}},
    "Lockpick":     {"class": "Rogue", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 4}},
    "Evasion":      {"class": "Rogue", "min_level": 4, "prereq": set(), "required_stats": {"dexterity": 8}},
    "Shadow Step":  {"class": "Rogue", "min_level": 5, "prereq": set(), "required_stats": {"dexterity": 10}},
    "Magic Missile":{"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 5}},
    "Arcane Focus": {"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 4}},
    "Mana Surge":   {"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 6}},
    "Fireball":     {"class": "Mage", "min_level": 5, "prereq": {"Magic Missile"}, "required_stats": {"intelligence": 10}},
    "Heal":         {"class": "Cleric", "min_level": 1, "prereq": set(), "required_stats": {"piety": 5}},
    "Smite":        {"class": "Cleric", "min_level": 1, "prereq": set(), "required_stats": {"piety": 4}},
    "Divine Shield":{"class": "Cleric", "min_level": 5, "prereq": set(), "required_stats": {"piety": 10}},
    "Greater Heal": {"class": "Cleric", "min_level": 5, "prereq": {"Heal"}, "required_stats": {"piety": 12}},
}
class_skills = {
    "Warrior": warrior_skills,
    "Rogue": rogue_skills,
    "Mage": mage_skills,
    "Cleric": cleric_skills,
}

xp_requirements = {
    1: 100,
    2: 200,
    3: 400, 
    4: 800,
    5: 1600,
    6: 2500,
    7: 3600,
    8: 5000,
    9: 6500,
    10: 8000,
    11: 10000,
    12: 12500,
    13: 14500,
    14: 17000,
    15: 20000,
    16: 23500,
    17: 27500,
    18: 32500,
    19: 40000,
    20: 50000,
    21: 62500,
    22: 77500,
    23: 97500,
    24: 130000,
    25: 175000,
    26: 250000,
    27: 325000,
    28: 425000,
    29: 555000,
    30: 700000
}

def menu():
    print("1. Adjust Stats")
    print("2. Create Character")
    print("3. Adjust Character Inventory")
    print(" ")
    action = pf.idiot_proof_num_range("Type the number of the desired option ", 1, 3)

    match action:
        case 1:
            adjust_stats()
        case 2:
            char_name, stats[char_name] = create_character()
            print(stats[char_name])
        case 3:
            manage_inventory(names)
        case _:
            raise Exception("Something horrendous has occured. If you are recieving this message, we are cooked")
        


def adjust_stats():
    character = pf.idiot_proof_specific("What characters stats do you want to adjust", names, "You dont have a character with that name")
    stat_to_change = pf.idiot_proof_specific("What stat do you want to adjust?\n'xp' or 'weapon' ", ["xp", "weapon"], "Thats not a valid stat")

    if stat_to_change == "xp":
        level = stats[character]["level"]
        xp = stats[character]["xp"]
        xp_to_add = pf.idiot_proof_general(f"How much xp do you want to add to {character}? ")

        xp += xp_to_add

        if xp > xp_requirements[level]:
            stats[character]["xp"] -= xp_requirements[level]
            stats[character]["level"] += 1

#KH 2nd skills

def ensure_skill_set(character):
    if "skills" not in character:
        character["skills"] = set()

def give_starter_skills(character):
    ensure_skill_set(character)
    for s in class_skills.get(character["class"], set()):
        if skill_data[s]["min_level"] == 1:
            character["skills"].add(s)

def can_unlock_skill(character, skill):
    ensure_skill_set(character)
    info = skill_data[skill]

    if character["class"] != info["class"]:
        return False
    if character["level"] < info["min_level"]:
        return False
    
    for stat, req in info["required_stats"].items():
        if character["stats"].get(stat, 0) < req:
            return False
    
    for p in info["prereq"]:
        if p not in character["skills"]:
            return False
    return True

def unlock_skill(character, skill):
    ensure_skill_set(character)
    if skill in character["skills"]:
        return False
    if can_unlock_skill(character, skill):
        character["skills"].add(skill)
        return True
    return False

def unlock_level_milestone_skills(character):
    ensure_skill_set(character)
    gained = []
    if character["level"] in {5, 10, 15, 20}:
        for s in class_skills[character["class"]]:
            if skill_data[s]["min_level"] == character["level"]:
                if can_unlock_skill(character, s):
                    character["skills"].add(s)
                    gained.append(s)
    return gained

def get_unlockable_skills(character):
    ensure_skill_set(character)
    result = []
    for s in class_skills[character["class"]]:
        if s not in character["skills"] and can_unlock_skill(character, s):
            result.append(s)
    return result


def skill_menu(character):
    ensure_skill_set(character)
    print("Current skills:", character["skills"])
    op = get_unlockable_skills(character)
    if not op:
        print("No unlockable skills")
        return
    
    for i, s in enumerate(op, 1):
        print(i, s)

    choice = input("Choose a skill number (Enter to cancel): ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(op):
            if unlock_skill(character, op[index]):
                print("Unlocked:", op[index])


def create_character():
    pass



def manage_inventory(names):
    def inventory(name1):
        global xpn

        # create inventory if character does not exist
        if name1 not in inventories: #create a inventory FOr the charachter
            inventories[name1] = {
                "weapons": {},
                "armor": {},
                "items": {}
            }

        inv = inventories[name1]

        choice = pf.idiot_proof_specific("Add item (1), View inventory (2), Sell item (3): ", ["1", "2", "3"])
        # ADD ITEM
        if choice == "1":
            category = input("Category (weapons / armor / items): ").lower()

            if category != "weapons" and category != "armor" and category != "items":
                print("Invalid category") #check if the category is "valid"
                return

            item_name = input("Item name: ") #actually add item
            value1 = int(input("Item vlalue: "))


            inv[category][item_name] = value1 #use itme name and value
            print(item_name, "added to", name1, category)

        # VIEW INVENTORY
        elif choice == "2":
            print("/n", name1, "Inventory")
            for category in inv:
                print("", category.capitalize())

                if len(inv[category]) == 0:
                    print("Empty")
                else:
                    for item in inv[category]:
                        print(item, ":", inv[category][item])

        # SELL ITEM (ItEMS ONLY)
        elif choice == "3":
            if len(inv["items"]) == 0:
                print("No items to sEll")
                return

            print("Items:")
            for item in inv["items"]:
                print(item, ":", inv["items"][item])

            sell_item = input("Item to sell: ")

            if sell_item in inv["items"]:
                xp += inv["items"][sell_item]
                del inv["items"][sell_item]
                print("Item sold")
                print("Total XP:", xp)
            else:
                print("Item si not found")

        else:
            print("Invalid option, try again")
            return

    if bool(names):
        character_to_adjust = pf.idiot_proof_specific("What characters inventory do you want to adjust? ", names, "you dont have a character with that name")
        inventory(character_to_adjust)

    #easy wy to use thic can be: 
    ''' new_character = input("Enter new character name: ")
    inventory(new_character)'''

    '''characters[name] = {"hp": 100, "xp": 0}'''

#EMH


def create_character():
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
    races = ["human", "elf", "half-orc", "kratos"]
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

    return name, {"strength": stren, "dexterity": dex, "constitution": cons, "intelligence": intell, "charisma": rizz, "wisdom": wis, "armor class": ac, "xp": 0, "weapon": weap, "class": choice1, "race": choice2}

menu()