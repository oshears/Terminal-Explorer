from TerminalExplorerAssets import (Player,Map,NPC,Object,Point)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification
import csv


def main():
	userInput=""
	points = []

	with open("model.csv") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			#print (row["x"],row["y"])
			points.append((int(row["x"]),int(row["y"])))

	units=[]

	for element in points:
		units.append(NPC(x=0,y=0,behavior="Track",track=Point(element[0],element[1])))

	map=Map(units,xscale=1,yscale=1,max_row=20, max_col=20)

	while(userInput!="quit"):

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


main()