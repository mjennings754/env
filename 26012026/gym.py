"""
Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, 
which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability
"""

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

import math
from collections import Counter
class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return self.data[0]
    
    def max(self):
        return self.data[-1]
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return sum(self.data) / self.count()
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]
    
data = Statistics(ages)

print('Count: ', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())