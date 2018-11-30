class HashTable:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def hashfunction(self,key,size):
        return key%size

    def put(self,key,data):
        if not None in self.slots:
            print('HashTable is full.')
            return
        hashvalue=self.hashfunction(key,self.size)
        if self.slots[hashvalue]==None or self.slots[hashvalue]==key:
            self.slots[hashvalue] = key
            self.data[hashvalue]=data
        else:
            if type(self.slots[hashvalue])==int:
                self.slots[hashvalue]=[self.slots[hashvalue]]
                self.slots[hashvalue].append(key)
                self.data[hashvalue] = [self.data[hashvalue]]
                self.data[hashvalue].append(data)
            else:
                if key in self.slots[hashvalue]:
                    self.data[hashvalue][self.slots[hashvalue].index(key)]=data
                else:
                    self.slots[hashvalue].append(key)
                    self.data[hashvalue].append(data)

    def get(self,key):
        hashvalue = self.hashfunction(key, self.size)
        if type(self.slots[hashvalue])==int:
            if self.slots[hashvalue]==key:
                return self.data[hashvalue]
        elif type(self.slots[hashvalue])==list:
            if key in self.slots[hashvalue]:
                return  self.data[hashvalue][self.slots[hashvalue].index(key)]
        else:
            return print('Not found.')

    def delete(self,key):
        hashvalue = self.hashfunction(key, self.size)
        if type(self.slots[hashvalue])==int:
            if self.slots[hashvalue]==key:
                self.slots[hashvalue]=None
                self.data[hashvalue]=None
                return
        elif type(self.slots[hashvalue])==list:
            if key in self.slots[hashvalue]:
                self.data[hashvalue].remove(self.data[hashvalue][self.slots[hashvalue].index(key)])
                self.slots[hashvalue].remove(key)
                return
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
H.delete(44)

