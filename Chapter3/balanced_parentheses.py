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


def parcheck(string):
    par=Stack()
    string_list=list(string)

    for char in string_list:
        if char=='(':
            par.push('(')
        elif char==')':
            if par.isEmpty():
                return print('Not balanced.')
            else:
                par.pop()

    if par.isEmpty():
        return print('Balanced')
    else:
        return print('Not balanced.')