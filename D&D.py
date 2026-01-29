import random as r
import time as t
import sys as s

def typing(text, delay=0.03):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)

    print()
gold = 50
inventory = {}
def show_inventory():
    print("These are your items!")
    for item in inventory.keys():
        typing(item)
value5 = 0
def combat(m_health, m_damage, health, gold_given):
    global gold
    global value5
    typing("Now you are fighting your opponent")
    damage = value3
    while True:
        atk = input("What would you like to do?\n Use a heal potion\n attack,\n or flee?\n").lower()
        if atk == "attack":
            show_inventory()
            hit = input("Alrighty, what would you like to use in your inventory to attack?\n").lower()
            if hit in inventory:
                user = inventory[hit]
                typing(f"You chose to use {hit}!")
                typing(f"You did {user} damage!")
                m_health -= user
            else:
                typing("You dont have that! He attacks anyways!")
        elif atk == "heal potion":
            if "heal potion" in inventory:
                typing(f"You healed 80% of your health! Also potentially gained some!")
                health *= 1.60
            else:
                typing("You don't have a healing potion")
        elif atk == "flee":
            typing("You successfully fleed!")
            break
        else:
            typing("You can't fight with that!")
        typing("Now it is the opponent's turn!")
        mon_attempt = r.randint(5,25)
        if mon_attempt >= ac:
            typing(f"You took {m_damage} damage!")
            health -= m_damage
            typing(f"Your health is now {health}")
        else:
            typing("Your opponent did not hit!")
        if health <= 0:
            typing("You died! You lose some gold!")
            if gold <= gold_given:
                gold -= gold
            elif gold > gold_given:
                gold -= gold_given
            break
        if m_health <= 0:
            typing(f"You won against your opponent! You gain {gold_given} gold!")
            gold += gold_given
            value5 += 1
            break
value9 = 0
def belville():
    global value9
    if value9 >= 1:
        typing("Seems you have went through this town!")
        t.sleep(1.5)
        typing("Now go to another town to defeat their military general!")
        return False
    global gold
    typing("After a long trek, you finally make your way to Belville, a once normal looking town has turned to something... deserted and destroyed.")
    t.sleep(0.5)
    typing("You hear someone come up behind, you get scared, thinking of the worst, when you turn around...")
    t.sleep(1.5)
    typing("It's just a dealer, but he seems to have something good in his wagon...")
    shop()
    t.sleep(1.5)
    typing("Whether you bought something or not, you go to explore the rest of Belville!")
    while True:
        try:
            act_choice = int(input("What do you want to do?\n1 for going into an abandoned house\n2 for going into a desolate basketball court\n"))
            break
        except ValueError:
            typing("That isn't something you can do!")
    if act_choice == 1:
        typing("You go into the abandoned house...")
        t.sleep(1.5)
        typing("You see a bunch of dusty pictures on the wall, along with destroyed furniture")
        t.sleep(1.5)
        typing("You wonder, why would the Dragon King ever cause something like this to happen to people...")
        t.sleep(1.5)
        typing("Anyways you continue through to the second floor of the house")
        t.sleep(1.5)
        typing("... and you fall through the floor!")
        t.sleep(1.5)
        typing("Luckily you landed on a half broken couch")
        t.sleep(1.5)
        typing("After that, you decide to go out of the house...")
        t.sleep(1.5)
        typing("But when you come out of the house... you run into one of the Dragon King's military generals!")
        combat(30,r.randint(1,10),35,30)
        t.sleep(1.5)
        typing("That was a close one... But you ended up making it out of the town!")
        t.sleep(1.5)
        value9 += 1
    elif act_choice == 2:
        typing("You go into the basketball court, to find an almost fully inflated basketball!")
        t.sleep(1.5)
        typing("You go to shoot into the hoop, you actually make it from across the court!")
        t.sleep(1.5)
        typing("Because of that, you get gold for that fire trickshot!")
        gold += 5
        t.sleep(1.5)
        typing("After the crazy trick that you just did, you venture out of the basketball court")
        typing("... eager to beat the Dragon King once and for all of the country of Draeburg!")
        t.sleep(1.5)
        typing("But just as you thought you were good, you run into one of the military generals of the Dragon King!")
        combat(30,r.randint(1,10),35,30)
        value9 += 1
