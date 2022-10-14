from turtle import Turtle
from commons import *	

class TitleBoard(Turtle):
	'''
	Object model for the title board displaying the title of the program.
	'''
	def __init__(self) -> None:
		super().__init__()
		self.speed('fastest')
		self.color(choice(COLORS))
		self.ht()
		self.penup()
		self.goto(0, HEIGHT//2 - 60)
		self.moves = 0
		self.display()
	
	def display(self):
		'''
		displays the title board after the turtle has been initialized
		'''
		self.clear()
		self.write(f"The Tower of Hanoi\nMoves: {self.moves}.", align=ALIGNMENT, font=FONT)

	def update(self):
		'''
		Updates the moves and redisplays the title board
		'''
		self.moves += 1
		self.display()

class Rod:
	"""
	object model representation of the rod, creates multiple rods as instructed by the user
	"""
	def __init__(self):
		self.list = []
		self.rod_number = ROD_NUMBER
		self.color = choice(COLORS)
		COLORS.remove(self.color)
		for i in range(self.rod_number):
			new_rod = Turtle()
			new_rod.ht()
			new_rod.shape('square')
			new_rod.speed('fastest')
			new_rod.color(self.color)
			new_rod.shapesize(10, 1)
			new_rod.penup()
			new_rod.goto(DEFAULT_X_LOCATION[i], BOTTOM)
			new_rod.st()
			self.list.append(new_rod)

class Line(Turtle):
	"""
	object model representation of the thin black line under the rods
	"""
	def __init__(self):
		super().__init__()
		self.speed('fastest')
		self.bottom = BOTTOM - 100
		self.color(LINE_COLOR)
		self.penup()
		self.ht()
		self.goto(-1 *  WIDTH // 2, self.bottom)
		self.pendown()
		self.goto(WIDTH//2, self.bottom)

class Graphics:
	'''
	a class to incorporate and handle the entire graphics
	'''
	def __init__(self):
		self.instance = 1
		self.line = None
		self.rods = None
		self.titleboard = None
		self.setup()

	def setup(self):
		self.titleboard = TitleBoard()
		self.line = Line()
		self.rods = Rod()