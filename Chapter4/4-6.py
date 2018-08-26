#https://darealnormanlee.wordpress.com/2014/06/25/solve-the-tower-of-hanoi-problem-using-stacks-in-python/
def hanoi(disknum,frompole,withpole,topole):
    if disknum>1:
        hanoi(disknum-1,frompole,topole,withpole)
        hanoi(1,frompole,withpole,topole)
        hanoi(disknum-1,withpole,frompole,topole)

    elif disknum==1:
        print('Move one disk from %s to %s'%(frompole,topole))
        eval(topole+'.append('+frompole+'.pop())')
        print(a,b,c)



a=[4,3,2,1]
b=[]
c=[]
hanoi(len(a),'a','b','c')