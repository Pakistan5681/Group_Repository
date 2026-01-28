# function for build_skill_data
# Make a set for warrior skills
# Make a set for rogue skills
# Make a set for mage skills
# Make a set for cleric skills 


#CAUTION TEST
# Sample character data for testing

# Make a dictionary that stores information for each skill 
# For every skill, write down the class, minimum level, required stats, etc. 
 
# Make a dictionary that stores a set of skills for each character 


warrior_skills = {"Power Strike", "Shield Block", "Whirlwind", "Battle Cry"}
rogue_skills   = {"Backstab", "Lockpick", "Evasion", "Shadow Step"}
mage_skills    = {"Magic Missile", "Arcane Focus", "Mana Surge", "Fireball"}
cleric_skills  = {"Heal", "Smite", "Divine Shield", "Greater Heal"}


skill_data = {
    # Warrior Skills
    "Power Strike": {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"strength": 5}},
    "Shield Block": {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 4}},
    "Battle Cry":   {"class": "Warrior", "min_level": 1, "prereq": set(), "required_stats": {"strength": 4}}, 
    "Whirlwind":    {"class": "Warrior", "min_level": 5, "prereq": {"Power Strike"}, "required_stats": {"strength": 10}},

    # Rogue Skills
    "Backstab":     {"class": "Rogue", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 5}},
    "Lockpick":     {"class": "Rogue", "min_level": 1, "prereq": set(), "required_stats": {"dexterity": 4}},
    "Evasion":      {"class": "Rogue", "min_level": 4, "prereq": set(), "required_stats": {"dexterity": 8}},
    "Shadow Step":  {"class": "Rogue", "min_level": 5, "prereq": set(), "required_stats": {"dexterity": 10}},

    # Mage Skills
    "Magic Missile":{"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 5}},
    "Arcane Focus": {"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 4}},
    "Mana Surge":   {"class": "Mage", "min_level": 1, "prereq": set(), "required_stats": {"intelligence": 6}},
    "Fireball":     {"class": "Mage", "min_level": 5, "prereq": {"Magic Missile"}, "required_stats": {"intelligence": 10}},

    # Cleric Skills
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


# function to ensure character skill set 
# If the character does not already have a skill set 
# Create an empty set for them 
def ensure_skill_set(character):
    if "skills" not in character:
        character["skills"] = set()

# Make sure the character has a skill set
# Read the character class and level
# for each skill in that class skill set
# If the skill requires level one
# Add it to the character’s skill set

def give_starter_skills(character):
    ensure_skill_set(character)
    for s in class_skills.get(character["class"], set()):
        if skill_data[s]["min_level"] == 1:
            character["skills"].add(s)

# function for can_unlock_skill(?)
# read the character class, level, and stats
# read the skill’s information from the skill data

# if the character class does not match the skill class(5,10,15,20), return false
# if the character level is lower than the required level, return false
# for each required stat
# if the character stat is lower, return false
# for each prerequisite skill
# if the character does not already know it, return false
# return true

def can_unlock_skill(character, skill):
    info = skill_data[skill]
    if character["class"] != info["class"]:
        return False
    if character["level"] < info["min_level"]:
        return False
    for p in info["prereq"]:
        if p not in character["skills"]:
            return False
    return True

# function for unlock_skill
# ensure the character has a skill set
# if the character already knows the skill, stop
# if the characcter meets all skill requirements
# add the skill to the character skill set

def unlock_skill(character, skill):
    ensure_skill_set(character)
    if skill in character["skills"]:
        return False
    if can_unlock_skill(character, skill):
        character["skills"].add(skill)
        return True
    return False

# function for unlock_level_milestone_skills
# this runs whhen a character levels up
# if the character level is 5 or 10 or 15 or 20
# look at all skills in the character’s class skill set
# for each skill that require s that level
# unlock it automatically if the reqquirements are met

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

# function get_unlockable_skills
# make an empty list
# read the character class
# for each skill in that class skill set
# if the character does not have it
# if the character meets the requirements
# add it to the list
# return the list

def get_unlockable_skills(character):
    ensure_skill_set(character)
    result = []
    for s in class_skills[character["class"]]:
        if s not in character["skills"] and can_unlock_skill(character, s):
            result.append(s)
    return result

# Function for the skill_menuu
# show the character’s current skills
# get the unlockable skills list
# if the list is empty, stop
# show the unlockable skills
# let the user choose one
# if a skill is chosen, unlock it

def skill_menu(character):
    ensure_skill_set(character)
    print("Current skills:", character["skills"])
    op = get_unlockable_skills(character)
    if not op:
        print("No unlockable skills")
        return
    
# after character creation, run give starter skills
# after a character levels up, run unlock level milestone skills
# after that, allow the user to open the skill menu for optional skill





#CAUTION! TEST! NOT USABLE FOR FINAL PROJECT
print("Starting Skill System Tests")

# Setup test characters
test_warrior = {
    "name": "Ken",
    "class": "Warrior",
    "level": 1,
    "stats": {"strength": 10, "dexterity": 8, "intelligence": 5}
}

test_mage = {
    "name": "Elijah",
    "class": "Mage",
    "level": 1,
    "stats": {"strength": 5, "dexterity": 5, "intelligence": 15}
}

# --- Test 1: give_starter_skills ---
print("\nTesting")
give_starter_skills(test_warrior)
# Expected: {'Shield Block', 'Power Strike'}
print(f"{test_warrior['name']} skills: {test_warrior['skills']}")


# --- Test 2: can_unlock_skill ---
print("\n--- Testing can_unlock_skill ---")
# Expected: False (Level requirement fails)
can_whirlwind_lvl1 = can_unlock_skill(test_warrior, "Whirlwind")
print(f"Can {test_warrior['name']} unlock Whirlwind at Lvl 1? {can_whirlwind_lvl1}")

test_warrior["level"] = 5 
# Expected: True (Now meets Lvl 5 and Prereq Power Strike)
can_whirlwind_lvl5 = can_unlock_skill(test_warrior, "Whirlwind")
print(f"Can {test_warrior['name']} unlock Whirlwind at Lvl 5? {can_whirlwind_lvl5}")


# --- Test 3: unlock_skill ---
print("\n--- Testing unlock_skill ---")
print(f"Skills before unlock attempt: {test_warrior['skills']}")
# Expected: True, and "Whirlwind" added to skills
unlocked_whirlwind = unlock_skill(test_warrior, "Whirlwind")
print(f"Did Whirlwind unlock successfully? {unlocked_whirlwind}")
print(f"Skills after unlock attempt: {test_warrior['skills']}")


# --- Test 4: unlock_level_milestone_skills (Mage example) ---
print("\n--- Testing unlock_level_milestone_skills ---")
give_starter_skills(test_mage)
test_mage["level"] = 5
print(f"{test_mage['name']} skills before milestone check: {test_mage['skills']}")
# Expected: gained_skills = ['Fireball']
gained_skills = unlock_level_milestone_skills(test_mage)
print(f"Skills gained automatically: {gained_skills}")
print(f"Skills after milestone check: {test_mage['skills']}")
