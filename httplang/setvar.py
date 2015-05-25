import utils
import sys

def setvar(line):
    subKeys = {

            "URL":basicSet,
            "POSTDATA":post,
            "COOKIE":basicSet,
            "USERAGENT":basicSet,

    }
    
    try:
        subKeys[line[1]](line)
    except KeyError:
        sys.exit("Set error, no such key '{0}' on line {1}".format(line[1], utils.lines))

def basicSet(line):
    utils.baseVariables[line[1]] = utils.typeDetermin(' '.join(line[2:]))
    
def post(line):
    data = ' '.join(line[2:]).split(",")
    outDict = {}
    for x in data:
        x = x.split("=")
        outDict[x[0]] = ' '.join(x[1:])
        
    utils.baseVariables["POSTDATA"] = outDict

