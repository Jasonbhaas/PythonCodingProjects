def Evaluate_RPN_Expression(expr):
    intermediary_values = []
    operators = {
        "+" : lambda x, y : x + y,
        "-" : lambda x, y : x - y,
        "x" : lambda x, y : x * y,
        "/" : lambda x, y : int(x / y)
    }

    for character in expr.split(','):
        if character in operators:
            intermediary_values.append(operators[character](
                intermediary_values.pop, intermediary_values.pop
            ))
        else:
            intermediary_values.append(int(character))
    
    return intermediary_values[-1]


def Evaluate_Reverse_RPN_Expression(expr):
    intermediary_values = []
    intermediary_operator = []
    operators = {
        "+" : lambda y, x: x + y,
        "-" : lambda y, x: x - y,
        "x" : lambda y, x: x * y,
        "/" : lambda y, x: int(x / y)
    }

    for token in expr.split(','):
        if token in operators:
            intermediary_operator.append(operators[token])
        else:
            intermediary_values.append(int(token))
        if len(intermediary_values) == 2:
            intermediary_values.append(intermediary_operator.pop()(intermediary_values.pop(), intermediary_values.pop()))

    return intermediary_values[-1]


print(Evaluate_Reverse_RPN_Expression("+,4,5,x,8,-,5"))