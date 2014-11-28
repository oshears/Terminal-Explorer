from TerminalExplorerAssets import Object

def SqrObjectification(startX,endX,startY,endY,whatisit="Something"):
	listOfObjects=[]

	for y in range(startY,endY+1):
		for x in range(startX,endX+1):
			listOfObjects.append(Object(whatisit,x=x,y=y))


	return listOfObjects