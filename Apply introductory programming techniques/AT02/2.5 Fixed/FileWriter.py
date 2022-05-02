f = open("news.txt", "w") #the w stands for write. using write over rights what was already there
f.write("You don't need to fight Elden Ring's Placidusax boss to complete your journey in the Lands Between, but if you're determined to take on every boss, this dragon is very easy to miss. "
        "It's also required for one of the achievements, so you'll need to take him down if you're a completionist."
        "got this info at https://www.pcgamer.com/au/elden-ring-dragonlord-placidusax-location/")
f.close()#it is good practice to close the file

f = open("news.txt", "r")
print(f.read())
f.close()