value6 = 0
def madland():
    global value6
    if value6 >= 1:
        typing("Seems you have went through this town!")
        t.sleep(1.5)
        typing("Now go to another town to defeat their military general!")
        return False
    global gold
    gold *= 2
    typing("You've traveled long and far to this town, but it looks so different compared to any other places...")
    t.sleep(1.5)
    typing("It looks poor and there is no fully built houses any where you look")
    t.sleep(1.5)
    typing("Then you realize, you're in the town of the poor in Draeburg.")
    t.sleep(1.5)
    while True:
        path = input("Now what would you like to do in the town of madland?\n'give' for giving gold to someone homeless,\n'shop' for going to a shop to see what they have\n or 'fight' for fighting a homeless guy\n").lower().strip()
        if path == "give":
            gift = int(input(f"So you have chosen to give some gold to the homeless, how much would you like to give out of {gold}\n"))
            if gift == 0:
                typing("Wooooow...")
                t.sleep(1.5)
                typing("You gave no gold! Why did you even pick generousity in the first place?")
            elif gift == 1:
                typing("Okay...")
                t.sleep(1.5)
                typing("You only gave 1 gold! Honestly it's good enough.")
                t.sleep(1.5)
                typing("But still, with inflation these days, what is 1 gold gonna get ya!?")
                t.sleep(1.5)
                typing("Hey at least they still appreciate it")
                gold -= 1
                break
            elif gift > 1 and gift <= 10:
                typing("Alrighty the generousity is getting there...")
                t.sleep(1.5)
                typing("Well the homeless definitely thank you for your charitable-ness")
                t.sleep(1.5)
                gold -= gift
                break
            elif gift > 10:
                typing(f"Nice! You gave {gift} gold to the homeless, not too bad!")
                t.sleep(1.5)
                typing("Because of the generousity that you have, in return they give you a rare weapon of your choice!")
                for x in rare_weapons:
                    print(x)
                typing("Those are your choices to chose from")
                t.sleep(1.5)
                w_choice = input("Now what weapon would you like to choose?").lower()
                if w_choice in rare_weapons:
                    chosen_item = rare_weapons[w_choice]
                    inventory[w_choice] = chosen_item
                    typing(f"You officially now have {w_choice}!")
                    t.sleep(1.5)
                    typing("... and that is because of your generousity")
                    break
            elif gift > gold:
                typing("You can't give that much!")
            else:
                typing("You can't give that!")
        elif path == "shop":
            typing("You walk to a shop in the middle of the delapidated town...")
            t.sleep(1.5)
            typing("You walk into the rundown store...")
            shop()
            break
        elif path == "fight":
            typing("So you happen to chose fighting a homeless person")
            t.sleep(1.5)
            typing("Why though?")
            t.sleep(1.5)
            typing("Little do you know, this fighting won't be as easy as you thought...")
            combat(50,r.randint(1,18),35,1)
            typing("Seriously why did you think to do that")
            t.sleep(1.5)
            typing("Anyway...")
        else:
            typing("You can't do that!")
    typing("Whichever one you did, after you did it, you decide to walk down the main street of this town...")
    t.sleep(1.5)
    typing("You suddenly wonder why this town is so rundown")
    t.sleep(1.5)
    typing("But then you see something in the distance")
    t.sleep(1.5)
    typing("It's a general that has heard about you before!")
    t.sleep(1.5)
    typing("He starts to run at you at break-neck speeds, like you've never seen...")
    t.sleep(1.5)
    typing("You start to run, hoping you can escape the inevitable")
    t.sleep(1.5)
    typing("He continues to catch up, and you pray that he doesn't get you")
    t.sleep(1.5)
    typing("Just as he is about to reach you, you do some crazy parkour")
    t.sleep(1.5)
    typing("But he ends up grabbing you in the end, due to him being super tall..")
    t.sleep(1.5)
    typing("Now, all you have left to do is fight.")
    combat(35,r.randint(1,18),25,40)
    t.sleep(1.5)
    typing("Whether you beat him or not, you continue to the next town...")
    gold /= 2
    round(gold)
    value6 += 1
