import sys
sys.path.append('D:\Data_structure\Chapter 1')
from adder import HalfAdder
from adder import FullAdder


class EigBitAdder():
    def __init__(self,num1,num2):
        self.num1=format(num1,'08b')
        self.num2=format(num2,'08b')
        self.result=[]

    def getresult(self):
        self.result = []
        halfadder = HalfAdder('halfadder')
        halfadder.pinA=int(self.num1[-1])
        halfadder.pinB=int(self.num2[-1])
        sumresult,carry=halfadder.getoutput()
        self.result.append(sumresult)

        for i in list(range(7))[6::-1]:
            fulladder = FullAdder('fulladder')
            fulladder.pinA=int(self.num1[i])
            fulladder.pinB = int(self.num2[i])
            fulladder.pinC = carry
            sumresult, carry=fulladder.getoutput()
            self.result.append(sumresult)
        if carry==1:
            self.result.append(carry)
        self.result.reverse()
        return int((''.join(map(str,self.result))),2)



a=EigBitAdder(71,50)
b=a.getresult()
