from ant import coordinates, addCoordinates, displayCoordinates, Ant, Grid
from random import randint
import pygame

DEFAULT_COORDINATES	= coordinates(100,100)
NUMBER_ANTS			= 10
	
def displayAnts():
	count = 0
	for i in antGrid.storedIndex:
		
		x 		= antGrid.storedIndex[count][0]
		y 		= antGrid.storedIndex[count][1]
		
		if antGrid.storedInformation[count][0]:
			screen.set_at((x, y),(255, 255, 255))
		else:
			color 	= antGrid.storedInformation[count][1]
			screen.set_at((x, y), (color, color, 100))
		count += 1
				
		
def updatePhermone():
	if randint(0, 10) >= 0:
		count = 0
		for i in antGrid.storedInformation:
			sPhermoneLevel = antGrid.storedInformation[count][1]
			if sPhermoneLevel > 5:
				antGrid.storedInformation[count][1] = sPhermoneLevel - 1
			count += 1
			
			backlog = len(antGrid.storedIndex)
			
			if backlog > 40000:
				antGrid.storedIndex.pop(0)
				antGrid.storedInformation.pop(0)

ant 	= Ant(DEFAULT_COORDINATES)
antGrid	= Grid(ant.GRID_WIDTH, ant.GRID_HEIGHT)
screen 	= pygame.display.set_mode((ant.GRID_WIDTH, ant.GRID_HEIGHT))

running = True

herd = [Ant(DEFAULT_COORDINATES) for i in range(0, NUMBER_ANTS)]

iterations = 1 		# for debugging purposes

while running:
		
	displayAnts()
	updatePhermone()
	
	for ant in herd:
		
		directions	= ant.getPossibleDirections()
		count = 0
		for direction in directions:
			possibleDirection 	= ant.DIRECTIONS[ant.DNAMES.index(directions[count])]
			possibleCoordinates = addCoordinates(ant.location, possibleDirection)
			if possibleCoordinates in antGrid.storedIndex:
				index = antGrid.storedIndex.index(possibleCoordinates)
				directions.remove(directions[count])
			count += 1
						
		rand = randint(0, (len(directions)- 1))
		
		antGrid.storePoint(ant.location, False, 0, 0)
		

		ant.move( ant.DIRECTIONS[ant.DNAMES.index(directions[rand])] )
		
		antGrid.storePoint(ant.location, True, 250, 0)
				
#	if iterations > 3:		# stop simulation after x iterations
#		running = False		# (for debugging purposes)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()
	
	iterations += 1
