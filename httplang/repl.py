import utils
import parse

def enterREPL():
    
    #loop state code
    loopStatus = {'loopDepth':0,
                  'rootLoopLength':0,
                  'loopCode':[]}
    
    while(True):
        inp = raw_input(str(utils.lines) + "> ").strip()

        if(inp == "quit"):
            return
        
        #update line count
        utils.lines += 1
        
        #handles loops and executes otherwise    
        loopStatus = parse.loopCheckThenParse(utils.lines,inp,loopStatus)