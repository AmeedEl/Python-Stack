class MathDojo: 
    def __init__(self):
        self.result = 0 

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n 
        return self 
        
md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)

y = md.add(10).subtract(4, 1).add(3, 6).subtract(2).result
print(y)