# to pick random colors
from random import choice

# * * * * * * * * * * * * * * * * COLORS * * * * * * * * * * * * * * * * 
# the colors for the rod, the title board
COLORS = ['DarkGoldenrod4', 'DarkOliveGreen4', 'DarkOrange4', 'DarkOrchid4', 'DarkSeaGreen4', 'DarkSlateGray4', 'MediumPurple4', 'maroon4', 'VioletRed4', 'thistle4', 'coral4', 'LemonChiffon4', 'DeepSkyBlue4', 'yellow4', 'OliveDrab4', 'RoyalBlue4', 'PeachPuff4', 'cornsilk4']
# the colors for the disks and the disks
COLORS2  = ['gainsboro', 'floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose']
# to use the colors since they will be poped onece used by the disks to avoid color redundancy
BACKUP = COLORS[:]

# * * * * * * * * * * * * * * * * ROD * * * * * * * * * * * * * * * * 
# default rod number for the tower of honoi is 3, although it can work for larger rods as well
ROD_NUMBER = 3

# * * * * * * * * * * * * * * * * LINE * * * * * * * * * * * * * * * *
# the color of the thin black line under the rods
LINE_COLOR = 'black'

# * * * * * * * * * * * * * * * * SCREEN * * * * * * * * * * * * * * * *
# the size of the playing screen
HEIGHT = 600
WIDTH = 800

# * * * * * * * * * * * * * * * * SCREEN * * * * * * * * * * * * * * * *
# the default location to lay out the rods
DEFAULT_Y_LOCATION = -1 * HEIGHT//4 + 50
DEFAULT_X_LOCATION = [-1 * WIDTH//4, 0, WIDTH//4]
BOTTOM = DEFAULT_Y_LOCATION

# * * * * * * * * * * * * * * * * FONT * * * * * * * * * * * * * * * * *
# the font and alignment for the title board
ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'normal')