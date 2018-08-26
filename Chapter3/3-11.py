import re
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


def htmlparcheck(address):
    par=Stack()
    f=open(address,'r')
    for line in f:
        openings=re.findall('<[^/]',line)
        closings=re.findall('</',line)
        for opening in openings:
            par.push(opening)
        for closing in closings:
            if par.isEmpty():
                return print('Not balanced.')
            else:
                par.pop()

    if par.isEmpty():
        return print('Balanced')
    else:
        return print('Not balanced.')


a=htmlparcheck('D:\Data_structure\Chapter3\html.txt')