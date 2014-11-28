from TerminalExplorerAssets import (Player,Map,NPC,Object)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification


def main(scale=1):
	userInput=""

	p1=Player(0,0)

	boxes=SqrObjectification(3,6,3,6)
	moarBoxes=StarObjectification(22,36,25,39,"Bushes","green")
	bushes=StarObjectification(2,6,15,19,"Bushes","green")


	somebody=[NPC(x=7,y=7),NPC(x=8,y=8),NPC(x=4,y=10),NPC(x=0,y=14),NPC(x=47,y=37),NPC(x=58,y=18),NPC(x=34,y=30),NPC(x=40,y=24)]


	map=Map(p1,boxes,moarBoxes,bushes,somebody,xscale=1,yscale=1,max_row=40, max_col=60)

	while(userInput!="quit"):

		#userInput=input("What do you do? ")

		if userInput=="up" or userInput=="w":
			p1.move(map.bounds,0,-1,boxes,moarBoxes,bushes,somebody)
		elif userInput=="down" or userInput=="s":
			p1.move(map.bounds,0,1,boxes,moarBoxes,bushes,somebody)
		elif userInput=="left" or userInput=="a":
			p1.move(map.bounds,-1,0,boxes,moarBoxes,bushes,somebody)
		elif userInput=="right" or userInput=="d":
			p1.move(map.bounds,1,0,boxes,moarBoxes,bushes,somebody)
		elif userInput=="quit":
			quit()


		for someone in somebody:
			someone.move(map.bounds,p1,boxes,moarBoxes,bushes)



		map.update(p1,boxes,moarBoxes,bushes,somebody)
		map.display()

		for someone in somebody:
			someone.updateNearby(p1,somebody)
			someone.updateRelate(p1,somebody)
		p1.updateNearby(somebody)
		p1.updateRelate(somebody)


main()
