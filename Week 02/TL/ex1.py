num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] 
k=3

def max_kernel(num_list, size):
    result = []
    for i in range(len(num_list) - size + 1):
        result.append(max(num_list[i:i + size]))
    return result

print(max_kernel(num_list, k))