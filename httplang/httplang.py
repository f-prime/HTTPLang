import parse
import sys
import utils
import repl

def run(file_):
    with open(file_, 'rb') as file:
        for line in file:
            parse.parse(line)
    return utils.baseVariables

if __name__ == "__main__":
    if len(sys.argv) < 2:
        repl.enterREPL()
        sys.exit()
    inputFile = sys.argv[1]
    run(inputFile)
