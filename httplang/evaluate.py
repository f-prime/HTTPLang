import operator
import parse 
import tokenize
import global_data
import make_request

operators = {
    "==":operator.eq,
    "!=":operator.ne,
    ">=":operator.ge,
    "<=":operator.le,
    ">":operator.gt,
    "<":operator.lt
}


def evaluate(ast):
    ast = list(ast)
    switch = {
        "DO":do,
        "SET":set_,
        "SHOW":show,
        "GOTO":goto,
        "CONDITION":condition
    }
    while global_data.line_on < len(ast):
        on = ast[global_data.line_on]
        tt = on.token_type
        if switch.get(tt):
            switch[tt](on)
        global_data.line_on += 1

def do(line):
    method = line.left.lexeme
    path = line.right.lexeme
    switch = {
        "GET":make_request.GET,
        "POST":make_request.POST,
        "PUT":make_request.PUT,
        "DELETE":make_request.DELETE,
        "PATCH":make_request.PATCH
    }
    switch[method](path)

def set_(line):
    global_var = line.left.lexeme
    val = line.right.token_type
    if val == "GLOBAL":
        val = global_data.GLOBALS[line.right.lexeme]
    elif val == "STRING":
        val = line.right.lexeme
    global_data.GLOBALS[global_var] = val

def show(line):
    if line.left.token_type == "GLOBAL":
        print(global_data.GLOBALS[line.left.lexeme])
    elif line.left.token_type == "STRING":
        print(line.left.lexeme)

def goto(line):
    global_data.line_on = global_data.labels[line.left.lexeme]

def condition(line):
   condition = line.left.lexeme
   larg = line.left.left.lexeme
   rarg = line.left.right.lexeme
   if operators[condition](larg, rarg):
       goto(line.right)

if __name__ == "__main__":
    f = "test.httpl"
    tokens = tokenize.getTokens(open(f))
    evaluate(parse.program(tokens))

