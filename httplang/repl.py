import utils
import parse

def enterREPL():
    
    #loop state code
    loopStatus = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[]}
    
    #track inputed line count
    #because we want to start the count at zero, we start at -1
    inpLine = -1
    
    while(True):
        inp = raw_input(str(utils.lines) + "> ").strip()

        if(inp == "quit"):
            return
        
        #update line count
        inpLine += 1
        utils.lines = inpLine
        
        #handles loops and executes otherwise    
        loopStatus = parse.loopCheckThenParse(utils.lines,inp,loopStatus)