import utils
import sys
import preEval

#handles lines of code in a list
def listParse(code,loops = 1):
    #fufill loops
    for i in range(loops):
        #set loop status variable
        #NOTE: PROBABLY SHOULD CHANGE TO NAMEDTUPLE
        lineInfo = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[],
                  'line':"",
                  'lineNumber':0,
                  'splitLine' : []}
        #iterate through lines in the code
        for lineNumber, line in code:
            #update the lineInfo variable
            lineInfo['line'] = line
            lineInfo['lineNumber'] = lineNumber
            #set the global lines variables (add one because line count starts at one)
            utils.lines = lineNumber
            #hand off line to parse
            lineInfo = parse(lineInfo)

#parses single line of code
def parse(lineInfo):
    
    #remove comments
    lineInfo['line'] = preEval.removeComments(lineInfo['line'])
    
    #split line
    lineInfo['splitLine'] = lineInfo['line'].split()
    
    #ignore empty/blank lines
    if len(lineInfo['splitLine']) < 1 or lineInfo['line'] == "\n":
        return lineInfo   
    
    #handle loops and other preEval stuff
    firstWord = lineInfo['splitLine'][0]
    if firstWord in preEval.keywords:
        lineInfo = preEval.keywords[firstWord](lineInfo)
    
    #handle regular code
    else:
    
        #if we are in a loop, add this line to the loop code
        if lineInfo['loopDepth'] != 0:
            lineInfo['loopCode'].append( (lineInfo['lineNumber'],lineInfo['line']) )
        
        #otherwise go ahead and evaluate it
        else:
            eval_(lineInfo['splitLine'])
            
    #return loop status info
    return lineInfo               

#evaluates a line of code 
# (eval_ differs from parse in that parse handles loops and comments and then pases the lines to eval_ )
def eval_(splitLine):
    if splitLine[0] in utils.keywords:
        utils.keywords[splitLine[0]](splitLine)
    else:
        sys.exit("Incorrect key word '{0}' on line {1}".format(splitLine[0], utils.lines))

