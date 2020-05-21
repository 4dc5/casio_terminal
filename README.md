Make a configurable display environment for the Casio fx-CG50.

To use, do this in your file:

from terminal.py import *

term=Terminal()

term.xprint("String to display")

For different colors, try for example:

term=Terminal(bg=(0,255,255),fg=(255,0,0))


-- 
4dc5.com
