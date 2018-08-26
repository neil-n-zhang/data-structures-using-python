def reverselist(list,reversal):
    if len(list)>=1:
        reversal.append(list.pop())
        reverselist(list,reversal)
        return




a=[1,2,666,3,4,5,6]
b=[]
reverselist(a,b)