def my_function(list_nums=[0, 1, 2]):
    var = 0
    len = 0

    for i in list_nums:
        var += i
        len += 1

    return var / len


print(my_function())
