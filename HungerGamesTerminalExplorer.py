from TerminalExplorerAssets import (Player,Map,NPC,Object)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification


def main():



	contestants=[NPC(x=0,y=0),NPC(x=0,y=4),NPC(x=0,y=8),NPC(x=0,y=12),NPC(x=0,y=16),NPC(x=0,y=20),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0)]

	centerbox=SqrObjectification(14,20,14,20,color="green")

	map=Map(contestants,centerbox,xscale=1,yscale=1,max_row=21, max_col=21)

	while(True):

		for person in contestants:
			person.move(map.bounds,centerbox,contestants)



		map.update(centerbox,contestants)
		map.display()

		for person in contestants:
			person.updateNearby(contestants)
			person.updateRelate(contestants)


main()