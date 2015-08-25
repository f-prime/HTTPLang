import sys
import utils
import parse

#handles "loop" Keyword
def loop(lineInfo):
    #increase the loop depth
    lineInfo['loopDepth'] += 1
    #if this is the first/root loop, make this the rootLoopLength
    if lineInfo['loopDepth'] == 1:
        #check we have precisely one argument
        if len(lineInfo['splitLine']) != 2:
            sys.exit("Loop Error, loop requires exactly one argument on line {0}".format(utils.lines))
        #set rootLoopLength handling for non-ints
        try:
            lineInfo['rootLoopLength'] = int(lineInfo['splitLine'][1])
        except ValueError:
            sys.exit("Loop error on line {0}. Loop amount must be integer not '{1}'.".format(utils.lines, lineInfo['splitLine'][1]))
    else:
    #otherwise add this loop to the loop code
        lineInfo['loopCode'].append( (lineInfo['lineNumber'],lineInfo['line']) )
        
    #return the new lineInfo
    return lineInfo
        
#handles "endloop" keyword
def endloop(lineInfo):
    #handle if endloop has no corresponding loop
    if lineInfo['loopDepth'] == 0:
        sys.exit("Loop error on line {0}. endloop has no corresponding loop to begin from.".format(utils.lines))
    #decrease loop depth
    lineInfo['loopDepth'] -= 1
    #parse the loopCode if this is the end of the rootLoop
    if lineInfo['loopDepth'] == 0:
        parse.listParse(lineInfo['loopCode'],lineInfo['rootLoopLength'])
        #clear the loop variables
        lineInfo['loopCode'] = []
    else:
    #otherwise add it to the loop code
        lineInfo['loopCode'].append( (lineInfo['lineNumber'],lineInfo['line']) )
   
    #return the new lineInfo
    return lineInfo

def removeComments(line):
    line = line.split("#", 1)
    line = line[0].split("//",1)
    return line[0]

#keywords for preParse
keywords = {
    "loop" : loop,
    "endloop" : endloop
}