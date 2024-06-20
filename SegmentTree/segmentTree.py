def __init__(self,data):
    self.n=len(data) #Inititalising of data
    self.tree=[0]*(2*self.n) # Creating array of size (2n)
    self.build(data)


def build(self,data):
    
    for i in range(self.n):
        self.tree[self.n + i] = data[i]
    
    for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    