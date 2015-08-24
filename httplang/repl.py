import utils
import parse

def enterREPL():
    
    #loop state code
    lineInfo = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[],
                  'line':"",
                  'lineNumber':0,
                  'splitLine' : []}
    
    #track inputed line count
    inpLine = 0
    
    while(True):
        #update line count
        inpLine += 1
        utils.lines = inpLine
        
        #display prompt
        inp = raw_input(str(utils.lines) + "> ").strip()

        #handles quit directive
        if(inp == "quit"):
            return
            
        #update lineInfo
        lineInfo['line'] = inp
        lineInfo['lineNumber'] = utils.lines

        #parse the line  
        loopStatus = parse.parse(lineInfo)