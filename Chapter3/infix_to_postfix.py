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

def infixtopostfix(string):
    opstack=Stack()
    output=[]
    string_list=list(string)
    operator=['*','/','+','-']
    prio={}
    prio['*']=1
    prio['/'] = 1
    prio['+'] = 2
    prio['-'] = 2
    prio['('] = 3

    for char in string_list:
        if char=='(':
            opstack.push('(')
        elif char==')':
            while not opstack.isEmpty():
                op=opstack.pop()
                if op=='(':
                    continue
                else:
                    output.append(op)
        elif not char in operator:
            output.append(char)
        else:
            while not opstack.isEmpty() and prio[opstack.peek()]<=prio[char]:
                output.append(opstack.pop())
            opstack.push(char)

    while not opstack.isEmpty():
        output.append(opstack.pop())

    return output

infixtopostfix('(A+B)*(C+D)')
infixtopostfix('(A+B)*C')
infixtopostfix('A+B*C')