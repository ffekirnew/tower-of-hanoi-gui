from turtle import Turtle
from commons import *
from random import choice

class Disk(Turtle):
	"""
	This is the class used to generate the disks that go on the rods
	initializes the disk to be created and calculates what the disk should look like based on the total disks that will go on the rod
	@n: the total number of rods to go on the rod
	@disk_size: the size of the particular disk
	"""
	def __init__(self, n: int, disk_size: int) -> None:
		super().__init__()
		self.shape("square")
		self.shapesize(1, (n - disk_size) * 2)
		self.show_color = choice(COLORS)
		COLORS.remove(self.show_color)
		self.color(self.show_color)
		self.speed(2)

class DiskArranger:
	"""
	This class will arrange the disks onto the screen
	@n: is the number of disks to be put on the starting rod
	"""
	def __init__(self, n: int) -> None:
		self.n = n
		self.rods = [[], [], []]
		self.initialize()

	def initialize(self) -> None:
		"""
		reinitializes the set incase the user wants to continue watching the show
		"""
		for disk_num in range(self.n):
			new_disk = Disk(self.n, disk_num);
			new_disk.speed('fastest')
			new_disk.penup()
			self.animate_move(new_disk, 0)
			new_disk.speed(2)
			self.rods[0].append(new_disk)
		
	def move(self, from_peg: int, to_peg: int) -> None:
		"""
		implements the standard tower of hanoi algorithm https://en.wikipedia.org/wiki/Tower_of_Hanoi
		@from_peg: the peg from which the disk is to be moved (an int from 0 - 2 usually)
		@to_peg: the peg to which the disk needs to be moved to
		"""
		disk = self.rods[from_peg][-1]
		self.animate_move(disk, to_peg)
		self.rods[to_peg].append(self.rods[from_peg].pop())

	def animate_move(self, object, destination: int):
		"""
		animates the move of the disks over the pegs
		@object: optional[Turtle: the disk to be moved
		@destination: the destination peg
		"""
		object.goto(object.xcor(), 10)
		object.goto(DEFAULT_X_LOCATION[destination], object.ycor())
		object.goto(object.xcor(), -190 + len(self.rods[destination]) * 20)