from TerminalExplorerAssets import (Player,Map,NPC,Object,Point)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification
import csv
from random import randrange



def main():
	userInput=""
	points = []
	randomSpawn=True

	with open(input("Filename: ")) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			#print (row["x"],row["y"])
			points.append((int(row["x"]),int(row["y"])))

	units=[]

	for element in points:
		if randomSpawn:
			units.append(NPC(x=randrange(0,19),y=randrange(0,19),behavior="Track",track=Point(element[0],element[1]),devMatter=True))
		else:
			units.append(NPC(x=0,y=0,behavior="Track",track=Point(element[0],element[1]),devMatter=True))

	map=Map(units,xscale=1,yscale=1,max_row=20, max_col=20)

	counter = 0

	while(userInput!="quit"):
		counter+=1

		done=True


		for unit in units:
			unit.move(map.bounds,units)
			#print(unit.x,unit.y)
			if unit.reached == False:
				done=False

		if done:
			userInput="quit"

		map.update(units)
		map.display()

	print("Completed in",counter,"turns.")

main()