import pygame
import tkinter as tk
from tkinter import messagebox
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("A-STAR!")

class Node():
	def __init__(self, x, y, parent, goal):
		self.x = x
		self.y = y
		self.parent = parent
		self.getcost(goal)
		

	def createchildren(self, goal):
		'''Creating and appending children to Open list when the node is not a wall or an already visited node'''
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x-25 and i.y == self.y:
				notwall = 0
		for i in Closed:
			if i.x == self.x-25 and i.y == self.y:
				notwall = 0
		if self.x-25 >= 0 and notwall:
			for i in Open:
				if self.x-25 == i.x and self.y == i.y:
					i.recomputeCost(self, goal, 'left')
					f = 1
					break
			if not f:
				Open.append(Node(self.x-25, self.y, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x and i.y == self.y+25:
				notwall = 0
		for i in Closed:
			if i.x == self.x and i.y == self.y+25:
				notwall = 0
		if self.y+25 < 500 and notwall:	
			for i in Open:
				if self.x == i.x and self.y+25 == i.y:
					i.recomputeCost(self, goal, 'down')
					f = 1
					break
			if not f:
				Open.append(Node(self.x, self.y+25, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x+25 and i.y == self.y:
				notwall = 0
		for i in Closed:
			if i.x == self.x+25 and i.y == self.y:
				notwall = 0
		if self.x+25 < 500 and notwall:
			for i in Open:
				if self.x+25 == i.x and self.y == i.y:
					i.recomputeCost(self, goal, 'right')
					f = 1
					break
			if not f:
				Open.append(Node(self.x+25, self.y, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x and i.y == self.y-25:
				notwall = 0
		for i in Closed:
			if i.x == self.x and i.y == self.y-25:
				notwall = 0
		if self.y-25 >= 0 and notwall:	
			for i in Open:
				if self.x == i.x and self.y-25 == i.y:
					i.recomputeCost(self, goal, 'up')
					f = 1
					break
			if not f:
				Open.append(Node(self.x, self.y-25, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x-25 and i.y == self.y-25:
				notwall = 0
		for i in Closed:
			if i.x == self.x-25 and i.y == self.y-25:
				notwall = 0
		if self.x-25 >= 0 and self.y-25 >= 0 and notwall:
			for i in Open:
				if self.x-25 == i.x and self.y-25 == i.y:
					i.recomputeCost(self, goal, 'leftup')
					f = 1
					break
			if not f:
				Open.append(Node(self.x-25, self.y-25, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x+25 and i.y == self.y-25:
				notwall = 0
		for i in Closed:
			if i.x == self.x+25 and i.y == self.y-25:
				notwall = 0
		if self.x+25 < 500 and self.y-25 >= 0 and notwall:
			for i in Open:
				if self.x+25 == i.x and self.y-25 == i.y:
					i.recomputeCost(self, goal, 'rightup')
					f = 1
					break
			if not f:
				Open.append(Node(self.x+25, self.y-25, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x-25 and i.y == self.y+25:
				notwall = 0
		for i in Closed:
			if i.x == self.x-25 and i.y == self.y+25:
				notwall = 0
		if self.x-25 >= 0 and self.y+25 < 500 and notwall:
			for i in Open:
				if self.x-25 == i.x and self.y+25 == i.y:
					i.recomputeCost(self, goal, 'leftdown')
					f = 1
					break
			if not f:
				Open.append(Node(self.x-25, self.y+25, self, goal))
		f=0
		notwall=1
		for i in walls:
			if i.x == self.x+25 and i.y == self.y+25:
				notwall = 0
		for i in Closed:
			if i.x == self.x+25 and i.y == self.y+25:
				notwall = 0
		if self.x+25 < 500 and self.y+25 < 500 and notwall:
			for i in Open:
				if self.x+25 == i.x and self.y+25 == i.y:
					i.recomputeCost(self, goal, 'rightdown')
					f = 1
					break
			if not f:
				Open.append(Node(self.x+25, self.y+25, self, goal))

		

	def recomputeCost(self, node, goal, dir):
		'''Recomputing the heuristic value for a node that is already present in the Open list, and choosing the value that has lesser heuristic(Closer to the goal)'''
		if dir=='left':
			temphcost = node.hcost+25
			tempgcost =  abs(goal.x-(node.x-25)) + abs(goal.y-node.y)
			tempfcost = temphcost + tempgcost
		elif dir=='right':
			temphcost = node.hcost+25
			tempgcost =  abs(goal.x-(node.x+25)) + abs(goal.y-node.y)
			tempfcost = temphcost + tempgcost
		elif dir=='up':
			temphcost = node.hcost+25
			tempgcost =  abs(goal.x-node.x) + abs(goal.y-(node.y-25))
			tempfcost = temphcost + tempgcost
		elif dir=='down':
			temphcost = node.hcost+25
			tempgcost =  abs(goal.x-node.x) + abs(goal.y-(node.y+25))
			tempfcost = temphcost + tempgcost
		elif dir=='leftup':
			temphcost = node.hcost+36
			tempgcost =  abs(goal.x-(node.x-25)) + abs(goal.y-(node.y-25))
			tempfcost = temphcost + tempgcost
		elif dir=='rightup':
			temphcost = node.hcost+36
			tempgcost =  abs(goal.x-(node.x+25)) + abs(goal.y-(node.y-25))
			tempfcost = temphcost + tempgcost
		elif dir=='leftdown':
			temphcost = node.hcost+36
			tempgcost =  abs(goal.x-(node.x-25)) + abs(goal.y-(node.y+25))
			tempfcost = temphcost + tempgcost
		elif dir=='rightdown':
			temphcost = node.hcost+36
			tempgcost =  abs(goal.x-(node.x+25)) + abs(goal.y-(node.y+25))
			tempfcost = temphcost + tempgcost
		if self.fcost > tempfcost:
			self.fcost = tempfcost
			self.parent = node

	def getcost(self, goal):
		'''Initial computation of the heuristic value'''
		if self.parent:
			self.hcost = self.parent.hcost+25
			self.gcost = abs(goal.x-self.x) + abs(goal.y-self.y)
			self.fcost = self.hcost + self.gcost
		else:
			if goal:
				self.hcost = 0
				self.gcost = abs(goal.x-self.x) + abs(goal.y-self.y)
				self.fcost = self.hcost + self.gcost
			else:
				self.hcost = 0
				self.gcost = 0
				self.fcost = 0


class Wall():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def drawWall(self):
		pygame.draw.rect(win, (255,255,255), (self.x, self.y, 25, 25))

def onsubmit():
	global start
	global End
	st = startBox.get().split(',')
	ed = endBox.get().split(',')
	start.x = int(st[0])
	start.y = int(st[1])
	end.x = int(ed[0])
	end.y = int(ed[1])
	window.quit()
	window.destroy()

end = Node(0, 0,0,0)
start = Node(0, 0, 0, end)

window = tk.Tk()
window.title('Enter')
label = tk.Label(window, text='Start(x,y): ')
startBox = tk.Entry(window)
label1 = tk.Label(window, text='End(x,y): ')
endBox = tk.Entry(window)

submit = tk.Button(window, text='Submit', command=onsubmit)

submit.grid(columnspan=2, row=3)
label1.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)


window.update()
tk.mainloop()



Open = []
Closed = []
walls = []

def drawcube():
	'''Drawing the grid'''
	for i in range(0,500,25):
		for j in range(0,500,25):
			pygame.draw.rect(win, (150,150,150), (i,j,25,25), 1)

def drawstartend(start, end):
	'''Drawing the start node and the end node'''
	pygame.draw.rect(win, (255,0,0), (start.x, start.y, 25, 25))
	pygame.draw.rect(win, (0,255,0), (end.x, end.y, 25, 25))

def getMin():
	'''Selecting the node that has the minimum heuristic value'''
	if len(Open) == 0:
		return 0
	minn = Open[0]
	for i in Open:
		if i.fcost < minn.fcost:
			minn = i
		elif i.fcost == minn.fcost:
			if i.gcost < minn.gcost:
				minn = i
	return minn


root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw()
messagebox.showinfo('Attention', 'Make obstuctions using mouse and press space to start') 

run = True

Open.append(start)

drawcube()

cost_font = pygame.font.Font(None, 15)

flagtostart = 0

while(run):
	pygame.time.delay(50)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
			run=False

	#Creating the walls
	if pygame.mouse.get_pressed()[0]:
		coord = pygame.mouse.get_pos()
		coord = ((coord[0]//25)*25, (coord[1]//25)*25)
		walls.append(Wall(coord[0], coord[1]))


	#press space to start
	k = pygame.key.get_pressed()
	if k[pygame.K_SPACE]:
		flagtostart = 1

	if flagtostart:
		cur = getMin()

		#Cant reach goal.
		if not cur:
			root = tk.Tk()
			root.attributes("-topmost", True)
			root.withdraw()
			messagebox.showinfo('OOPS!!', 'Goal not Found!! ')
			exit()

		pygame.draw.rect(win, (0,80,0), (cur.x,cur.y,25,25))
		cost_surf = cost_font.render(str(cur.fcost), 1, (255,255,255))
		win.blit(cost_surf, [cur.x+5,cur.y+10])

		#Goal Found.
		if cur.x == end.x and cur.y == end.y:
			print('Found goal!!')
			run = False
			break
		cur.createchildren(end)
		Open.remove(cur)
		Closed.append(cur)
		for i in Open:
			pygame.draw.rect(win, (0,200,0), (i.x,i.y,25,25))
			if i.parent.x == i.x-25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x,i.y+12),(i.x+5,i.y+12)])
			elif i.parent.x == i.x+25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+20,i.y+12),(i.x+25,i.y+12)])
			elif i.parent.y == i.y-25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+12,i.y),(i.x+12,i.y+5)])
			elif i.parent.y == i.y+25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+12,i.y+20),(i.x+12,i.y+25)])
			elif i.parent.x == i.x+25 and i.parent.y == i.y+25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+20,i.y+20),(i.x+25,i.y+25)])
			elif i.parent.x == i.x-25 and i.parent.y == i.y+25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+5,i.y+20),(i.x,i.y+25)])
			elif i.parent.x == i.x+25 and i.parent.y == i.y-25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+20,i.y+5),(i.x+25,i.y)])
			elif i.parent.x == i.x-25 and i.parent.y == i.y-25:
				pygame.draw.lines(win, (255,255,255), True, [(i.x+5,i.y+5),(i.x,i.y)])
			cost_surf = cost_font.render(str(i.fcost), 1, (255,255,255))
			win.blit(cost_surf, [i.x+5,i.y+10])
		print("length of Open: ", str(len(Open)))
		for i in Open:
			print("x,y: " + str(i.x) + "," + str(i.y) + " hcost:" + str(i.hcost) + " gcost:" + str(i.gcost) + " fcost:" + str(i.fcost))

	drawstartend(start, end)
	for i in walls:
		i.drawWall()
	pygame.display.update()


p = cur
counter = -1

#Backtracking and finding the route to the goal
while(p):
	pygame.draw.rect(win, (0,0,255), (p.x,p.y,25,25))
	p = p.parent
	counter += 1

pygame.display.update()
root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw()
messagebox.showinfo('Goal Found!', 'Distance to Goal: '+str(counter)) 

for e in pygame.event.get():
	if e.type == pygame.QUIT:
		exit()
	