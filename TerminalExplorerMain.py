from TerminalExplorerAssets import (Player,Map,NPC,Object)


def main(scale=1):
	userInput=""

	p1=Player(0,0)

	boxes=[]
	for x in range(5):
		boxes=Object("Box",3,3)


	somebody=NPC(4,4)


	map=Map(p1,box,somebody,xscale=3,yscale=3,max_row=5, max_col=5)

	while(userInput!="quit"):
		userInput=input("What do you do? ")
		if userInput=="up" or userInput=="w":
			p1.move(map.bounds,0,-1,box,somebody)
		elif userInput=="down" or userInput=="s":
			p1.move(map.bounds,0,1,box,somebody)
		elif userInput=="left" or userInput=="a":
			p1.move(map.bounds,-1,0,box,somebody)
		elif userInput=="right" or userInput=="d":
			p1.move(map.bounds,1,0,box,somebody)

		somebody.move(map.bounds,p1,box)
		map.update(p1,box,somebody)
		map.display()

main()
