import do
import setvar
import sys
import show
import getvalue
import loop

lines = 0

baseVariables = {

        "URL":None,
        "TMPCOOKIE":None,
        "COOKIE":None,
        "HTML":None,
        "POSTDATA":None,
        "USERAGENT":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",                                                                                           
        "STATUS":None,
        "VALUE":None,
        "LINKS":None,
}



keywords = {

        "do":do.do,
        "set":setvar.setvar,
        "show":show.show,        
        "getvalue":getvalue.getvalue,
        "loop":loop.loop,
        "endloop":loop.endloop,
}


inLoop = False
loopCode = []
inRecursionForLoop = False # This is a little bit of a hack... but it works. Will need to be modified in some way in the future, but loops work.

def typeDetermin(data):
    if data.startswith("$"):
        data = data[1:]
        if data in baseVariables:
            return baseVariables[data]
        else:
            sys.exit("Error on line {0}, variable ${1} is not a language variable.")

    return data
