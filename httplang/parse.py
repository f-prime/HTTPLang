import tokenize
import sys
import global_data
import itertools

global line
line = 0

class AST: 
    def __init__(self, left, right, tt, lexeme, l):
        self.left = left
        self.right = right
        self.token_type = tt
        self.lexeme = lexeme
        self.line = l

def program(tokens):
    global line
    switch = {
        "DO":do,
        "SET":set_,
        "SHOW":show,
        "LABEL":label,
        "GOTO":goto,
        "CONDITION":condition
    }
    for token in tokens:
        tt = token['tokenType']
        if switch.get(tt):
            line += 1
            yield switch[tt](tokens) 
        else:
            sys.exit("Parse Error: Don't know what to do with {} line {}".format(token, line))

def condition(tokens):
    condition_expr = expr(tokens)
    goto_check = tokens.next()
    if goto_check['tokenType'] != "GOTO":
        sys.exit("Parse Error: goto expected after condition line {}".format(line))
    goto_part = goto(tokens)
    return AST(condition_expr, goto_part, "CONDITION", None, line)

def do(tokens):
    method_val = method(tokens)
    location = string(tokens)
    return AST(method_val, location, "DO", None, line)

def set_(tokens):
    global_val = global_var(tokens)
    tokens, copy = itertools.tee(tokens)
    type_check = copy.next()['tokenType']
    if type_check == "GLOBAL":
        location = global_var(tokens)
    else:
        location = string(tokens)
    return AST(global_val, location, "SET", None, line)

def expr(tokens):
    left_arg = tokens.next()
    if left_arg['tokenType'] not in ["GLOBAL", "STRING", "INTEGER"]:
        sys.exit("Parse Error: Invalid left argument {} line {}".format(left_arg['lexeme'], line))

    op = tokens.next()
    if op['tokenType'] != "OPERATOR":
        sys.exit("Parse Error: Invalid operator {} line {}".format(op['lexeme'], line))

    right_arg = tokens.next()
    if right_arg['tokenType'] not in ["GLOBAL", "STRING", "INTEGER"]:
        sys.exit("Parse Error: Invalid right argument {} line {}".format(right_arg["lexeme"], line))
    return AST(
            AST(None, None, left_arg['tokenType'], left_arg['lexeme'], line),
            AST(None, None, right_arg["tokenType"], right_arg['lexeme'], line),
            "OPERATOR",
            op['lexeme'],
            line)

def show(tokens):
    tokens, copy = itertools.tee(tokens)
    type_check = copy.next()['tokenType']
    if type_check == "STRING":
        variable_name = string(tokens)
    else:
        variable_name = global_var(tokens)
    return AST(variable_name, None, "SHOW", None, line)

def label(tokens):
    label_name = string(tokens)
    global_data.labels[label_name.lexeme] = line - 1
    return AST(label_name, None, "LABEL", None, line)

def goto(tokens):
    label_name = string(tokens)
    return AST(label_name, None, "GOTO", None, line)

def string(tokens):
    string_val = tokens.next()
    if string_val['tokenType'] != "STRING":
        sys.exit("Parse Error: {} is not a STRING line {}".format(string_val['lexeme'], line))
    return AST(None, None, string_val['tokenType'], string_val['lexeme'], line)

def integer(tokens):
    int_val = tokens.next()
    if int_val['tokenType'] != "INTEGER":
        sys.exit("TypeError: {} is not an INTEGER line {}".format(int_val['lexeme'], line))
    try:
        int_val['lexeme'] = int(int_val['lexeme'])
    except:
        sys.exit("Type Error: {} is not an INTEGER")
                
    return AST(None, None, int_val['tokenType'], int_val['lexeme'], line)

def method(tokens):
    method_val = tokens.next()
    if method_val['tokenType'] != "METHOD":
        sys.exit("Type Error: {} is not a METHOD line {}".format(method_val['lexeme'], line))
    return AST(None, None, method_val['tokenType'], method_val['lexeme'], line)

def global_var(tokens):
    variable_val = tokens.next()
    if variable_val['tokenType'] == "GLOBAL_VAR":
        sys.exit("Type Error: {} is not a GLOBAL_VAR line {}".format(variable_val['lexeme'], line))
    return AST(None, None, variable_val['tokenType'], variable_val['lexeme'], line)

if __name__ == "__main__":
    print(list(program(tokenize.getTokens(open("test.httpl")))))

