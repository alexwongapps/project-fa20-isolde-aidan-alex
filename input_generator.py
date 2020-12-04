from random import *
from utils import *
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


# print(generate_output([[3, 11, 15, 7], [8, 5, 17], [4, 14, 0], [18, 2, 10, 12], [9, 1], [16, 13, 19, 6]]))

def generate_input(lst):
    lst1 = lst[0]
    lst2 = lst[1]
    print(lst)
    size = len(lst1) + len(lst2)
    ret = ""
    ret += str(size) + "\n"
    ret += str(size) + "\n"

    for i in range(size):
        if i in lst1:
            index = 0
        else:
            index = 1
        for j in range(size):
            if i < j:
                if j in lst[index]:
                    rand_stress = uniform(0, 1)
                    rand_happiness = uniform(size, size+10)
                else:
                    rand_stress = uniform(size, size+10)
                    rand_happiness = uniform(0, 1)
                ret += str(i) + " " + str(j) + " " + str(round(rand_happiness, 3)) + " " + str(round(rand_stress, 3))
                ret += "\n"
    return ret

def generate_lst(s):
    lst = [[], []]
    for i in range(s):
        check = randint(0,1)
        if check == 0:
            lst[0] += [i]
        else:
            lst[1] += [i]
    return lst
            

#print(generate_input(generate_lst(10)))
print(generate_output([[13, 8, 2, 6], [9, 5, 1, 0], [4, 11, 18, 14], [12, 17, 16, 15], [7, 10, 3, 19]]))


