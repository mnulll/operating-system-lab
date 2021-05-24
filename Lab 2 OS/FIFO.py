class FIFO:
    def __init__(self):
        self.a = []
        self.counter = 0
        self.fail = 0

    def capacity(self, size):
        self.a = [None]*size

    def enqueue(self, word):
        if word not in self.a:
            self.a.append(word)
            self.a.pop(0)
            print(self.a)
            self.fail += 1
            self.counter += 1
        else:
            self.counter += 1

    def success_rate(self):
        success = 1-(self.fail/self.counter)
        print("Success rate is", success)


q = FIFO()
q.capacity(4)
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
q.enqueue("a")
q.enqueue("e")
q.enqueue("a")
q.success_rate()
