import utils
import parse

def enterREPL():
    while(True):
        inp = raw_input(str(utils.lines) + "> ").strip()

        if(inp == "quit"):
            return

        parse.parse(inp)
