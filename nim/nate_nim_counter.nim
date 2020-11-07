import system
from strutils import parseInt
var
    timesAround = 0
    start = readLine(stdin)
    count = 0
    tmpin = ""
while start == "":
    echo "Would you like to start? [y/n]? "
    start = readLine(stdin)
    case start
    of "y": break
    of "n": system.quit(130)
    else: echo "Not a valid answer."
while timesAround == 0:
    echo "How many times around would you like to go (Please enter a number) "
    try: timesAround = stdin.readLine.parseInt
    except: echo "aha fuck, not a int"
    finally: echo "Times around will be ", $timesAround
    case timesAround:
    of 0: system.quit(130)
    of 1..100: break
    else: discard
while timesAround > count:
    tmpin = readLine(stdin)
    if count == timesAround:
        var start = readLine(stdin)
        while start == "":
            echo "Would you like to go around again?"
            start = readLine(stdin)
            if start == "y": count = 0
    if tmpin == " ": inc count
    echo count
