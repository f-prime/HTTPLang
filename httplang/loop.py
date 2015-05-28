import utils
import sys
import parse

def loop(line):
    if utils.inLoop:
        return
    try:
        utils.inLoop = int(line[1])
    except ValueError:
        sys.exit("Loop error on line {0}. Loop amount must be integer not {1}.".format(utils.lines, line[1]))

def endloop(line):
    for x in range(utils.inLoop - 1): # Subtract one because when the loop is being analyzed for the first time it is actually being executed as well, so the firest iteration already happened.
        for code in utils.loopCode:
            utils.inRecursionForLoop = True
            parse.parse(code)
    utils.inRecursionForLoop = False
    utils.inLoop = False
    utils.loopCode = []
        
