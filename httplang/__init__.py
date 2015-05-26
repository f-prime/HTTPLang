from . import httplang
import sys

def console_main():
	if len(sys.argv) < 2:
	    sys.exit("Usage: ./httplang <file.http>")

	httplang.run(sys.argv[1])
