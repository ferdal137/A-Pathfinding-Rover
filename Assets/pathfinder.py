import pygame, sys 
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

objectives = [(37,1),(25,20),(1,20)] #Chance the points here
start = [(1,1)] #Chance the start point here

class Pathfinder:

	def __init__(self,matrix):

		# setup
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)
		

		# pathfinding
		self.path = []
		self.object1 = pygame.sprite.GroupSingle(Objective1(self.empty_path))
		self.object2 = pygame.sprite.GroupSingle(Objective2(self.empty_path))
		self.object3 = pygame.sprite.GroupSingle(Objective3(self.empty_path))
		self.rover = pygame.sprite.GroupSingle(Rover(self.empty_path))


	def empty_path(self):
		self.path = []


	def create_path(self):

		points = [(37,1),(25,20),(1,20)]  #Chance the points here
		ends = []
		lens = []
		starts = [(1,1)]  #Chance the start point here
		self.paths = []

		aux = 0

		for point in range(len(points)):

			# start
			start_x, start_y = starts[0]
			start = self.grid.node(start_x,start_y)

			# end
			for i in range(len(points)):
				end = self.grid.node((points[i])[0],(points[i])[1]) 
				ends.append(end)

			finder = AStarFinder(diagonal_movement = DiagonalMovement.always)

			# path
			for i in range(len(ends)):
				self.path,_ = finder.find_path(start,ends[i],self.grid)
				self.grid.cleanup()
				path = self.path
				lens.append(len(path))
			
			obj = ends[lens.index(min(lens))]
			index = lens.index(min(lens))

			self.path,_ = finder.find_path(start,obj,self.grid)
			self.grid.cleanup()
			self.paths.append(self.path)
			ends.remove(obj)
			lens.clear()
			ends.clear()
			starts.clear()
			starts.append(points[index])
			points.remove(points[index])

			if self.path:
				colors = ["#c2c2c2","#828282","#000000"]    
				po = []
				for point in self.path:
					x = (point[0] * 32) + 16
					y = (point[1] * 32) + 16
					po.append((x,y))

				pygame.draw.lines(screen,colors[aux],False,po,5)

				aux += 1
		

	def update(self):
		self.create_path()
		self.object1.draw(screen)
		self.object2.draw(screen)
		self.object3.draw(screen)
		self.rover.draw(screen)
		

class Objective1(pygame.sprite.Sprite):
	def __init__(self,empty_path):
		super().__init__()
		self.image = pygame.image.load('objective.png').convert_alpha()
		self.rect = self.image.get_rect(center = (((objectives[0])[0])*32+16,((objectives[0]))[1]*32+16))

class Objective2(pygame.sprite.Sprite):
	def __init__(self,empty_path):
		super().__init__()
		self.image = pygame.image.load('objective.png').convert_alpha()
		self.rect = self.image.get_rect(center = (((objectives[1])[0])*32+16,((objectives[1]))[1]*32+16)) 

class Objective3(pygame.sprite.Sprite):
	def __init__(self,empty_path):
		super().__init__()
		self.image = pygame.image.load('objective.png').convert_alpha()
		self.rect = self.image.get_rect(center = (((objectives[2])[0])*32+16,((objectives[2]))[1]*32+16)) 

class Rover(pygame.sprite.Sprite):
	def __init__(self,empty_path):
		start_x, start_y = start[0]
		super().__init__()
		self.image = pygame.image.load('rover.png').convert_alpha()
		self.rect = self.image.get_rect(center = ((start_x*32)+16,(start_y*32)+16))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()

# game setup
bg_surf = pygame.image.load('map1.png').convert()

matrix = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

pathfinder = Pathfinder(matrix)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pathfinder.create_path()

	screen.blit(bg_surf,(0,0))
	pathfinder.update()

	pygame.display.update()
	clock.tick(60)