#M1:L1~L96 are all straight-forward

#M2:L2:
# Go to the end of the path and build a fence on the X
# Use your moveXY(x, y) function.
# It's the first point of the path.
hero.moveXY(36, 59)
# Move at the next points of the path.
hero.moveXY(37, 12)
# Build a fence to stop the ogre.
hero.buildXY("fire-trap", 72, 25)
hero.moveXY(77, 15)
hero.moveXY(54, 17)
hero.moveXY(73, 64)