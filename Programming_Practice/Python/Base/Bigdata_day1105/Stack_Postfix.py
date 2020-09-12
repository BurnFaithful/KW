def compute(operator, left_operand, right_operand):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand


def custom_eval(expr):
    stack = list()
    token_list = expr.split()

    for token in token_list:
        if token.isdecimal():
            stack.append(int(token))
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            result = compute(token, left_operand, right_operand)
            stack.append(result)
    return stack.pop()


# 식 변환을 할 때, 연산자에 스택을 넣는 규칙을 검사하기 위한 우선순위 반환
def priority(operator):
    if operator == '+' or operator == '-':
        return 0
    elif operator == '*' or operator == '/':
        return 1

    return -2


# 10 + 5 * 2 -> 10 5 2 * +
def infix_to_postfix(expr):
    postfix_stack = list()
    operator_stack = list()
    token_list = expr.split()

    for token in token_list:
        if token.isdecimal():
            postfix_stack.append(token)
        else:
            if not operator_stack:
                operator_stack.append(token)
                continue

            while operator_stack and priority(operator_stack[-1]) >= priority(token):
                postfix_stack.append(operator_stack.pop())

            operator_stack.append(token)

    while operator_stack:
        postfix_stack.append(operator_stack.pop())

    return ' '.join(postfix_stack)


if __name__ == "__main__":
    expression = input("식 입력(공백 필수) => ")
    postfix_expression = infix_to_postfix(expression)
    print(f"Infix : {expression} => Postfix : {postfix_expression} = {custom_eval(postfix_expression)}")