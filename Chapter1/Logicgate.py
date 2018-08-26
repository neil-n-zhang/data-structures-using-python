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
        else:
            return self.pinA.getFrom().getoutput()
    def getpinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for gate "+ self.getlabel()+"-->"))
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

class UnaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pin = None

    def getpin(self):
        if self.pin==None:
            return int(input("Enter pin input for gate " + self.getlabel() + "-->"))
        else:
            return self.pin.getFrom().getoutput()
    def setNextPin(self,source):
        if self.pin==None:
            self.pin=source
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

class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performgatelogic(self):
        a=self.getpin()
        if a==1:
            return 0
        elif a==0:
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


#Test
g1=AndGate("G1")
g2=AndGate("G2")
g3=OrGate("G3")
g4=NotGate("G1")
g4=NotGate("G4")
c1=Connector(g1,g3)
c2=Connector(g2,g3)
c3=Connector(g3,g4)
