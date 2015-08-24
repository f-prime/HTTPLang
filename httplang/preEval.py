
#handles "loop" Keyword
def loop(loopStatus):
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
        
#handles "endloop" keyword
def endloop(loopStatus):
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

def removeComments(line):
    line = line.split("#", 1)
    line = line[0].split("//",1)
    return line[0]

#keywords for preParse
keywords = {
    "loop" : loop,
    "endloop" : endloop
}