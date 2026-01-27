def inventory():
    items = input("do you want to view armor(1) weapons(2) or items (3)")




inventory = {
    "Armor":{"leather": {"Defense": 4}, "iron": {"Defense": 6}, "Diamond": {"Defense": 8}},
    "Weapons":{"sword": {"damage": 5}, "axe": {"Damage": 7}, ""},
    "Items": {}
}

for key, value in inventory.items():
    print(f"{key}: {value}")