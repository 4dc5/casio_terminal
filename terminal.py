from casioplot import *  

# Make a configurable display environment for the Casio fx-CG50.
#
# To use, do this in your file:
# from terminal.py import *
# term=Terminal()
# term.xprint("String to display")
#
# For different colors, try for example:
# term=Terminal(bg=(0,255,255),fg=(255,0,0))

class Terminal:

  # Default to black background and green foreground. Set bg and/or fg to change this.
  def __init__(self,bg=(0,0,0),fg=(0,255,0)):
    self.scr=[] # The screen buffer
    self.bg=bg
    self.fg=fg
    self.rows=11 # Text rows
    self.cols=34 # Text columns
    self.clear()

  # Clear the screen.
  def clear(self):
    # We print the letter 'T' all over the screen. Do it as little as possible, for speed.
    for y in range(0,189,3):
      for x in range(0,3):
        draw_string(x,y,"T"*32,self.bg)    
    # We missed some pixels at the bottom of the screen, so fill them in now.
    for x in range(0,3):
      draw_string(x,189,"T"*32,self.bg)

  # Refresh the screen with whatever we have in the buffer.
  def refresh(self):
    self.clear()
    # We only want the number of rows we can fit on the screen, so truncate the buffer.
    self.scr=self.scr[-self.rows:]
    # Write the buffer rows to the screen.
    y=0
    for r in self.scr:
      draw_string(5,8+y*16,r,self.fg)
      y+=1
    show_screen()

  # Print a string on the screen.
  def xprint(self,s):
    s=str(s)
    self.scr.extend(self._lines(s))
    self.refresh()

  # Split a string into a number of lines that will fit within the screen width.
  def _lines(self,s):
    r=[]
    while len(s)>self.cols:
      r.append(s[:self.cols])
      s=s[-(len(s)-self.cols):]  
    if len(s)>0:
      r.append(s)
    return r    

