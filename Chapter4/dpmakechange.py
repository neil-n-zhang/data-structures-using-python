def dpmakechange(coinlist,changes,mincoins,coinused):
    for change in range(1,changes+1):
        coinnum = []
        coinvalue = []
        for coin in coinlist:
            if coin<=change:
                coinnum.append(mincoins[change-coin]+1)
                coinvalue.append(coin)
        mincoins[change]=min(coinnum)
        coinused[change]=coinvalue[coinnum.index(mincoins[change])]

def printcoins(changes,coinused):
    while changes>0:
        print(coinused[changes])
        changes=changes-coinused[changes]



c1=[1,5,10,21,25]
a=[0]*64
b=[0]*64
dpmakechange(c1,63,a,b)
printcoins(63,b)
dpmakechange(c1,52,a,b)
printcoins(52,b)