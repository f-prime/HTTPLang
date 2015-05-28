import utils
from lxml import etree, html

def show(line):
    if line[1] == "$HTML":
        print etree.tostring(html.fromstring(utils.typeDetermin(line[1])), pretty_print=True)
    else:
        print utils.typeDetermin(line[1])
