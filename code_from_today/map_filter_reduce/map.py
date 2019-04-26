# Take a list and run som task on each item in the list

# Version 1
money = [10, 20, 30]
print('original list', money)

def double_money(m):
    return m * 2
"""
double_list = []

for item in money:
    x = double_money(item)
    double_list.append(x)


print (double_list)

"""
# Version map

x = list(map(double_money, money))
print('Map version:', x)















