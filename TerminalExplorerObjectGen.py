from TerminalExplorerAssets import Object

def SqrObjectification(startX,endX,startY,endY,whatisit="Something",color="red"):
	listOfObjects=[]


	for y in range(startY,endY+1):
		for x in range(startX,endX+1):
			listOfObjects.append(Object(whatisit,x=x,y=y,color=color))


	return listOfObjects

def StarObjectification (startX,endX,startY,endY,whatisit="Something",color="red"):
	listOfObjects=[]
	
	xDif=endX-startX
	yDif=endY-startY
	count=-1

	for y in range(startY,endY+1):
		count+=1
		for x in range(startX,endX+1):
				if x==(xDif/2)+startX or y==(yDif/2)+startY:
					listOfObjects.append(Object(whatisit,x=x,y=y,color=color))				
				elif x==(xDif/2)+startX+(yDif/2)+count:
					if (x!=endX and y!=endY and x!=startX and y!=startY): 
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)+startX+((yDif/2)-count):
					if(x!=endX and y!=endY and x!=startX and y!=startY):
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)+startX-(yDif/2)+count:
					if (x!=endX and y!=endY and x!=startX and y!=startY): 
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)+startX-((yDif/2)-count):
					if(x!=endX and y!=endY and x!=startX and y!=startY):
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)-startX-(yDif/2)+count:
					if (x!=endX and y!=endY and x!=startX and y!=startY): 
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)-startX-((yDif/2)-count):
					if(x!=endX and y!=endY and x!=startX and y!=startY):
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)-startX+(yDif/2)+count:
					if (x!=endX and y!=endY and x!=startX and y!=startY): 
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
				elif x==(xDif/2)-startX+((yDif/2)-count):
					if(x!=endX and y!=endY and x!=startX and y!=startY):
						listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
	return listOfObjects