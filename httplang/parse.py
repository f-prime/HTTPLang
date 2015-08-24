import utils
import sys
import preEval

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
            #hand off line to parse
            loopStatus = parse(lineNumber,line,loopStatus)

#parses single line of code
def parse(lineNumber,line,loopStatus):
    
    #remove comments
    line = removeComments(line)
    
    #split line
    splitLine = line.split()
    
    #ignore empty/blank lines
    if len(splitLine) < 1 or line == "\n":
        return loopStatus    
    
    #handle loops and other preEval stuff
    if splitLine[0] in preEval.keywords:
        loopStatus = preEval.keywords[splitLine[0]](loopStatus)
    else:
    #handle regular code
    
        #if we are in a loop, add this line to the loop code
        if loopStatus['loopDepth'] != 0:
            loopStatus['loopCode'].append( (lineNumber,line) )
        else:
        #otherwise go ahead and evaluate it
            eval_(line)
            
    #return loop status info
    return loopStatus               

#evaluates a line of code 
# (eval_ defers from parse in that parse handles loops and comments and then pases the lines to eval_ )
def eval_(line):
    line = line.split()
    if line[0] in utils.keywords:
        utils.keywords[line[0]](line)
    else:
        sys.exit("Incorrect key word '{0}' on line {1}".format(line[0], utils.lines))

