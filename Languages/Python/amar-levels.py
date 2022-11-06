#M1:L1~L19 are all straight-forward from "Dungeons of Kithgard" to "Kithgard Gates"

#M2:L2 "Winding Trail"
#Getting all the gems trick
#1. Getting the first gem
hero.moveXY(36, 59)
#2. Getting the second gem
hero.moveXY(37, 12)
#3. Instead of buidling a fence, build a fire-trap on the X mark
hero.buildXY("fire-trap", 72, 25)
#4. Move away from the fence to the right then to the left 
#to waste some time till the enemy reaches the fire-trap
hero.moveXY(77, 15)
hero.moveXY(54, 17)
#5. Get the last sweet gems!
hero.moveXY(73, 64)

#M2:L8 "Range Finder"
#Completing the level in only 3 lines of code, 
#just ignoring the declaration of distance and enemy variables
hero.say(hero.distanceTo("Gort"))
hero.say(hero.distanceTo("Smasher"))
hero.say(hero.distanceTo("Gorgnub"))

#M2:L9 "Peasant Protection"
#Using the Boolean Operator "and" to reduce the code count
while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10: #<- Use "and" here
        hero.attack(enemy)
    else:
        hero.moveXY(40, 37)


#M2:L10 "Maniac Munchkins"
#Using multiple "and"s to reduce the code count
while True:
    hero.attack("Chest")
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 5 and hero.isReady("cleave"): #Use three lines in one line
        hero.cleave(enemy)
    elif enemy and hero.distanceTo(enemy) < 5: #Use two lines in one line
        hero.attack(enemy)
