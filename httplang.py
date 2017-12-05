from httplang import *
import sys
import os

if len(sys.argv) < 2:
    sys.exit("Usage: python httplang.py <file>.httpl")

if not os.path.exists(sys.argv[1]):
    sys.exit("No file names {}".format(sys.argv[1]))

evaluate.evaluate(parse.program(tokenize.getTokens(open(sys.argv[1]))))
