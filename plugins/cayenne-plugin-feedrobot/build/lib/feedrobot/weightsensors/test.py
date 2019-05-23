class test:
    def __init__(self):
        self.max = 100
        self.min = 10
    def add(self, x, y):
        return x + y
    def mul(self, x, y): return x * y

if __name__ == '__main__': 
    t=test()
    print(t.add(10,20))       