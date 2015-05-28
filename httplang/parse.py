import utils
import sys

def parse(line):
    if line == "\n": # There was an error where blank lines were causing the program to crash
        return
    utils.lines += 1
    line = line.split()
    if line[0] in utils.keywords:
        if utils.inLoop and not utils.inRecursionForLoop and line[0] != "endloop":
            utils.loopCode.append(' '.join(line))
        utils.keywords[line[0]](line)
    else:
        sys.exit("Incorrect key word '{0}' on line {1}".format(line[0], utils.lines))

