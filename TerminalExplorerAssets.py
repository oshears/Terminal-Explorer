from os import system
import TerminalExplorerAIs
from TerminalExplorerUtilities import colorify,colorify_advanced

class Player:


	def __init__(self,x=0,y=0,name="A Player",solid=True,color="cyan"):
		self.type="Player"
		self.x=x
		self.y=y
		self.name=name
		self.nearby=[]
		self.relate={}
		self.solid=solid
		self.color=color


	def move(self,bounds,x=0,y=0,*objects):

		for item in objects:
			if (str(type(item))=="<class 'list'>"):
				for subItems in item:
					if self.x+x==subItems.x and self.y==subItems.y and subItems.solid and subItems.type=="Object":
						return
					elif self.y+y==subItems.y and self.x==subItems.x and subItems.solid and subItems.type=="Object":
						return
					#elif subItems.x==self.x and subItems.y==self.y and self.encounter==False:
						#return

			else:
				if self.x+x==item.x and self.y==item.y and item.solid and item.type=="Object":
					return
				elif self.y+y==item.y and self.x==item.x and item.solid and item.type=="Object":
					return
				#elif item.x==self.x and item.y==self.y and self.encounter==False:
					#return

		if self.x!=0 and self.x!=bounds[1]-1:
			self.x+=x
		if self.y!=0 and self.y!=bounds[0]-1:
			self.y+=y
		if self.y==0 and y>0:
			self.y+=y
		if self.x==0 and x>0:
			self.x+=x
		if self.y==bounds[0]-1 and y<0:
			self.y+=y
		if self.x==bounds[1]-1 and x<0:
			self.x+=x

	def updateNearby(self,*objects):
		self.nearby=TerminalExplorerAIs.findNearby(self,*objects)

	def updateRelate(self,*objects):
		self.relate=TerminalExplorerAIs.makeRelate(self,*objects)
		#Code for displaying who the object is near
		#print(self,":",self.name)
		#for key in self.relate.keys():
			#print(key,self.relate[key])


class Map:

	def __init__(self, *objects, xscale=1, yscale=1, max_col=5, max_row=5,floorColor="black"):
		self.positions=[]
		self.xscale=xscale
		self.yscale=yscale
		self.bounds=(max_row*yscale,max_col*xscale)
		self.floorColor=floorColor
		for y in range(self.bounds[0]):
			tempList=[]
			for x in range(self.bounds[1]):
				tempList.append([colorify("X",self.floorColor)])
			self.positions.append(tempList)

		print(self.bounds)

		for item in objects:
			if (str(type(item))=="<class 'list'>"):
				for subItems in item:
					if subItems.type=="Object":
						self.positions[subItems.y][subItems.x]=[colorify("+",subItems.color)]
					elif subItems.type=="Player":
						self.positions[subItems.y][item.x]=[colorify("@",subItems.color)]
					elif subItems.type=="NPC":
						self.positions[subItems.y][subItems.x]=[colorify("$",subItems.color)]
			else:
				if item.type=="Object":
					self.positions[item.y][item.x]=[colorify("+",item.color)]
				elif item.type=="Player":
					self.positions[item.y][item.x]=[colorify("@",item.color)]
				elif item.type=="NPC":
					self.positions[item.y][item.x]=[colorify("$",item.color)]

		self.display()


	def update(self,*objects):
		reserved_locations=[]
		for item in objects:
			if (str(type(item))=="<class 'list'>"):
				for subItems in item:
					for row in range(self.bounds[0]):
						for col in range(self.bounds[1]):
							if subItems.x == col and subItems.y==row:
								reserved_locations.append((row,col))
								if subItems.type=="Object":
									self.positions[row][col]=[colorify("+",subItems.color)]
								elif subItems.type=="Player":
									self.positions[row][col]=[colorify("@",subItems.color)]
									#Code for player scaling
									#for y in range(self.yscale):
										#for x in range(self.xscale):
											#self.positions[row+y][col+x]=["\x1b[46m\x1b[36m@\x1b[0m"]
											#reserved_locations.append((row+y,col+x))
								elif subItems.type=="NPC":
									self.positions[row][col]=[colorify_advanced("$",subItems.advancedColor)]
							elif (row,col) not in reserved_locations:
								self.positions[row][col]=[colorify("X",self.floorColor)]
			else:
				for row in range(self.bounds[0]):
					for col in range(self.bounds[1]):
						if item.x == col and item.y==row:
							reserved_locations.append((row,col))
							if item.type=="Object":
								self.positions[row][col]=[colorify("+",item.color)]
							elif item.type=="Player":
								self.positions[row][col]=[colorify("@",item.color)]
								#Code for player scaling
								#for y in range(self.yscale):
									#for x in range(self.xscale):
										#self.positions[row+y][col+x]=["\x1b[46m\x1b[36m@\x1b[0m"]
										#reserved_locations.append((row+y,col+x))
							elif item.type=="NPC":
								self.positions[row][col]=[colorify_advanced("$",item.advancedColor)]
						elif (row,col) not in reserved_locations:
							self.positions[row][col]=[colorify("X",self.floorColor)]


	def display(self):
		system("clear")
		for row in range(self.bounds[0]):
			for col in range(self.bounds[1]):
				print(self.positions[row][col][0]," ",end="")
			print()

