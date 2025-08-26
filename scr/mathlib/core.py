"""
This file will choose or will be gate for math functions access.
"""

from .statistics import Statistics

print(Statistics.mean([10, 20, 30]))        
print(Statistics.mean((5, 15, 25)))         
print(Statistics.mean({2, 4, 6, 8}))        
print(Statistics.mean(range(1, 6)))      