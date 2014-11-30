from TerminalExplorerAssets import (Player,Map,NPC,Object)
from TerminalExplorerObjectGen import SqrObjectification,StarObjectification


def main():

	centerbox=SqrObjectification(14,20,14,20,color="green")
	obstruction=SqrObjectification(0,12,14,14,color="green",solid=False)

	contestants=[NPC(x=0,y=8),NPC(x=0,y=4),NPC(x=0,y=0),NPC(x=0,y=12),NPC(x=0,y=16),NPC(x=0,y=20),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0),
				NPC(x=4,y=0),NPC(x=8,y=0),NPC(x=12,y=0),NPC(x=16,y=0),NPC(x=20,y=0)]

	hunters=[NPC(x=0,y=20,behavior="Track",track=contestants[0],color="red",hostile=True),
				NPC(x=4,y=20,behavior="Track",track=contestants[25],color="red",hostile=True),
				NPC(x=8,y=20,behavior="Track",track=contestants[4],color="red",hostile=True),
				NPC(x=12,y=20,behavior="Track",track=contestants[6],color="red",hostile=True)]

	map=Map(obstruction,centerbox,contestants,hunters,xscale=1,yscale=1,max_row=21, max_col=21)

	x=0
	while(x>-1):

		for person in contestants:
			person.move(map.bounds,centerbox,obstruction,contestants,hunters)

		for hunter in hunters:
			hunter.move(map.bounds,centerbox,obstruction,contestants,hunters)



		map.update(centerbox,obstruction,contestants,hunters)
		map.display()

		for person in contestants:
			person.updateNearby(contestants,hunters)
			person.updateRelate(contestants,hunters)

		for hunter in hunters:
			hunter.updateNearby(contestants,hunters)
			hunter.updateRelate(contestants,hunters)

		x+=1
		print("Step:",x)

main()