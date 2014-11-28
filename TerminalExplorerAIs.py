from random import randrange

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