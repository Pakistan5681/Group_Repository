import pakistans_functions as pf

#--- Character Stats ---
# All character stats are referenced by name

stats = {}

def menu():
    print("1. Adjust Stats")
    print("2. Create Character")
    print("3. Adjust Character Inventory")
    print(" ")
    action = pf.idiot_proof_num_range("Type the number of the desired option", 1, 3)

    match action:
        case 1:
            adjust_stats()
        case 2:
            create_character()
        case 3:
            manage_inventory()
        case _:
            raise Exception("Something horrendous has occured. If you are recieving this message, we are cooked")
        
def adjust_stats():
    pass

def create_character():
    pass

def manage_inventory():
    pass