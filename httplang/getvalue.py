import sys
from lxml import html
import utils

def getvalue(line):
    if not utils.baseVariables['HTML']:
        sys.exit("HTML varable must be set before getvalue can be called. Line {}".format(utils.lines))
    subKeys = {
            "NAME":name,
            "ID":_id,
    }
    
    try:
        subKeys[line[1]](line)
    except KeyError:
        sys.exit("Getvalue error, no such key '{0}' on line {1}".format(line[1], utils.lines))


def name(line):
    source = html.fromstring(utils.baseVariables['HTML'])
    toFind = line[2]
    found = False
    for check in source.iter():
        try:
            if check.name == toFind:
                found = check.value
                break
        except AttributeError:
            continue

    if not found:
        sys.exit("Getvalue error, either no such NAME `{0}` in HTML, or HTTPLang could not find NAME in HTML. Line {1}".format(line[2], utils.lines))
    else:
        utils.baseVariables['VALUE'] = found

def _id(line):
    source = html.fromstring(utils.baseVariables['HTML'])
    try:
        utils.baseVarables['VALUE'] = source.get_element_by_id(line[2]).value
    except KeyError:
        sys.exit("Getvalue error, either no such ID `{0}` in HTML, or HTTPLang could not find ID in HTML. Line {1}".format(line[2], utils.lines))
