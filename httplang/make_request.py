try:
    import urllib2 as urllib
except:
    import urllib.request as urllib
import global_data
import sys
from global_data import GLOBALS

def setValues(response):
    GLOBALS['RESPONSE'] = response.read()
    GLOBALS['STATUS'] = response.code
    GLOBALS['SETCOOKIE'] = response.info()['set-cookie']

def getURL():
    url = GLOBALS['URL']
    if not url:
        sys.exit("Variable Error: URL is not set line {}".format(global_data.line_on))
    return url   

def getOpener():
    opener = urllib.build_opener()
    opener.addheaders.append(('Cookie', GLOBALS['COOKIE']))
    opener.addheaders.append(("User-Agent", GLOBALS['USERAGENT']))
    return opener

def GET(path):
    url = getURL()
    opener = getOpener()
    request = urllib.Request(url)
    response = opener.open(request)
    setValues(response)

def POST(path):
    url = getURL()
    opener = getOpener()
    request = urllib.Request(url, GLOBALS['POSTDATA'])
    response = opener.open(request)
    setValues(response)

def PATCH(path):
    pass

def DELETE(path):
    pass

def PUT(path):
    pass
