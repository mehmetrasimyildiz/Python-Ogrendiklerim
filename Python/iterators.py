class MyNumber:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
list = MyNumber(10,20)
myiter = iter(list)

while True:
    try:
        elemnt = next(myiter)
        print(elemnt)
    except StopIteration:
        break

