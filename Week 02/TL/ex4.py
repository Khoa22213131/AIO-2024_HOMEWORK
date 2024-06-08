#factors for each transformation
ins_cost_factor = 1
del_cost_factor = 1
sub_cost_factor = 1

# functions to calculate the cost of transformation 
def ins_cost(target):
    return ins_cost_factor

def del_cost(source):
    return del_cost_factor

def sub_cost(source, target):
    if source == target:
        return 0
    return sub_cost_factor

# main function to calculate the levenshtein distance
def levenshtein_distance(source, target):
    # initialize matrix
    m = len(source) + 1
    n = len(target) + 1
    D = [[0 for j in range(n)] for i in range(m)]
    
    # fill in value of first row and column
    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = j
        
    # fill in the rest of the matrix
    for i in range(1, m):
        for j in range(1, n):
            D[i][j] = min(D[i-1][j] + del_cost(source[i-1]),
                          D[i][j-1] + ins_cost(target[j-1]),
                          D[i-1][j-1] + sub_cost(source[i-1], target[j-1]))
    
    # print the matrix
    for row in D:
        print(row)
    
    # return the value in the bottom right cornered cell
    return D[m-1][n-1]

source = 'kitten'
target = 'sitting'

print(levenshtein_distance(source, target)) 