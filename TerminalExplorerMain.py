from TerminalExplorerAssets import (Player,Map,NPC,Object)
from TerminalExplorerObjectGen import SqrObjectification


def main(scale=1):
	userInput=""

	p1=Player(0,0)

	boxes=SqrObjectification(3,6,3,6)
	moarBoxes=SqrObjectification(9,14,3,14)


	somebody=[NPC(x=7,y=7),NPC(x=8,y=8),NPC(x=4,y=10),NPC(x=0,y=14)]


	map=Map(p1,boxes,moarBoxes,somebody,xscale=3,yscale=3,max_row=5, max_col=5)

	while(userInput!="quit"):

		userInput=input("What do you do? ")

		if userInput=="up" or userInput=="w":
			p1.move(map.bounds,0,-1,boxes,moarBoxes,somebody)
		elif userInput=="down" or userInput=="s":
			p1.move(map.bounds,0,1,boxes,moarBoxes,somebody)
		elif userInput=="left" or userInput=="a":
			p1.move(map.bounds,-1,0,boxes,moarBoxes,somebody)
		elif userInput=="right" or userInput=="d":
			p1.move(map.bounds,1,0,boxes,moarBoxes,somebody)
		elif userInput=="quit":
			quit()


		for someone in somebody:
			someone.move(map.bounds,p1,boxes,moarBoxes)



		map.update(p1,boxes,moarBoxes,somebody)
		map.display()

		for someone in somebody:
			someone.updateNearby(p1,somebody)
			someone.updateRelate(p1,somebody)
		p1.updateNearby(somebody)
		p1.updateRelate(somebody)


main()
