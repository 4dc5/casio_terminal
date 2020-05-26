Make a configurable display environment for the Casio fx-CG50.

To use, do this in your file:

from terminal.py import *

term=Terminal()

term.xprint("String to display")

For different colors, try for example:

term=Terminal(bg=(0,255,255),fg=(255,0,0))

Note that this package relies on the casioplot package which was added to version 3.40 of the OS. If you're on an older version, you'll need to update: https://edu.casio.com/download/index.php

-- 
4dc5.com
