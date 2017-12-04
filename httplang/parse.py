import tokenize
import sys

global line
line = 0

class AST: 
    def __init__(self, left, right, tt, lexeme, l):
        self.left = left
        self.right = right
        self.token_type = tt
        self.lexeme = lexeme
        self.line = l
        
def Program(tokens):
    global line
    for token in tokens:
        tt = token['tokenType']
        if tt == "DO":
            line += 1
            yield do(tokens) 
        elif tt == "SET":
            line += 1
            yield set_(tokens)
        elif tt == "SHOW":
            line += 1
            yield show(tokens)
        elif tt == "LABEL":
            line += 1
            yield label(tokens)
        elif tt == "GOTO":
            line += 1
            yield goto(tokens)
        elif tt == "CONDITION":
            line += 1
            yield condition(tokens)
        else:
            sys.exit("Parse Error: Don't know what to do with {} line {}".format(token, line))
def condition(tokens):
    condition_expr = expr(tokens)
    goto_part = goto(tokens)

def do(tokens):
    pass

def set_(tokens):
    pass

def expr(tokens):
    pass

def show(tokens):
    variable_name = global_var(tokens)
    return AST(variable_name, None, "SHOW", None, line)

def label(tokens):
    label_name = string(tokens)
    return AST(label_name, None, "LABEL", None, line)

def goto(tokens):
    pass

def string(tokens):
    string_val = tokens.next()
    if string_val['tokenType'] != "STRING":
        sys.exit("Parse Error: {} is not a STRING line {}".format(string_val['lexeme'], line))
    return AST(None, None, string_val['tokenType'], string_val['lexeme'], line)

def integer(tokens):
    pass

def global_var(tokens):
    variable_val = tokens.next()
    if variable_val['tokenType'] == "GLOBAL_VAR":
        sys.exit("Parse Error: {} is not a GLOBAL_VAR line {}".format(variable_val['lexeme'], line))
    return AST(None, None, variable_val['tokenType'], variable_val['lexeme'], line)

if __name__ == "__main__":
    print list(Program(tokenize.getTokens(open("test.httpl"))))

