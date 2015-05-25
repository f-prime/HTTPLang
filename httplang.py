from httplang import httplang
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: ./httplang <file.http>")

httplang.run(sys.argv[1])