class NPC:
	def __init__(self,name="An NPC",x=0,y=0,color="yellow",behavior="Wander",track=None,hp=100,hostile=False,advancedColor=118,solid=True):
		
		#Pretty much alwats static
		self.solid=False
		self.type="NPC"

		self.x=x
		self.y=y
		self.name=name
		self.behavior=behavior
		self.nearby=[]
		self.relate={}
		self.track=track
		self.color=color
		self.hp=hp
		self.hostile=hostile
		self.advancedColor=advancedColor
	
	def updateDefinition(self,name=None,x=None,y=None,color=None,behavior=None,track=None,hp=None,hostile=None):

		if name!=None:
			self.name=name
		if behavior!=None:
			self.behavior=behavior
		if track!=None:
			self.track=track
		if color!=None:
			self.color=color
		if hp!=None:
			self.hp=hp
		if hostile!=None:
			self.hostile=hostile

	def cleanSlate(self,name="An NPC",color="yellow",behavior="Wander",track=None,hp=100,hostile=False):
		self.name=name
		self.behavior=behavior
		self.nearby=[]
		self.relate={}
		self.track=track
		self.color=color
		self.hp=hp
		self.hostile=hostile
		self.reached=False
	
	def teleport(self,x=0,y=0):
		self.x=x
		self.y=y

	def move(self,bounds,*objects):
		TerminalExplorerAIs.movement(self,bounds,objects)
		if self.x==self.track.x and self.y==self.track.y:
			self.reached=True
		else:
			self.reached=False

	def updateNearby(self,*objects):
		self.nearby=TerminalExplorerAIs.findNearby(self,*objects)

	def updateRelate(self,*objects):
		self.relate=TerminalExplorerAIs.makeRelate(self,*objects)
		#Code for displaying who the object is near
		#print(self,":",self.name)
		#for key in self.relate.keys():
			#print(key,self.relate[key])
		if self.relate!={}:
			if max(list(self.relate.values()))>=80 and not self.hostile:
				self.cleanSlate()
			elif max(list(self.relate.values()))>=60 and not self.hostile:
				self.color="blue"
				print( colorify(self,self.color,True), colorify(max(list(self.relate.values())),self.color,True) )
			elif max(list(self.relate.values()))>=40 and not self.hostile:
				self.color="white"
				print( colorify(self,self.color,True), colorify(max(list(self.relate.values())),self.color,True) )
			elif max(list(self.relate.values()))>=20 and not self.hostile:
				self.color="magenta"
				print( colorify(self,self.color,True), colorify(max(list(self.relate.values())),self.color,True) )



class Object:
	def __init__(self,name="An Object",x=0,y=0,solid=True,color="red"):
		self.x=x
		self.y=y
		self.type="Object"
		self.name=name
		self.solid=solid
		self.color=color

class Point:

	def __init__(self,x,y,solid=False):
		self.x=x
		self.y=y
		self.solid=solid


