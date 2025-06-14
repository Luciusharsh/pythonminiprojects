def call_print(expression):
    print("[ ",end='')
    print(','.join(str(i) for i in expression),end='')
    print(" ]")
def postfix_to_solution(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    if stack:
        print("Result:", stack[0])
def infix_to_postfix(infix):
    postfix = []
    exp_hold = []
    symbols = ['/','*','+','-']
    for i in infix:
        if i not in symbols:
            postfix.append(i)
        else:
            if not exp_hold:
                exp_hold.append(i)
            elif exp_hold:
                if exp_hold[-1] in ['+','-']:
                    exp_hold.append(i)
                elif exp_hold[-1] in ['*','/']:
                    if i in ['*','/']:
                        exp_hold.append(i)
                    else:
                        while exp_hold:
                            postfix.append(exp_hold.pop())
                        exp_hold.append(i)
    while exp_hold:
        postfix.append(exp_hold.pop())
    call_print(postfix)
    postfix_to_solution(postfix)
def userinput_to_infix_generator(user_input):
    infix = []
    temp = ""
    symbols = ['+','-','/','*']
    for i in user_input:
        if i not in symbols:
            temp = temp + i
        else:
            infix.append(temp)
            infix.append(i)
            temp = ""
    if temp:
        infix.append(temp)
    call_print(infix)
    infix_to_postfix(infix)
def main():
    valid_inputs = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/']
    try:
        user_input = input('Enter : ')
        user_input = user_input.replace(" ","")
        if any(i not in valid_inputs for i in user_input):
            raise ValueError("Invalid input")
    except Exception as e:
        print(e)
        return
    userinput_to_infix_generator(user_input)
main()
