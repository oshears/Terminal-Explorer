from TerminalExplorerAssets import (Player,Map,NPC,Object,Point)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification


def main():
	userInput=""


	units = [NPC(x=0,y=0,behavior="Track",track=Point(11,11)),
		NPC(x=0,y=0,behavior="Track",track=Point(11,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(11,13)),
		NPC(x=0,y=0,behavior="Track",track=Point(12,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(13,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(14,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(15,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(16,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,12)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,11)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,10)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,9)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,8)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,7)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,6)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,5)),
		NPC(x=0,y=0,behavior="Track",track=Point(17,4))]


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