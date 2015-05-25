import do
import setvar
import sys
import show
import getvalue

lines = 0

baseVariables = {

        "URL":None,
        "TMPCOOKIE":None,
        "COOKIE":None,
        "HTML":None,
        "POSTDATA":None,
        "USERAGENT":None,                                                                                                                                                                              
        "STATUS":None,
        "VALUE":None,

}



keywords = {

        "do":do.do,
        "set":setvar.setvar,
        "show":show.show,        
        "getvalue":getvalue.getvalue,

}


def typeDetermin(data):
    if data.startswith("$"):
        data = data[1:]
        if data in baseVariables:
            return baseVariables[data]
        else:
            sys.exit("Error on line {0}, variable ${1} is not a language variable.")

    return data
