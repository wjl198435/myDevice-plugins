from multiprocessing.managers import BaseManager
import random
class MathsClass:
    def __init__(self):
        self.max = 100
        self.min = 10
    def add(self, x, y):
        return x + y
    def mul(self, x, y): return x * y
    
    def get_value(self):
        value = random.uniform(self.min, self.max) 
        return (value,'weight', 'kg')

class MyManager(BaseManager): 
    pass
MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    with MyManager() as manager:
         maths = manager.Maths()
         print(maths.add(4, 3))
         print(maths.mul(7, 8))        