def inventory():
    items = input("do you want to view armor(1) weapons(2) or items (3)")


"""weapons = {

}

armor = {

}

items = {

}"""

inventory = {
    "Armor":{},
    "Weapons":{},
    "Items": {}
}

for key, value in weapons.items():
    print(f"{key}: {value}")




inventory = {"weapons": {}, "armor": {}, "items": {}}

category = input("Enter category (weapons/armor/items): ")
name = input("Enter item name: ")
damage = input("Enter damage value: ")

# This adds the item directly to the nested dictionary chosen by the user
inventory[category][name] = {"damage": damage}


#seperate
found_loot = {"Iron Sword": {"damage": 10, "weight": 5}}

# Assigning the variable from the loot dict to the inner 'weapons' dict
weapon_name = "Iron Sword"
inventory["weapons"][weapon_name] = found_loot[weapon_name]