from TerminalExplorerAssets import (Player,Map,NPC,Object)


def main(scale=1):
	userInput=""

	p1=Player(0,0)
	box=Object(3,3)
	map=Map(p1,box,scale=1,max_row=5, max_col=4)

	while(userInput!="quit"):
		userInput=input("What do you do? ")
		if userInput=="up":
			p1.move(map.bounds,0,-1,box)
			map.update(p1,box)
			map.display()
		elif userInput=="down":
			p1.move(map.bounds,0,1,box)
			map.update(p1,box)
			map.display()
		elif userInput=="left":
			p1.move(map.bounds,-1,0,box)
			map.update(p1,box)
			map.display()
		elif userInput=="right":
			p1.move(map.bounds,1,0,box)
			map.update(p1,box)
			map.display()

main()
