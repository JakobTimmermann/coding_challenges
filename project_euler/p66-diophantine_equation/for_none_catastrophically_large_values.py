'''
This works fine for D values that are not too large.
Doesn't work for D values of e.g. 61
'''

def solve_quadratic_diophantine_equation(D):
    y = determine_y_start_value(D)
    while True:
        x = max(1, determine_x_start_value(y, D))
        while D * x ** 2 < y ** 2:
            result = y ** 2 - D * x ** 2
            if result == 1:
                return y, x
            x += 1
        y += 1


def determine_y_start_value(D):
    return int(np.floor(np.sqrt(D + 1)))


def determine_x_start_value(y, D):
    min_x = np.sqrt((y ** 2 - 1) / D)
    return int(min_x)



