# store inventories for all characters
inventories = {}

# XP counter
xp = 0

def inventory(name1):
    global xp

    # create inventory if character does not exist
    if name1 not in inventories: #create a inventory FOr the charachter
        inventories[name1] = {
            "weapons": {},
            "armor": {},
            "items": {}
        }

    inv = inventories[name1]

    choice = input("Add item (1), View inventory (2), Sell item (3): ")




    # ADD ITEM
    if choice == "1":
        category = input("Category (weapons / armor / items): ").lower()

        if category != "weapons" and category != "armor" and category != "items":
            print("Invalid category") #check if the category is "valid"
            return

        item_name = input("Item name: ") #actually add item
        value1 = int(input("Item vlalue: For weapons calue is damage for armor its defense for items its xp value: "))


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

        sell_item = input("Item to rell: ")

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



#easy wy to use thic can be: 
''' new_character = input("Enter new character name: ")
inventory(new_character)'''

'''characters[name] = {"hp": 100, "xp": 0}'''
