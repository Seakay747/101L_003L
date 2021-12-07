import math
def total(values):
    sum = 0
    for ele in values:
        sum += ele
    return sum
def average(values):
    if len(values) == 0:
        return math.nan
    return (total(values) / len(values))
def median(values):
    if len(values) == 0:
        raise ValueError
    if len(values) % 2 == 1:
        return sorted(values)[len(values)//2]
    else:
        return average([sorted(values)[len(values)//2], sorted(values)[(len(values)//2) - 1]])
