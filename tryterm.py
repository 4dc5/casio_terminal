from terminal import *

term=Terminal()

term.xprint("Short lines are OK.")
term.xprint("But long lines are OK too because they will be wrapped.")
term.xprint("It does not have to be text.")
term.xprint(42)
term.xprint("That is a number and it is OK.")

term.xprint("We handle scrolling too.")
for i in range(0,10):
  term.xprint(i)

term=Terminal(bg=(0,255,255),fg=(255,0,0))

term.xprint("But we can choose other colors too!")
