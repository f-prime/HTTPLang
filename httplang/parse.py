import utils
import sys

#handles lines of code in a list
def listParse(code,loops = 1):
    #fufill loops
    for i in range(loops):
        #set loop status variable
        loopStatus = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[]}
        #iterate through lines in the code
        for lineNumber, line in code:
            #set the global lines variables (add one because line count starts at one)
            utils.lines = lineNumber
            #hand off line to loopCheckThenParse
            loopStatus = loopCheckThenParse(lineNumber,line,loopStatus)

#checks for loops and normal parses otherwise    
#WARNING: NEED WAY TO HANDLE FORGOTTEN ENDLOOPS
def loopCheckThenParse(lineNumber,line,loopStatus):
    #check and remove comments
    line = line.split("#", 1)
    line = line[0].split("//",1)
    line = line[0]
    #split line
    splitLine = line.split()
    #ignore empty/blank lines
    if len(splitLine) < 1 or line == "\n":
        return (loopStatus)
                
    #handle loop begins
    if splitLine[0] == "loop":
        #increase the loop depth
        loopStatus['loopDepth'] += 1
        #if this is the first/root loop, make this the rootLoopLength
        if loopStatus['loopDepth'] == 1:
            #check we have precisely one argument
            if len(splitLine) != 2:
                sys.exit("Loop Error, loop requires exactly one argument on line {0}".format(utils.lines))
            #set rootLoopLength handling for non-ints
            try:
                loopStatus['rootLoopLength'] = int(splitLine[1])
            except ValueError:
                sys.exit("Loop error on line {0}. Loop amount must be integer not '{1}'.".format(utils.lines, splitLine[1]))
        else:
        #otherwise add this loop to the loop code
            loopStatus['loopCode'].append( (lineNumber,line) )
    #handle loop ends
    elif splitLine[0] == "endloop":
        #handle if endloop has no corresponding loop
        if loopStatus['loopDepth'] == 0:
            sys.exit("Loop error on line {0}. endloop has no corresponding loop to begin from.".format(utils.lines))
        #decrease loop depth
        loopStatus['loopDepth'] -= 1
        #parse the loopCode if this is the end of the rootLoop
        if loopStatus['loopDepth'] == 0:
            listParse(loopStatus['loopCode'],loopStatus['rootLoopLength'])
            #clear the loop variables
            loopStatus['loopCode'] = []
        else:
        #otherwise add it to the loop code
            loopStatus['loopCode'].append( (lineNumber,line) )
    else:
        #if we are in a loop, add this line to the loop code
        if loopStatus['loopDepth'] != 0:
            loopStatus['loopCode'].append( (lineNumber,line) )
        else:
        #otherwise go ahead and evaluate it
            eval_(line)
    #return loop status info
    return loopStatus               

def eval_(line):
    line = line.split()
    if line[0] in utils.keywords:
        utils.keywords[line[0]](line)
    else:
        sys.exit("Incorrect key word '{0}' on line {1}".format(line[0], utils.lines))

