class HashTable:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,rehash_time,size):
        return (oldhash+rehash_time**2)%size

    def put(self,key,data):
        if not None in self.slots:
            print('HashTable is full.')
            return
        hashvalue=self.hashfunction(key,self.size)
        if self.slots[hashvalue]==None or self.slots[hashvalue]==key:
            self.slots[hashvalue] = key
            self.data[hashvalue]=data
        else:
            rehash_time=1
            nexthash=self.rehash(hashvalue,rehash_time,self.size)
            while self.slots[nexthash]!=None and self.slots[nexthash]!=key:
                rehash_time+=1
                nexthash = self.rehash(hashvalue, rehash_time,self.size)
            self.slots[nexthash]=key
            self.data[nexthash]= data
    def get(self,key):
        hashvalue = self.hashfunction(key, self.size)
        count=0
        found=False
        while count<=self.size and not found:
            if self.slots[hashvalue]==key:
                found=True
            else:
                rehash_time=1
                hashvalue=self.rehash(hashvalue,rehash_time,self.size)
                count+=1
                rehash_time+=1
        if found:
            return self.data[hashvalue]
        else:
            return print('Not found.')

    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key,data)
    def __len__(self):
        return sum([1 for x in self.data if x!=None])
    def __contains__(self, item):
        return item in self.data


H=HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])