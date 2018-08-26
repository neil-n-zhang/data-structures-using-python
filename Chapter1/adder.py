class LogicGate():
    def __init__(self,n):
        self.label=n
        self.output=None

    def getlabel(self):
        return self.label

    def getoutput(self):
        self.output=self.performgatelogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pinA=None
        self.pinB=None

    def getpinA(self):
        if self.pinA==None:
            return int(input("Enter pin A input for gate "+ self.getlabel()+"-->"))
        elif self.pinA==0 or self.pinA==1:
            return self.pinA
        else:
            return self.pinA.getFrom().getoutput()
    def getpinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for gate "+ self.getlabel()+"-->"))
        elif self.pinB==0 or self.pinB==1:
            return self.pinB
        else:
            return self.pinB.getFrom().getoutput()
    def setNextPin(self,source):
        if self.pinA==None:
            self.pinA=source
        else:
            if self.pinB==None:
                self.pinB=source
            else:
                raise RuntimeError("No empty pins")

class AndGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performgatelogic(self):
        a=self.getpinA()
        b=self.getpinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performgatelogic(self):
        a=self.getpinA()
        b=self.getpinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class XorGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performgatelogic(self):
        a=self.getpinA()
        b=self.getpinB()
        if a==b:
            return 0
        else:
            return 1

class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate=fgate
        self.togate=tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate

class HalfAdder():
    def __init__(self,n):
        self.label = n
        self.output = None
        self.pinA=None
        self.pinB=None
        self.output_S=None
        self.output_C=None

    def getlabel(self):
        return self.label

    def getpinA(self):
        if self.pinA == None:
            return int(input("Enter pin A input for HalfAdder " + self.getlabel() + "-->"))
        elif self.pinA==0 or self.pinA==1:
            return self.pinA
        else:
            return self.pinA.getFrom().getoutput()

    def getpinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for HalfAdder " + self.getlabel() + "-->"))
        elif self.pinB==0 or self.pinB==1:
            return self.pinB
        else:
            return self.pinB.getFrom().getoutput()

    def getoutput(self):
        self.pinA=self.getpinA()
        self.pinB=self.getpinB()
        output_gate_S=XorGate('output_gate_S')
        output_gate_S.pinA=self.pinA
        output_gate_S.pinB = self.pinB
        self.output_S=output_gate_S.getoutput()

        output_gate_C = AndGate('output_gate_C')
        output_gate_C.pinA = self.pinA
        output_gate_C.pinB = self.pinB
        self.output_C = output_gate_C.getoutput()
        return self.output_S,self.output_C

class FullAdder():
    def __init__(self,n):
        self.label = n
        self.output = None
        self.pinA=None
        self.pinB=None
        self.pinC = None
        self.output_S=None
        self.output_C=None

    def getlabel(self):
        return self.label

    def getpinA(self):
        if self.pinA == None:
            return int(input("Enter pin A input for HalfAdder " + self.getlabel() + "-->"))
        elif self.pinA==0 or self.pinA==1:
            return self.pinA
        else:
            return self.pinA.getFrom().getoutput()

    def getpinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for HalfAdder " + self.getlabel() + "-->"))
        elif self.pinB==0 or self.pinB==1:
            return self.pinB
        else:
            return self.pinB.getFrom().getoutput()

    def getpinC(self):
        if self.pinC == None:
            return int(input("Enter pin B input for HalfAdder " + self.getlabel() + "-->"))
        elif self.pinC==0 or self.pinC==1:
            return self.pinC
        else:
            return self.pinC.getFrom().getoutput()

    def getoutput(self):
        self.pinA=self.getpinA()
        self.pinB=self.getpinB()
        self.pinC = self.getpinC()
        xor1=XorGate('xor1')
        xor1.pinA=self.pinA
        xor1.pinB = self.pinB

        xor2 = XorGate('xor2')
        xor2.pinB = self.pinC
        c1 = Connector(xor1, xor2)

        and1=AndGate('and1')
        and1.pinB=self.pinC
        c2=Connector(xor1,and1)

        and2 = AndGate('and2')
        and2.pinA = self.pinA
        and2.pinB = self.pinB

        or1=OrGate('or1')
        c3=Connector(and1,or1)
        c4 = Connector(and2, or1)

        self.output_S=xor2.getoutput()
        self.output_C=or1.getoutput()

        return self.output_S,self.output_C


# halfadder=HalfAdder('halfadder')
# s,c=halfadder.getoutput()
#
#
# fulladder=FullAdder('fulladder')
# s,c=fulladder.getoutput()