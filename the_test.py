#CAUTION! TEST! NOT USABLE FOR FINAL PROJECT, PROBABLY
print("Starting Skill System Tests")

# Setup test characters
test_warrior = {
    "name": "Ken",
    "class": "Warrior",
    "level": 1,
    "stats": {"strength": 10, "dexterity": 8, "intelligence": 5},
    "skills": set()
}

test_mage = {
    "name": "Elijah",
    "class": "Mage",
    "level": 1,
    "stats": {"strength": 5, "dexterity": 5, "intelligence": 15},
    "skills": set()
}

print("\nTesting")
give_starter_skills(test_warrior)
print(f"{test_warrior['name']} skills: {test_warrior['skills']}")


# Test 2: can_unlock_skill
print("\nTesting can_unlock_skill")
# Expected: False (Level requirement fails)
can_whirlwind_lvl1 = can_unlock_skill(test_warrior, "Whirlwind")
print(f"Can {test_warrior['name']} unlock Whirlwind at Lvl 1? {can_whirlwind_lvl1}")

test_warrior["level"] = 5 
# Expected: True (Now meets Lvl 5 and Prereq Power Strike)
can_whirlwind_lvl5 = can_unlock_skill(test_warrior, "Whirlwind")
print(f"Can {test_warrior['name']} unlock Whirlwind at Lvl 5? {can_whirlwind_lvl5}")


# Test 3: unlock_skill
print(f"Skills before unlock attempt: {test_warrior['skills']}")
# Expected: True, and "Whirlwind" added to skills
unlocked_whirlwind = unlock_skill(test_warrior, "Whirlwind")
print(f"Did Whirlwind unlock successfully? {unlocked_whirlwind}")
print(f"Skills after unlock attempt: {test_warrior['skills']}")


give_starter_skills(test_mage)
test_mage["level"] = 5
print(f"{test_mage['name']} skills before milestone check: {test_mage['skills']}")
# Expected: gained_skills = ['Fireball']
gained_skills = unlock_level_milestone_skills(test_mage)
print(f"Skills gained automatically: {gained_skills}")
print(f"Skills after milestone check: {test_mage['skills']}")




