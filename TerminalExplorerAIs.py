def movement():
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