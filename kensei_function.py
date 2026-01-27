# function for build_skill_data                                                                                              
# Make a set for warrior skills                                                                                              
# Make a set for rogue skills                                                                                              
# Make a set for mage skills                                                                                              
# Make a set for cleric skills                                                                                              
                                                                                              
# Make a dictionary that stores information for each skill                                                                                              
# For every skill, write down the class, minimum level, required stats, etc.                                                                                              
                                                                                              
# Make a dictionary that stores a set of skills for each character                                                                                              
                                                                                              
# function to ensure character skill set                                                                                              
# If the character does not already have a skill set                                                                                              
# Create an empty set for them                                                                                              
                                                                                              
# function for give_starter_skills                                                                                              
# Make sure the character has a skill set                                                                                              
# Read the character class and level                                                                                              
# for each skill in that class skill set                                                                                              
# If the skill requires level one                                                                                              
# Add it to the character’s skill set                                                                                              
                                                                                              
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
                                                                                              
# function for unlock_skill                                                                                              
# ensure the character has a skill set                                                                                              
# if the character already knows the skill, stop                                                                                              
# if the characcter meets all skill requirements                                                                                              
# add the skill to the character skill set                                                                                              
                                                                                              
# function for unlock_level_milestone_skills                                                                                              
# this runs whhen a character levels up                                                                                              
# if the character level is 5 or 10 or 15 or 20                                                                                              
# look at all skills in the character’s class skill set                                                                                              
# for each skill that require s that level                                                                                              
# unlock it automatically if the reqquirements are met                                                                                              
                                                                                              
# function get_unlockable_skills                                                                                              
# make an empty list                                                                                              
# read the character class                                                                                              
# for each skill in that class skill set                                                                                              
# if the character does not have it                                                                                              
# if the character meets the requirements                                                                                              
# add it to the list                                                                                              
# return the list                                                                                              
                                                                                              
# Function for the skill_menuu                                                                                              
# show the character’s current skills                                                                                              
# get the unlockable skills list                                                                                              
# if the list is empty, stop                                                                                              
# show the unlockable skills                                                                                              
# let the user choose one                                                                                              
# if a skill is chosen, unlock it                                                                                              
                                                                                              
# integration                                                                                              
# after character creation, run give starter skills                                                                                              
# after a character levels up, run unlock level milestone skills                                                                                              
# after that, allow the user to open the skill menu for optional skill


