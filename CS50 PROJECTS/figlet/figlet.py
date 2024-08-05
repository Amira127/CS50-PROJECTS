from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fontlist=figlet.getFonts()
if len(sys.argv) ==1:
    input=input("Input:")
    randomFont = choice(fontlist)
    figlet.setFont(font=randomFont)
    print(f"Output: {figlet.renderText(input)}")

elif len(sys.argv) >= 3:
    if sys.argv[2] in fontlist and (sys.argv[1]=="-f" or sys.argv[1]=="--font") :
        input=input("Input:")
        figlet.setFont(font=sys.argv[2])
        print(f"Output: {figlet.renderText(input)}")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