value8 = 0
def rockshield():
    global value8
    global gold
    global strr
    global ac
    if value8 >= 1:
        typing("Seems you have went through this town!")
        t.sleep(1.5)
        typing("Now go to another town to defeat their military general!")
        return False
    typing("You traveled a long way to get to this town...")
    t.sleep(1.5)
    typing("Across a long desert land")
    t.sleep(1.5)
    typing("But as you look...")
    t.sleep(1.5)
    typing("You see green vehicles and artilery in the distance")
    t.sleep(1.5)
    typing("That is when you realize...")
    t.sleep(1.5)
    typing("You've made it to the military town of Draeburg.")
    t.sleep(1.5)
    while True:
        r_choice = input("Now what would you like to do in this town?\n'shop' for buying somethin\n'train' for doing some military training\n'armor' to go get (may or may not rob) some armor\n")
        if r_choice == "shop":
            typing("You walk into an armory, that is dusty, and hot")
            t.sleep(1.5)
            typing("It maybe hot, but it looks like there is something good")
            shop()
            break
        elif r_choice == "train":
            typing("You walk into a public military try out center")
            t.sleep(1.5)
            typing("You see a sergeant, you walk up to him and ask...")
            t.sleep(1.5)
            typing("Can I train?")
            t.sleep(1.5)
            typing("He says, yeah sure!")
            t.sleep(1.5)
            typing("You're surprised that he hasn't noticed who you are yet")
            t.sleep(1.5)
            typing("Then as you're walking to the training area...")
            t.sleep(1.5)
            typing("He says, 'do I know you from somewhere?'")
            t.sleep(1.5)
            typing("You immediately say no")
            t.sleep(1.5)
            typing("He says, 'alrighty' then you continue.")
            t.sleep(1.5)
            typing("You see yourself in the training room...")
            t.sleep(1.5)
            typing("Then the sergeant says to you...")
            typing("GET DOWN AND GIVE ME 25!")
            t.sleep(1.5)
            typing("So you instantly get down and do 25 pushups")
            t.sleep(1.5)
            typing("The sergeant says...")
            t.sleep(1.5)
            typing("'Wow you were fast with that'")
            t.sleep(1.5)
            typing("'Faster than any of my other troops'")
            t.sleep(1.5)
            typing("(Because of that you gain 2 strength!)")
            strr += 5
            t.sleep(1.5)
            typing("'But that means you definitely didn't fool me, adventurer'")
            t.sleep(1.5)
            typing("'Now in order to finish your little quest'")
            t.sleep(1.5)
            typing("'You will have to get through ME!")
            combat(50,r.randint(1,20),30,47)
            break
        elif r_choice == "armor":
            typing("You walk to a store in the middle of the town...")
            t.sleep(1.5)
            typing("Then you see if you can secretly walk out of the store with it!")
            t.sleep(1.5)
            typing("So you grab a chest plate, usually worth 45 gold...")
            t.sleep(1.5)
            typing("...and right before you make it out of the store...")
            t.sleep(1.5)
            typing("You have to roll for stealth!")
            stealth = r.randint(1,20)
            while value < 4:
                typing("Rolling...")
            if stealth <= 10:
                typing("You rolled too low!")
                t.sleep(1.5)
                typing("The store clerk ends up noticing...")
                t.sleep(1.5)
                typing("He immediately comes over")
                t.sleep(1.5)
                typing("He whips out his sword")
                t.sleep(1.5)
                typing("Next thing you know...")
                combat(30,r.randint(1,20),30,23)
                break
            else:
                typing(f"You rolled a {stealth}!")
                t.sleep(1.5)
                typing("You end up making it out with the chest plate!")
                t.sleep(1.5)
                typing("You gain 3 to your armor class!")
                ac += 3
                break
        else:
            typing("That ain't something you can do!")
    typing("Whatever you ended up choosing...")
    t.sleep(1.5)
    typing("You continue through the town, inching closer to the capital")
    t.sleep(1.5)
    typing("You see a huge, strong general with a gun on his belt...")
    t.sleep(1.5)
    typing("He comes up to you and says, you only have me before you reach Drappes!")
    t.sleep(1.5)
    typing("If you can't beat me...")
    t.sleep(1.5)
    typing("Then you will never beat the Dragon King!")
    combat(100,r.randint(1,30),66,100)
    typing("You think, wow that battle was hard...")
    t.sleep(1.5)
    typing("Now you must venture to the next town")
    value8 += 1
