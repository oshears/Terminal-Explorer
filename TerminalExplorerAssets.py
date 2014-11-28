class Player:


	def __init__(self,x=0,y=0):
		self.name="Player"
		self.x=x
		self.y=y
		self.encounter=False


	def move(self,bounds,x=0,y=0,*objects):
		self.encounter=False

		if self.x!=0 and self.x!=bounds[0]-1:
			self.x+=x
		if self.y!=0 and self.y!=bounds[1]-1:
			self.y+=y
		if self.y==0 and y>0:
			self.y+=y
		if self.x==0 and x>0:
			self.x+=x
		if self.y==bounds[1]-1 and y<0:
			self.y+=y
		if self.x==bounds[0]-1 and x<0:
			self.x+=x

		for item in objects:
			if item.x==self.x and item.y==self.y and self.encounter==False:
				self.encounter=True

class Map:

	def __init__(self, *objects, scale=5, max_row=5, max_col=5):
		self.scale=scale
		self.positions=[]
		for x in range(max_col*self.scale):
			tempList=[]
			for y in range(max_row*self.scale):
				tempList.append(["X"])
			self.positions.append(tempList)

		self.bounds=(max_row*scale,max_col*scale)
		print(self.bounds)

		for item in objects:
			if item.name=="Player":
				self.positions[item.y][item.x]=["\x1b[36m@\x1b[0m"]
			if item.name=="Object":
				self.positions[item.y][item.x]=["\x1b[31m+\x1b[0m"]
		#self.positions[player.y][player.x]=["\x1b[31m@\x1b[0m"]
		self.display()


	def update(self,*objects):
		reserved_locations=[]
		for item in objects:
			for y in range(self.bounds[1]):
				for x in range(self.bounds[0]):
					if item.x == x and item.y==y:
						reserved_locations.append((y,x))
						if item.name=="Player":
							self.positions[y][x]=["\x1b[36m@\x1b[0m"]
						elif item.name=="Object":
							self.positions[y][x]=["\x1b[31m+\x1b[0m"]
					elif (y,x) not in reserved_locations:
						self.positions[y][x]=["X"]


	def display(self):
		for y in range(self.bounds[1]):
			for x in range(self.bounds[0]):
				print(self.positions[y][x][0],end="")
			print()

class NPC:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		self.name="NPC"


class Object:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		self.name="Object"


