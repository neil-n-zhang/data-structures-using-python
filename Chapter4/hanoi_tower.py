def hanoi(disknum,frompole,withpole,topole):
    if disknum>1:
        hanoi(disknum-1,frompole,topole,withpole)
        hanoi(1,frompole,withpole,topole)
        hanoi(disknum-1,withpole,frompole,topole)
    elif disknum==1:
        print('Move one disk from %s to %s'%(frompole,topole))


hanoi(3,'a','c','b')