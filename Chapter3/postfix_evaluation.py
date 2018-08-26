class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def postfix_eva(string):
    tokenlist=list(string)
    operand=Stack()
    for token in tokenlist:
        if token in '0123456789':
            operand.push(int(token))
        else:
            num2=operand.pop()
            num1=operand.pop()
            result=cal(num1,num2,token)
            operand.push(result)
    return operand.pop()

def cal(n1,n2,operator):
    if operator=='*':
        return n1*n2
    elif operator=='/':
        return n1/n2
    elif operator=='+':
        return n1+n2
    else:
        return n1-n2

#test
postfix_eva('456*+1+')
postfix_eva('45+61+*')
