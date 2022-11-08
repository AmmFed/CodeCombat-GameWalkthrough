# M1:L1~L19 are all straight-forward 
# from "Dungeons of Kithgard" to "Kithgard Gates"


# M2:L2 "Winding Trail"
# Getting all the gems trick
# 1. Getting the first gem
hero.moveXY(36, 59)
# 2. Getting the second gem
hero.moveXY(37, 12)
# 3. Instead of buidling a fence, build a fire-trap on the X mark
hero.buildXY("fire-trap", 72, 25)
# 4. Move away from the fence to the right then to the left 
# to waste some time till the enemy reaches the fire-trap
hero.moveXY(77, 15)
hero.moveXY(54, 17)
# 5. Get the last sweet gems!
hero.moveXY(73, 64)


# M2:L8 "Range Finder"
# Completing the level in only 3 lines of code, 
# just ignoring the declaration of distance and enemy variables
hero.say(hero.distanceTo("Gort"))
hero.say(hero.distanceTo("Smasher"))
hero.say(hero.distanceTo("Gorgnub"))


# M2:L9 "Peasant Protection"
# Using the Boolean Operator "and" to reduce the code count
while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10: # <- Use "and" here
        hero.attack(enemy)
    else:
        hero.moveXY(40, 37)


# M2:L10 "Maniac Munchkins"
# Using multiple "and"s to reduce the code count
while True:
    hero.attack("Chest")
    enemy = hero.findNearestEnemy()
    # Use three lines in one line
    if enemy and hero.distanceTo(enemy) < 5 and hero.isReady("cleave"): 
        hero.cleave(enemy)
    # Use two lines in one line
    elif enemy and hero.distanceTo(enemy) < 5: 
        hero.attack(enemy)


# M2:L11 "Forest Fire Dancing"
# In this level the evilstone is bad! Avoid them, 
# walking the other direction.
while True:
    evilstone = hero.findNearestItem()
    # When evilstone exists and is to the left:
    if evilstone and evilstone.pos.x == 34:
        hero.moveXY(46, 23)
    # When evilstone exists but is not to the left:
    elif evilstone and evilstone.pos.x != 34:
        hero.moveXY(34, 22)
    # When evilstone is not there
    else:
        hero.moveXY(40, 22)


# M2:L12 "Village Rover"
# Create functions that will be used
# This function checks for enemies and then attacks them
def findAndAttack():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)


# Create a while-true loop to keep looking for enemies
# and protecting the peasents moving back-and-forth
while True:
    # Move to the left defense spot
    hero.moveXY(35, 34)
    # Look for any enemies
    findAndAttack()
    # Move to the right defense spot
    hero.moveXY(60, 31)
    # Look for any enemies
    findAndAttack()


# M2:L13 "Backwoods Fork"
# Use the checkAndAttack function 
# to make your code easy to read.

# Define a function to check then attack if an enemy exists
def checkAndAttack(target):
    if target:
        hero.attack(target)

# Start a while-true loop to let the hero move around 
# and search then attack enemies, repeatedly
while True:
    # Move around and check to attack if there's an enemy
    hero.moveXY(58, 52) # Move to upper spot and check
    checkAndAttack(hero.findNearestEnemy())
    hero.moveXY(43, 34) # Move to middle spot and check
    checkAndAttack(hero.findNearestEnemy())
    hero.moveXY(58, 16) # Move to lower spot and check
    checkAndAttack(hero.findNearestEnemy())
    hero.moveXY(43, 34) # Move to middle spot and check
    checkAndAttack(hero.findNearestEnemy())


# M2:L14 "Leave It to Cleaver"
# This shows how to define a function called cleaveWhenClose

# Define a function with a parameter to cleave when an enemy is close
def cleaveWhenCloseOrAttack(target):
    # 3 lines in one condition
    if target and hero.distanceTo(target) < 5 and hero.isReady("cleave"):
        hero.cleave(target)
    elif target:
        hero.attack(target)

# Start a loop to attack or cleave nearby enemies
while True:
    cleaveWhenCloseOrAttack(hero.findNearestEnemy()) # Cleave or attack enemies



