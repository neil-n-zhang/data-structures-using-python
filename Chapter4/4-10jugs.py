class Jar():
    def __init__(self,max_vol,name):
        self.max_vol=max_vol
        self.vol=0
        self.name=name
    def full(self):
        self.vol=self.max_vol
        print('Full',self.name)
    def empty(self):
        self.vol=0
        print('Empty', self.name)

def rm_water(jar1,jar2,water):
    jar1.vol=jar1.vol-water
    jar2.vol=jar2.vol+water
    print('transfer %i water from'%water,jar1.name,'to',jar2.name)

def addjug(small_jug,big_jug,target_vol):
    while big_jug.vol!=target_vol:
        big_jug.full()
        while big_jug.vol!=0:
            if big_jug.vol>=(small_jug.max_vol-small_jug.vol):
                rm_water(big_jug,small_jug,(small_jug.max_vol-small_jug.vol))
                small_jug.empty()
            else:
                rm_water(big_jug,small_jug,big_jug.vol)

            if big_jug.vol==target_vol:
                print('Finish')
                return
            elif big_jug.vol==0 and small_jug.vol==0:
                print('Can\'t make it.')
                return


small_jug=Jar(6,'small')
big_jug=Jar(10,'big')
addjug(small_jug,big_jug,5)