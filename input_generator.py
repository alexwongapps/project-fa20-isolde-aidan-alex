from random import *
def create_input_file(n, max_stress):
    ret = ""
    ret += str(n) + "\n"
    ret += str(round(max_stress, 3)) + "\n"
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                rand_happiness = round(random() * 99.999, 3)
                rand_stress = round(random() * 1.5, 3)
                ret += str(i) + " " + str(j) + " " + str(rand_happiness) + " " + str(rand_stress)
                ret += "\n"
    return ret


def generate_output(lst):
    ret = ""
    for i in range(0, len(lst)):
        for element in lst[i]:
            ret += str(element) + " " + str(i)
            ret += "\n"
    return ret


print(generate_output([[7, 13, 1, 12], [10, 14, 16, 5], [11, 15, 3], [0, 17, 19], [2, 18, 8], [9, 4, 6]]))