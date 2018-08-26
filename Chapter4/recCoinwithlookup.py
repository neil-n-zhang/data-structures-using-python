def recCoin(coinlist,change,knownresults):
    if change in coinlist:
        knownresults[change]=1
        return 1
    elif knownresults[change]>0:
        print(knownresults)
        print(change)
        return knownresults[change]
    else:
        coinnum=[]
        for i in [c for c in coinlist if change>c]:
            coinnum.append(1+recCoin(coinlist,change-i,knownresults))
        knownresults[change]=min(coinnum)
        return knownresults[change]


recCoin([1,5,10,25],8,[0]*9)