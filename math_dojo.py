class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        sum_nums = 0
        for i in nums:
            sum_nums += i
        sum = num + sum_nums
        self.result += sum
        return self
    def subtract(self, num, *nums):
        sum_nums = 0
        for i in nums:
            sum_nums += i
        sum = num + sum_nums
        self.result -= sum
        return self

md = MathDojo()

x = md.add(50, 100, 100, 100, 10, 50, 40, 50).add(50, 50, 100).subtract(100, 50, 50 ,100, 200).result 

print(x)