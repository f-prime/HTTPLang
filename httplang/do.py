import urllib2
import utils
import sys
from urllib import urlencode
import re

def do(line):
    subKeys = {

            "GET":get,
            "POST":post,

    }
    
    try:
        subKeys[line[1]](line)
    except KeyError:
        sys.exit("Do error, no such request '{0}' on line {1}".format(line[1], utils.lines))

def get(line):
    if not utils.baseVariables['URL']:
        sys.exit("Error on line {}, URL not set.".format(utils.lines))

    url = utils.baseVariables['URL'] + line[2]
    request = urllib2.Request(url)
    request = __setHeaders(request)
    try:
        data = urllib2.urlopen(request)
    except urllib2.HTTPError:
        sys.exit("Error on line {0} url {1} does not exist.".format(utils.lines, url))
    source = data.read()
    try:
        tmpcookie = data.info()['set-cookie']
        utils.baseVariables['TMPCOOKIE'] = tmpcookie
    except KeyError:
        pass
    utils.baseVariables["HTML"] = source
    utils.baseVariables['STATUS'] = data.getcode()
    utils.baseVariables['LINKS'] = re.findall(r'href=[\'"]?([^\'" >]+)', source)

def post(line):
    if not utils.baseVariables["URL"]:
        sys.exit("Error on line {}, URL not set.".format(utils.lines))
    if not utils.baseVariables["POSTDATA"]:
        sys.exit("POSTDATA must be set to do POST request, line {}".format(utils.lines))
    url = utils.baseVariables["URL"] + line[2]
    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    request = urllib2.Request(url, data=urlencode(utils.baseVariables["POSTDATA"]))
    request = __setHeaders(request)
    try:
        data = opener.open(request)
    except urllib2.HTTPError:
        sys.exit("Error on line {0} url {1} does not exist.".format(utils.lines, url))
    source = data.read()
    try:
        tmpcookie = data.info()["set-cookie"]
        utils.baseVariables["TMPCOOKIE"] = tmpcookie
    except KeyError:
        pass
    utils.baseVariables["HTML"] = source
    utils.baseVariables['STATUS'] = data.getcode()

def __setHeaders(request):
    if utils.baseVariables["COOKIE"]:
        request.add_header("Cookie", utils.baseVariables["COOKIE"])
    if utils.baseVariables["USERAGENT"]:
        request.add_header("User-Agent", utils.baseVariables['USERAGENT'])

    return request
