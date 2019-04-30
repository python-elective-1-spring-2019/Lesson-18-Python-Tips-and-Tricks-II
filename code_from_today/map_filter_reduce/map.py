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

x = tuple(map(double_money, money))
print('Map version:', x)


# Version map with lambda

x = list(map(lambda x: x*2 , money))
print('Map Lambda version:', x)










"""
# Lav en liste af a-z små bogstaver
map() lav en ny liste med store bogstaver.
brug lambda.
"""

import string

alph = string.ascii_lowercase
print(list(map(lambda x: x.upper(), alph)))



''











"""



x = tuple(map(lambda x : x*2 , money))
print('Lambda/map version:', x)

"""