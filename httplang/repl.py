import utils
import parse

def enterREPL():
    
    #loop state code
    loopStatus = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[]}
    
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

        #handles loops and executes otherwise    
        loopStatus = parse.loopCheckThenParse(utils.lines,inp,loopStatus)