value4 = 0
def angousir():
    global value4
    if value4 >= 1:
        typing("Seems you have already went through this town!")
        t.sleep(1.5)
        typing("Now go another town to defeat their military general!")
        return False
    global gold
    gold /= 2
    round(gold)
    typing("You walked a long way to get to this town, and this town looks...")
    t.sleep(1.5)
    typing("Very nice oddly")
    t.sleep(1.5)
    typing("As you're looking around some more, you realize...")
    t.sleep(1.5)
    typing("This is the rich town!")
    t.sleep(1.5)
    while True:
        a_choice = input("What would you like to do in this town?\n'break' for breaking into a mansion\n'shop' to buy somethin\n'grafetti' for vandalizing someone's mansion\n or 'look' to dream about some nice homes").lower()
        if a_choice == "break":
            typing("So you decide to break into someone's house?")
            t.sleep(1.5)
            typing("Sounds wrong since you're trying to save a country but alrighty")
            t.sleep(1.5)
            typing("So you break a window...")
            t.sleep(1.5)
            typing("Then you step into the huge place")
            t.sleep(1.5)
            typing("Then almost instantly, you hear an ear piercing alarm sound that...")
            t.sleep(1.5)
            typing("Echos throughout the entire town!")
            t.sleep(1.5)
            typing("You go into the owner's room to hide, hoping he doesn't see you")
            t.sleep(1.5)
            typing("You hear his footsteps slowly get louder and louder...")
            t.sleep(1.5)
            typing("The first place he checks is under the bed...")
            t.sleep(1.5)
            typing("The second place he looks is in the closet...")
            t.sleep(1.5)
            typing("He sees you in his house!")
            t.sleep(1.5)
            typing("Next thing you know...")
            combat(60,r.randint(1,20),40,70)
            typing("Whether you beat him or not...")
            t.sleep(1.5)
            typing("But you barely made it out alive...")
            value4 += 1
            break
        elif a_choice == "shop":
            typing("You walk into a nice, organized shop...")
            shop()
            value4 += 1
            break
        elif a_choice == "grafetti":
            typing("You chose to vandalize?")
            t.sleep(1.5)
            typing("You're such a little crime commiter")
            t.sleep(1.5)
            typing("You walk over to a mansion that looked the nicest out of any other one")
            t.sleep(1.5)
            gra = input("What would you like to write on the guy's mansion\n").lower()
            t.sleep(1.5)
            typing(f"You skillfully paint {gra} on the person's mansion...")
            t.sleep(1.5)
            typing("Then just as you walk away...")
            t.sleep(1.5)
            typing("You hear a man walk behind you...")
            t.sleep(1.5)
            typing("It turns out to be the owner of the mansion!")
            t.sleep(1.5)
            typing("You wonder what he is going to say...")
            t.sleep(1.5)
            typing("Somehow, he ends up liking your art that you made!")
            t.sleep(1.5)
            typing("Because of this great masterpiece that you have made...")
            t.sleep(1.5)
            typing("He gives you 20 gold!")
            gold += 20
            value4 += 1
            break
        elif a_choice == "look":
            typing("You decide to go down the main street in this town")
            t.sleep(1.5)
            typing("You look at all the great houses and shops...")
            t.sleep(1.5)
            typing("You go into a day dream")
            t.sleep(1.5)
            typing("But then you realize you are still trying to save a country...")
            t.sleep(1.5)
            typing("...from eternal darkness")
            t.sleep(1.5)
            typing("But suddenly you get a little ahead of yourself...")
            t.sleep(1.5)
            typing("Thinking...")
            t.sleep(1.5)
            typing("Honestly all I have to do is beat this little Dragon King...")
            t.sleep(1.5)
            typing("Then I could have everything in this town")
            t.sleep(1.5)
            typing("But then you snap back to your senses and remember...")
            t.sleep(1.5)
            typing("I must not be selfish...")
            t.sleep(1.5)
            typing("This mindset fills you with determination.")
            value4 += 1
            break
        else:
            typing("That ain't somethin' you can do!")
    typing("Well, whatever you decided to do, you continue to the other side of the town")
    t.sleep(1.5)
    typing("You continue to make your way to the side of the town...")
    t.sleep(1.5)
    typing("Closest to the capital.")
    t.sleep(1.5)
    typing("Eager to leave onto the next town, you remember...")
    t.sleep(1.5)
    typing("You still have to fight a general...")
    t.sleep(1.5)
    typing("In order to save this country!")
    t.sleep(1.5)
    typing("So you hurry to go find him")
    t.sleep(1.5)
    typing("When suddenly you feel a tug on your shirt...")
    t.sleep(1.5)
    typing("It's the richest lookin military general you've ever seen")
    t.sleep(1.5)
    typing("In this one case only, he gives you a choice")
    t.sleep(1.5)
    typing("Do you want to fight him?...")
    yay_or_nay = input("y or n?\n").lower()
    t.sleep(1.5)
    if yay_or_nay == "y":
        combat(70,r.randint(1,25),50,45)
    else:
        typing("Alrighty, you chose not to fight him!")
    gold *= 2
    value4 += 1
