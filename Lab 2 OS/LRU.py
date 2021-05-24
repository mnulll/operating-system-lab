class LRU:
    def __init__(self):
        self.a = []

    def capacity(self, size):
        self.a = [None]*size

    def put(self, arr):
        for i in arr:
            if i in self.a:
                x = self.a.index(i)
                self.a.pop(x)
                self.a.append(i)
                print(self.a)
            else:
                self.a.pop(0)
                self.a.append(i)
                print(self.a)


a = LRU()
a.capacity(5)
b = [1, 2, 3, 4, 5, 8, 5, 7, 6, 5, 7]
a.put(b)
