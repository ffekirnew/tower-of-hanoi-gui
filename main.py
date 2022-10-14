from turtle import Screen
from disk import DiskArranger
from commons import *
from graphics import Graphics

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("The Towers Of Hanoi! by Fikernew Birhanu.")

graphics = Graphics()

def solve(n, from_peg, to_peg, through_peg):
	if n > 0:
		solve(n-1, from_peg, through_peg, to_peg)
		disk_arranger.move(from_peg, to_peg)
		graphics.titleboard.update()
		solve(n-1, through_peg, to_peg, from_peg)

while True:
	COLORS = BACKUP[:]

	screen.clear()
	screen.bgcolor(choice(COLORS2))
	graphics = Graphics()

	number_of_disks = int(screen.numinput("Number of Disks", "How many disks do you want to watch?", 3, 2, 10))
	disk_arranger = DiskArranger(number_of_disks)

	screen.textinput("Start?", f"{number_of_disks} disks have been setup, should we start?")
	solve(number_of_disks, 0, 2, 1)

	user_choice = screen.textinput("Done!", "Wanna do this again?\n(Type anything with an 'N' to end here.)")
	if 'N' in user_choice: break