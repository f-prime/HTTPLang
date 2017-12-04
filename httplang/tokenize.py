import re
import sys

tokens = {
        "^do$":"DO",
        "^set$":"SET",
        "^GET$|^POST$|^PUT$|^DELETE$|^PATCH$":"METHOD",
        "^URL$|^TMPCOOKIE$|^COOKIE$|^HTML$|^POSTDATA$|^USERAGENT$|^STATUS$|^LINK$|^VALUE$":"GLOBAL",
        "^show$":"SHOW",
        "^if$":"CONDITION",
        "^label$":"LABEL",
        "^goto$":"GOTO",
        "==|!=|>=|<=":"OPERATOR",
        "\"(.*?)\"":"STRING",
        "[0-9]+":"INTEGER"
}

def getTokens(stream):
    token = ""
    line = 1
    for char in stream.read():
        if char == " " or char == "\n":
            for token_check in tokens:
                check = re.findall(token_check, token)
                if check:
                    token = ""
                    yield {
                            "lexeme":check[0],
                            "tokenType":tokens[token_check]
                          }
                    break
            else:
                sys.exit("Invalid Token: {} on line {}".format(token, line))
            if char == "\n":
                line += 1
        else:
            token += char

if __name__ == "__main__":
    print list(getTokens(open("test.httpl")))
