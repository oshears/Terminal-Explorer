from TerminalExplorerAssets import (Player,Map,NPC,Object)


def main(scale=1):
	userInput=""

	p1=Player(0,0)
	box=Object(3,3)
	somebody=NPC(4,4)
	map=Map(p1,box,somebody,scale=1,max_row=10, max_col=10)

	while(userInput!="quit"):
		userInput=input("What do you do? ")
		if userInput=="up" or userInput=="w":
			p1.move(map.bounds,0,-1,box)
		elif userInput=="down" or userInput=="s":
			p1.move(map.bounds,0,1,box)
		elif userInput=="left" or userInput=="a":
			p1.move(map.bounds,-1,0,box)
		elif userInput=="right" or userInput=="d":
			p1.move(map.bounds,1,0,box)

		somebody.move(map.bounds,p1,box)
		map.update(p1,box,somebody)
		map.display()

main()
