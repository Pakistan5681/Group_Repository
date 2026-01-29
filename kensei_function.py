#KH 2nd skills
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

