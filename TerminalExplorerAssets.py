from random import randrange

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
			elif item.name=="NPC":
				self.positions[item.y][item.x]=["\x1b[32m$\x1b[0m"]

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
						elif item.name=="NPC":
							self.positions[y][x]=["\x1b[32m$\x1b[0m"]
					elif (y,x) not in reserved_locations:
						self.positions[y][x]=["X"]


	def display(self):
		for y in range(self.bounds[1]):
			for x in range(self.bounds[0]):
				print(self.positions[y][x][0],end="")
			print()

class NPC:
	def __init__(self,x=0,y=0,behavior="Wander"):
		self.x=x
		self.y=y
		self.name="NPC"
		self.behavior=behavior

	def move(self,bounds,*objects):

		if self.behavior=="Wander":

			horV=randrange(0,2)

			if horV==0:
				xMove=randrange(0,2)

				if xMove == 0:
					xMove = -1

				xGood=True

				for item in objects:
					if self.x+xMove==item.x and self.y==item.y:
						xGood=False
						print("NPC has an issue moving horizontally with"+item.name)

				if xGood:
					if self.x!=0 and self.x!=bounds[0]-1:
						self.x+=xMove
					if self.x==0 and xMove>0:
						self.x+=xMove
					if self.x==bounds[0]-1 and xMove<0:
						self.x+=xMove

			elif horV==1:
				yMove=randrange(0,2)

				if yMove == 0:
					yMove = -1

				yGood=True

				for item in objects:
					if self.y+yMove==item.y and self.x==item.x:
						yGood=False
						print("NPC has an issue moving vertically with"+item.name)


				if yGood:
					if self.y!=0 and self.y!=bounds[1]-1:
						self.y+=yMove
					if self.y==0 and yMove>0:
						self.y+=yMove
					if self.y==bounds[1]-1 and yMove<0:
						self.y+=yMove
		


class Object:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		self.name="Object"


