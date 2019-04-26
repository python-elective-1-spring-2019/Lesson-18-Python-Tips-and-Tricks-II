# Take a list and run som task on each item in the list

# Version 1
money = [10, 20, 30]
print('original list', money)

def double_money(m):
    return m * 2

double_list = []

for item in money:
    x = double_money(item)
    double_list.append(x)


print (double_list)

# Version map

x = tuple(map(double_money, money))
print('Map version:', x)

# Version map with lambda

x = tuple(map(lambda x : x*2 , money))
print('Lambda/map version:', x)

# Iterating over a dictionary using map and lambda
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]
map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]

# Multiple iterables to the map function
list_x = [1, 2, 3]
list_y = [10, 20, 30]
  
map(lambda x, y: x + y, list_x, list_y) # Output: [11, 22, 33]