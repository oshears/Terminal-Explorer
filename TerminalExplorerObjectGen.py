from TerminalExplorerAssets import Object

def SqrObjectification(startX,endX,startY,endY,whatisit="Something",color="red"):
	listOfObjects=[]

	for y in range(startY,endY+1):
		for x in range(startX,endX+1):
			listOfObjects.append(Object(whatisit,x=x,y=y,color=color))


	return listOfObjects

def CirObjectification (startX,endX,startY,endY,whatisit="Something",color="red"):
	listOfObjects=[]

	xDif=endX-startX
	yDif=endY-startY
	xAtribute=0
	negXAtribute=0
	count=-1

	for y in range(startY,endY+1):
		#count+=1
		for x in range(startX,endX+1):
			if x==(xDif/2)+startX or y==(yDif/2)+startY:
				listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
			
			if x==(xDif/2)+startX+(yDif/2)+count:
				if (x!=endX and y!=endY and x!=startX and y!=startY): 
					listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
			if x==(xDif/2)+startX+((yDif/2)-count):
				if(x!=endX and y!=endY and x!=startX and y!=startY):
					listOfObjects.append(Object(whatisit,x=x,y=y,color=color))

			if x==(xDif/2)-startX+(yDif/2)+count:
				if (x!=endX and y!=endY and x!=startX and y!=startY): 
					listOfObjects.append(Object(whatisit,x=x,y=y,color=color))
			if x==(xDif/2)-startX+((yDif/2)-count):
				if(x!=endX and y!=endY and x!=startX and y!=startY):
					listOfObjects.append(Object(whatisit,x=x,y=y,color=color))

	return listOfObjects
'''
startY
(xDif/2)+0
xx0xx

startY+1
(xDif/2)+0
(xDif/2)+1
(xDif/2)-1
x000x

startY+2
(xDif/2)+0
(xDif/2)+1
(xDif/2)-1
00000

x000x
xx0xx
'''