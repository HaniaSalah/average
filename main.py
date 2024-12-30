def average(ls):
    summation = sum(ls)
    avg = summation / len(ls)
    return avg

ls=[2,4,6,8,10]

avg = average(ls)

print("list =",ls)
print("Average=",average(ls))