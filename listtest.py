#Bryan Morris
#10/7/19
#Inventory
import random
#player stats
deff = 0
atk = 1
health = 100
mana = 50
inv = []
equp = []
maxInv = 10
#chest setup
chestInv = ("gold", "gems", "food", "sword", "armor", "shield","healing potion", "mana potion",
            "arrows","bow","spear","cross bow","helm","pants","boots", "Doom Hammer",
            "orb of future telling","gloves","bracers","Excalibar","Hero Shield")

maxChest = 5

items = random.randint (1,maxChest)
chest = []
for i in range(items):
    chest.append(random.choice(chestInv))


if inv:
    print(inv)
else:
    print("you have nothing in inventory")
    input("open the chest to get your items")
    for items in chest:
        inv.append(items)
print(inv)

for items in inv:
    if items == "healing potion":
        health += 50
        inv.remove("healing potion")
    elif items == "armor":
        print("you put on the armor")
        deff += 10
        equp.append("armor")
        inv.remove("armor")
    elif items == "shield":
        deff += 5
        equp.append("shield")
        inv.remove("shield")
    elif items == "helm":
        deff += 5
        equp.append("helm")
        inv.remove("helm")
    elif items == "pants":
        deff += 3
        equp.append("pants")
        inv.remove("pants")
    elif items == "boots":
        deff += 2
        inv.remove("boots")
        equp.append("boots")
    elif items == "gloves":
        deff += 2  
        equp.append("gloves")
        inv.remove("gloves")
    elif items == "bracers":
        deff += 5
        equp.append("bracers")
        inv.remove("bracers")
    elif items == "Hero Shield":
        deff += 50
        equp.append("Hero Shield")
        inv.remove("Hero Shield")
    elif items == "sword":
        atk += 10
        equp.append("sword")
        inv.remove("sword")
print("Health:",health)
print("Defense:",deff)
print("Inventory:",inv)
print("Equipped:",equp)


maxChest = 15

items = random.randint (1,maxChest)
chest = []
for i in range(items):
    chest.append(random.choice(chestInv))
input ("press enter to open chest")
for i in chest:
    inv.append(i)

if len(inv) > maxInv:
    x = len(inv) - maxInv 
    print(inv)
    print("You need to remove " +str(x) +" items")
    while x > 0:
        item = input("Choose an item to drop.")
        inv.remove(item)
        x -= 1
    print(inv)

    