def drappes():
    typing("After a long trek, you've made it to the final town of them all...")
    t.sleep(1.5)
    typing("There is some of the tallest buildings that you've ever seen")
    t.sleep(1.5)
    typing("But there is only one thing to do in this massive place...")
    t.sleep(1.5)
    typing("That is to fight the one and only Dragon King!")
    t.sleep(1.5)
    typing("So you venture your way over to the center of the city")
    t.sleep(1.5)
    typing("When suddenly you hear over an intercom...")
    t.sleep(1.5)
    typing("I already know you're here, little one...")
    t.sleep(1.5)
    typing("He suddenly flies over you, towering with his massive wings...")
    t.sleep(1.5)
    typing("He lands right in front of you, towering tall over you...")
    t.sleep(1.5)
    typing("He says in a menacing voice...")
    t.sleep(1.5)
    typing("Now you've came, and are about to get what you wished...")
    t.sleep(1.5)
    typing("You begin to fight the Dragon King.")
    combat(250,r.randint(1,35),80,1000)
    typing("...")
    return

start_weapons = {
"great axe":12,
"dagger":8,
"scimitar":10,
"javelin":6, 
"small dinky hammer":12
}
rare_weapons = {
"long sword":15,
"pickaxe":12,
"musket":10,
"lightning bolt":15,
"brick":18
}
exotic_weapons = {
"random cloth":20,
"big dinky hammer":14,
"signature sledge":20,
"plastic knife":16,
"get outa here":25
}
secret_weapons = {
"soda cup":30,
"wand of wander":100,
"555 dc motor":50,
"whip of the century":25,
"mega knight":80,
"Ms LaRose":200,
"fist":80
}
spells = {
"freeze":10,
"fire":15,
"earthquake":20,
"levitation":12,
"thin air":13,
"tornado":20,
"drown":17,
"electrocution":18,
"riches":10,
"insanity":8,
"rage attack":9,
"wind":12,
"heal potion":10
}

