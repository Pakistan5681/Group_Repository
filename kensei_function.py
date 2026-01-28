# function for build_skill_data
# Make a set for warrior skills
# Make a set for rogue skills
# Make a set for mage skills
# Make a set for cleric skills 
 
# Make a dictionary that stores information for each skill 
# For every skill, write down the class, minimum level, required stats, etc. 
 
# Make a dictionary that stores a set of skills for each character 


warrior_skills = {"Power Strike", "Shield Block", "Whirlwind", "Battle Cry"}
rogue_skills   = {"Backstab", "Lockpick", "Evasion", "Shadow Step"}
mage_skills    = {"Magic Missile", "Arcane Focus", "Mana Surge", "Fireball"}
cleric_skills  = {"Heal", "Smite", "Divine Shield", "Greater Heal"}


skill_data = {
"Power Strike": {"class": "Warrior", "min_level": 1, "prereq": set()},
    "Shield Block": {"class": "Warrior", "min_level": 1, "prereq": set()},
    "Whirlwind":    {"class": "Warrior", "min_level": 5, "prereq": {"Power Strike"}},

    "Backstab":     {"class": "Rogue", "min_level": 1, "prereq": set()},
    "Lockpick":     {"class": "Rogue", "min_level": 1, "prereq": set()},
    "Evasion":      {"class": "Rogue", "min_level": 4, "prereq": set()},

    "Magic Missile":{"class": "Mage", "min_level": 1, "prereq": set()},
    "Fireball":     {"class": "Mage", "min_level": 5, "prereq": {"Magic Missile"}},

    "Heal":         {"class": "Cleric", "min_level": 1, "prereq": set()},
    "Greater Heal": {"class": "Cleric", "min_level": 5, "prereq": {"Heal"}},
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


