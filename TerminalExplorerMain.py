from TerminalExplorerAssets import (Player,Map,NPC,Object)
from TerminalExplorerObjectGen import SqrObjectification


def main(scale=1):
	userInput=""

	p1=Player(0,0)

	boxes=[]
	for x in range(5):
		boxes.append(Object("Box",3,3+x))


	somebody=NPC(4,4)


	map=Map(p1,boxes,somebody,xscale=3,yscale=3,max_row=5, max_col=5)

	while(userInput!="quit"):
		userInput=input("What do you do? ")
		if userInput=="up" or userInput=="w":
			p1.move(map.bounds,0,-1,boxes,somebody)
		elif userInput=="down" or userInput=="s":
			p1.move(map.bounds,0,1,boxes,somebody)
		elif userInput=="left" or userInput=="a":
			p1.move(map.bounds,-1,0,boxes,somebody)
		elif userInput=="right" or userInput=="d":
			p1.move(map.bounds,1,0,boxes,somebody)

		somebody.move(map.bounds,p1,boxes)
		map.update(p1,boxes,somebody)
		map.display()

main()
