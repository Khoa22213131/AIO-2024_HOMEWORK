def calc_se(y, y_hat):
    return (y - y_hat) ** 2

print(calc_se(2, 1))