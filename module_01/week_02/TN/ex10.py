def my_function(integers, number=1):
    return any([integer == number for integer in integers])


my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
