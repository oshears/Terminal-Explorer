from random import randrange
from os import system

def movement(self,bounds,objects):


	if self.behavior=="Wander":

			horV=randrange(0,2)

			if horV==0:
				xMove=randrange(0,2)

				if xMove == 0:
					xMove = -1

				xGood=True

				for item in objects:
					if (str(type(item))=="<class 'list'>"):
						for subItems in item:
							if self.x+xMove==subItems.x and self.y==subItems.y:
								xGood=False
					else:
						if self.x+xMove==item.x and self.y==item.y:
							xGood=False

				if xGood:
					if self.x!=0 and self.x!=bounds[1]-1:
						self.x+=xMove
					if self.x==0 and xMove>0:
						self.x+=xMove
					if self.x==bounds[1]-1 and xMove<0:
						self.x+=xMove

			elif horV==1:
				yMove=randrange(0,2)

				if yMove == 0:
					yMove = -1

				yGood=True

				for item in objects:
					if (str(type(item))=="<class 'list'>"):
						for subItems in item:
							if self.y+yMove==subItems.y and self.x==subItems.x:
								yGood=False
					else:
						if self.y+yMove==item.y and self.x==item.x:
							yGood=False

				if yGood:
					if self.y!=0 and self.y!=bounds[0]-1:
						self.y+=yMove
					if self.y==0 and yMove>0:
						self.y+=yMove
					if self.y==bounds[0]-1 and yMove<0:
						self.y+=yMove


def findNearby(self,*objects):
	self.nearby=[]
	for item in objects:
		if (str(type(item))=="<class 'list'>"):
			for subItems in item:
				#Right
				if (self.x+1==subItems.x and self.y==subItems.y):
					self.nearby.append(subItems)
				#Left
				elif (self.x-1==subItems.x and self.y==subItems.y):
					self.nearby.append(subItems)
				#Bottom Right
				elif (self.x+1==subItems.x and self.y+1==subItems.y):
					self.nearby.append(subItems)
				#Bottom
				elif (self.x==subItems.x and self.y+1==subItems.y):
					self.nearby.append(subItems)
				#Top Left
				elif (self.x-1==subItems.x and self.y-1==subItems.y):
					self.nearby.append(subItems)
				#Top
				elif (self.x==subItems.x and self.y-1==subItems.y):
					self.nearby.append(subItems)
				#Bottom Left
				elif (self.x-1==subItems.x and self.y+1==subItems.y):
					self.nearby.append(subItems)
				#Top Right
				elif (self.x+1==subItems.x and self.y-1==subItems.y):
					self.nearby.append(subItems)
		else:
			#Right
			if (self.x+1==item.x and self.y==item.y):
				self.nearby.append(item)
			#Left
			elif (self.x-1==item.x and self.y==item.y):
				self.nearby.append(item)
			#Bottom Right
			elif (self.x+1==item.x and self.y+1==item.y):
				self.nearby.append(item)
			#Bottom
			elif (self.x==item.x and self.y+1==item.y):
				self.nearby.append(item)
			#Top Left
			elif (self.x-1==item.x and self.y-1==item.y):
				self.nearby.append(item)
			#Top
			elif (self.x==item.x and self.y-1==item.y):
				self.nearby.append(item)
			#Bottom Left
			elif (self.x-1==item.x and self.y+1==item.y):
				self.nearby.append(item)
			#Top Right
			elif (self.x+1==item.x and self.y-1==item.y):
				self.nearby.append(item)
	return self.nearby

def makeRelate(self,*objects):
	for item in objects:
		if (str(type(item))=="<class 'list'>"):	
			for subItems in item:
				if subItems in self.nearby:
					if subItems in self.relate:
						self.relate[subItems]+=1
					else:
						self.relate.update({subItems:1})
		else:
			if item in self.nearby:
				if item in self.relate:
					self.relate[item]+=1
				else:
					self.relate.update({item:1})
	return self.relate
