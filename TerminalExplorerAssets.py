from os import system
import TerminalExplorerAIs

class Player:


	def __init__(self,x=0,y=0,name="A Player"):
		self.type="Player"
		self.x=x
		self.y=y
		self.name=name
		self.encounter=False


	def move(self,bounds,x=0,y=0,*objects):
		self.encounter=False

		for item in objects:
			if (str(type(item))=="<class 'list'>"):
				for subItems in item:
					if self.x+x==subItems.x and self.y==subItems.y and subItems.solid:
						return
					elif self.y+y==subItems.y and self.x==subItems.x and subItems.solid:
						return
					if subItems.x==self.x and subItems.y==self.y and self.encounter==False:
						self.encounter=True
			else:
				if self.x+x==item.x and self.y==item.y and item.solid:
					return
				elif self.y+y==item.y and self.x==item.x and item.solid:
					return
				if item.x==self.x and item.y==self.y and self.encounter==False:
					self.encounter=True

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



class Map:

	def __init__(self, *objects, xscale=1, yscale=1, max_col=5, max_row=5):
		self.positions=[]
		self.xscale=xscale
		self.yscale=yscale
		self.bounds=(max_row*yscale,max_col*xscale)
		for y in range(self.bounds[0]):
			tempList=[]
			for x in range(self.bounds[1]):
				tempList.append(["X"])
			self.positions.append(tempList)

		print(self.bounds)

		for item in objects:
			if (str(type(item))=="<class 'list'>"):
				for subItems in item:
					if subItems.type=="Player":
						self.positions[subItems.y][item.x]=["\x1b[46m\x1b[36m@\x1b[0m"]
					if subItems.type=="Object":
						self.positions[subItems.y][subItems.x]=["\x1b[31m\x1b[41m+\x1b[0m"]
					elif subItems.type=="NPC":
						self.positions[subItems.y][subItems.x]=["\x1b[32m\x1b[42m$\x1b[0m"]
			else:
				if item.type=="Player":
					self.positions[item.y][item.x]=["\x1b[46m\x1b[36m@\x1b[0m"]
				if item.type=="Object":
					self.positions[item.y][item.x]=["\x1b[31m\x1b[41m+\x1b[0m"]
				elif item.type=="NPC":
					self.positions[item.y][item.x]=["\x1b[32m\x1b[42m$\x1b[0m"]

		#self.positions[player.y][player.x]=["\x1b[31m@\x1b[0m"]
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
								if subItems.type=="Player":
									self.positions[row][col]=["\x1b[46m\x1b[36m@\x1b[0m"]
									#for y in range(self.yscale):
										#for x in range(self.xscale):
											#self.positions[row+y][col+x]=["\x1b[46m\x1b[36m@\x1b[0m"]
											#reserved_locations.append((row+y,col+x))
								elif subItems.type=="Object":
									self.positions[row][col]=["\x1b[41m\x1b[31m+\x1b[0m"]
								elif subItems.type=="NPC":
									self.positions[row][col]=["\x1b[42m\x1b[32m$\x1b[0m"]
							elif (row,col) not in reserved_locations:
								self.positions[row][col]=["X"]
			else:
				for row in range(self.bounds[0]):
					for col in range(self.bounds[1]):
						if item.x == col and item.y==row:
							reserved_locations.append((row,col))
							if item.type=="Player":
								self.positions[row][col]=["\x1b[46m\x1b[36m@\x1b[0m"]
								#for y in range(self.yscale):
									#for x in range(self.xscale):
										#self.positions[row+y][col+x]=["\x1b[46m\x1b[36m@\x1b[0m"]
										#reserved_locations.append((row+y,col+x))
							elif item.type=="Object":
								self.positions[row][col]=["\x1b[41m\x1b[31m+\x1b[0m"]
							elif item.type=="NPC":
								self.positions[row][col]=["\x1b[42m\x1b[32m$\x1b[0m"]
						elif (row,col) not in reserved_locations:
							self.positions[row][col]=["X"]


	def display(self):
		system("clear")
		for row in range(self.bounds[0]):
			for col in range(self.bounds[1]):
				print(self.positions[row][col][0]," ",end="")
			print()

class NPC:
	def __init__(self,name="An NPC",x=0,y=0,behavior="Wander"):
		self.x=x
		self.y=y
		self.type="NPC"
		self.name=name
		self.behavior=behavior
		self.solid=True

	def move(self,bounds,*objects):
		TerminalExplorerAIs.movement(self,bounds,objects)


class Object:
	def __init__(self,name="An Object",x=0,y=0,solid=True):
		self.x=x
		self.y=y
		self.type="Object"
		self.name=name
		self.solid=True