starter_weapons = list(start_weapons.keys())
rarer_weapons = list(rare_weapons.keys())
spellers = list(spells.keys())
def shop():
    global gold
    shop_list = [r.choice(starter_weapons), r.choice(spellers), r.choice(rarer_weapons)]
    typing("You take a look to see what they have...")
    for x in shop_list:
        typing(x)
    buy = input("What item would you like to buy? \nor type n to not buy anything\n")
    while True:
        if buy in shop_list and start_weapons or rare_weapons or spells:
            if buy in start_weapons:
                bought_item = start_weapons[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
            elif buy in rare_weapons:
                bought_item = rare_weapons[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
            elif buy in spells:
                bought_item = spells[buy]
                if bought_item >= gold:
                    typing("This costs too much")
                elif bought_item <= gold:
                    inventory[buy] = bought_item
                    gold -= bought_item
                    typing(f"You have bought {buy}! You loose {bought_item} gold!")
                    break
        elif buy == "n":
            break
        else:
            typing("Not an item")
typing("lore goes here...")
t.sleep(1.5)
typing("Welcome to the country of Draeburg, adventurer")
t.sleep(1.5)
typing("Before you start the quest of destroying the dragon king and his army,")
t.sleep(1.5)
typing("You must roll for your stats!")
t.sleep(1.5)
value = 0
value2 = 0
health = 0
while value < 4:
    typing("rolling...")
    t.sleep(1.3)
    value += 1
while value2 <= 1:
    strr = r.randint(5,20)
    dex = r.randint(5,20)
    con = r.randint(5,20)
    intt = r.randint(5,20)
    wis = r.randint(5,20)
    cha = r.randint(5,20)
    ac = r.randint(5,15)
    typing(f"Your stats are...\n strength is {strr}\n dexterity is {dex}\n constitution is {con}\n intelligence is {intt}\n wisdom is {wis}\n charisma is {cha}\narmor class is {ac}\n\n")
    if cha <= 15 or dex <= 15 or strr <= 15 or con <= 15 or intt <= 15 or wis <= 15:
        re_roll = input("Do you want to roll your stats again, y or n?\n")
        if re_roll == "y":
            value2 += 1
            if value2 > 1:
                typing("Well well well, it seems you have reached your limit for rolling")
                break
            continue
        elif "n":
            break
        else:
            typing("not a valid input")
t.sleep(1.5)
typing("Now, here is the list of starter weapons, you can collect more as you go through the towns!")
t.sleep(1)
for key in start_weapons.keys():
    typing(key)
while True:
    s_weapon = input("Which of these weapons would you like?\n").lower()
    if s_weapon in start_weapons:
        value3 = start_weapons[s_weapon]
        typing(f"You have chosen {s_weapon}! nice!\n it does 1D{value3} damage!")
        inventory[s_weapon] = value3
        break
    else:
        typing("Not an actual weapon")
t.sleep(1.5)
typing("Here is the list of towns you can go to!\n Belville\n Madland\n Angousir\n Rockshield\n or the capital, Drappes")
t.sleep(1.5)
while True:
    choice = input("Now which town would you like to go to first, to start fighting the Dragon King's army!\n")
    if choice == "Belville":
        belville()
        break
    elif choice == "Madland":
        madland()
        break
    elif choice == "Angousir":
        angousir()
        break
    elif choice == "Rockshield":
        rockshield()
        break
    elif choice == "Drappes":
        typing("Alrighty, if you really want too")
        drappes()
    else:
        typing("Not a town on the map it seems...")
"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
angousir_complete = False
belville_complete = False
madland_complete = False
rockshield_complete = False
drappes_complete = False
while not angousir_complete or not belville_complete or not madland_complete or not rockshield_complete or not drappes_complete:
    typing("Here is the list of towns you can go to!\n Belville\n Madland\n Angousir\n Rockshield\n or the capital, Drappes")
    choice2 = input("What is the next town that you want to go to?\n")
    if choice2 == "Belville":
        belville()
        belville_complete = True
    elif choice2 == "Madland":
        madland()
        madland_complete = True
    elif choice2 == "Angousir":
        angousir()
        angousir_complete = True
    elif choice2 == "Rockshield":
        rockshield()
        rockshield_complete = True
    elif choice2 == "Drappes":
        drappes()
        drappes_complete = True
    else:
        typing("That isn't a town!")
if angousir_complete and belville_complete and madland_complete and rockshield_complete and drappes_complete:
    if value5 == 0:
        typing("You got the worst ending! You defeated 0 bosses")
        t.sleep(1.5)
        typing("But at least you tried!")
    elif value5 == 1:
        typing("Ay, you didn't do all that bad! You defeated 1 boss")
        t.sleep(1.5)
        typing("But you still got the second worst ending")
    elif value5 == 2:
        typing("Nice! You defeated 2 bosses!")
        t.sleep(1.5)
        typing("You got the third best ending!")
    elif value5 == 3:
        typing("You defeated 3 bosses! You did great")
        t.sleep(1.5)
        typing("This was the second best ending!")
    elif value5 >= 4:
        typing("You defeated 4 or more bosses!")
        t.sleep(1.5)
        typing("You got the best ending.")
    replay = input("Do you want to play again, y or n?\n")
    if replay == "y":
        typing("Alrighty, sending you back to the easiest town...")
        belville()
    else:
        typing("Alrighty, you shall be done.")