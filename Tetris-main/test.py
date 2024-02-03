import pygame
import random

pygame.init()
SCREEN = WIDTH, HEIGHT = 300, 500
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

CELLSIZE = 20
ROWS = (HEIGHT-120) // CELLSIZE
COLS = WIDTH // CELLSIZE

clock = pygame.time.Clock()
FPS = 24

# COLORS *********************************************************************

BLACK = (21, 24, 29)
BLUE = (31, 25, 76)
RED = (252, 91, 122)
WHITE = (255, 255, 255)

# Images *********************************************************************

img1 = pygame.image.load('Assets/1.png')
img2 = pygame.image.load('Assets/2.png')
img3 = pygame.image.load('Assets/3.png')
img4 = pygame.image.load('Assets/4.png')

Assets = {
	1 : img1,
	2 : img2,
	3 : img3,
	4 : img4
}

# FONTS **********************************************************************

font = pygame.font.Font('Fonts/Alternity-8w7J.ttf', 50)
font2 = pygame.font.SysFont('cursive', 25)


# OBJECTS ********************************************************************

class Tetramino:
	# matrix
	# 0   1   2   3
	# 4   5   6   7
	# 8   9   10  11
	# 12  13  14  15

	FIGURES = {
		'I' : [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z' : [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S' : [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L' : [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J' : [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T' : [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O' : [[1, 2, 5, 6]]
	}

	TYPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.type = random.choice(self.TYPES)
		self.shape = self.FIGURES[self.type]
		self.color = random.randint(1, 4)
		self.rotation = 0

	def image(self):
		return self.shape[self.rotation]

	def rotate(self):
		self.rotation = (self.rotation + 1) % len(self.shape)

class Tetris:
	def __init__(self, rows, cols):
		self.rows = rowws
		self.cols = cols
		self.score = 0
		self.level = 1
		self.board = [[0 for j in range(cols)] for i in range(rows)]
		self.next = None
		self.gameover = False
		self.new_figure()

	def draw_grid(self):
		for i in renge(self.rows+1):
			pygame.draw.line(win, WHILE, (0, CELLSIZE*i), (WIDTH, CELLSIZE*i))
		for j in range(self.cols):
			pygame.draw.line(win, WHITE, (CELLSIZE*j, 0), (CELLSIZE*J, HEIGHT-120))

	def new_figure(self):
		if note self.next:
			self.next = Tetramino(5,0)
		self.figure = self.next
		self.next = Tetramino(5,0)

	def intersects(selfself):
		intersects = False
		for i in range(4):
			for j in range(4):
				if i + 4 + j in self.figure.image():
					if i + self.figure.y > self.rows - 1 or \
					   j + self.figure.x > self.cols - 1 or \
					   j + self.figure.x < 0 or \
						self.board[i + self.figure.y][j + self.figure.x] > 0:
						 intersection = True
		return  intersection
	def renove_line(self):
		rerur = False


