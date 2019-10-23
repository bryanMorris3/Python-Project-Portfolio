import random
highScores = [1000,950,850,700,675,550,443,414,395,380]
prices = [9.99, 10.25, 19.99, 100.]
dogBreeds = ["Poodle","Collie","Terrier","Beagle"]
logicalResults = [True, True, False, True]
myCollection = [1000, 3.14159, "Carrots", False]
topGames = ["Hollow Knight","Super Smash Bros. Ultimate","Super Mario Odyssey","Breath of the Wild",
"Ocarina of Time","Majora's Mask","Super Mario Galaxy","Final Fantasy","Link to the Past","Mario Kart 8",
"Smash Bros. U","Minecraft","Splatoon","Super Mario World","Final Fantasy 4","Final Fantasy 6",
"Legend of Zelda","Lego Games","Earthbound","Wii Sports"]
print(type(topGames))
print(len(topGames))

if len(topGames) < 20:
    print("fail")
elif "fortnite" in topGames or "Fortnite" in topGames:
    print("fail")
elif topGames != "World of Warcraft":
    print("fail")
else:
    print("pass")
##for i in topGames:
##    print(i)
##for i in range(0, len(topGames)):
##    print(topGames[i])
num = random.randint(0,len(topGames)-1)
print(topGames[num])
topGames [0] = "World of Warcraft"
print(topGames)
for i in topGames:
    if  i == "World of Warcraft" or i == "Link to the Past":
        print("pass")
    else:
        print("not it")
worstGames = ["Yo! Noid","Skate or Die","Where's Waldo","Total Recall","Fatal Fury","Elevator Action",
"Fester's Quest","Desert Strike: Return to the Gulf","The Three Stooges","Superman: The New Superman Adventures",
"Ghosts n' Goblins","Jurassic Park","Joust","Wayne's World","Muscle","Paperboy","Top Gun","Shaq Fu","E.T.","Fortnite"]
              
