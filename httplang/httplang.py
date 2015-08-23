import parse
import sys
import utils
import repl

def main():
    if len(sys.argv) < 2:
        repl.enterREPL()
        sys.exit()
    inputFile = sys.argv[1]
    run(inputFile)

def run(file_):
    with open(file_, 'rb') as file:
        #pass enumerated file so we can get line numbers starting at 1
        parse.preParse(enumerate(file,1))
    return utils.baseVariables

if __name__ == "__main__":
    main()
