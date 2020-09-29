def load_list_1():
    vals = []
    with open('problem_1_vals.txt') as file:
        for val in file:
            vals.append(int(val))
    return vals

def load_list_2():
    vals = []
    with open('problem_2_vals.txt') as file:
        for line in file:
            val1, val2 = line.split()
            vals.append([int(val1), int(val2)])
    return vals
