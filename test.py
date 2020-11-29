from breakout import *
from parse import *
from utils import *

G, stress_budget = read_input_file("in/50_1.in")
print(greedy_happiness(G, stress_budget))
"""
problem = BreakoutProblem(G, stress_budget)
problem.updates = 1000
zoom, happiness = problem.anneal()
print("\n")
print(zoom.rooms, happiness)
"""
"""
def fun(lst):
    graph, stress_budget = read_input_file("in/50.in")
    dic = {}
    for i in range(len(lst)):
        dic[i] = lst[i]
    if is_valid_solution(convert_dictionary(dic), graph, stress_budget, len(lst)):
        return -1 * calculate_happiness(convert_dictionary(dic), graph)
    else: # does not meet stress requirement
        return 1
        # return max(0, (-1 * self.state.stress_happiness_score()) / 100)

print(fun([[2, 7, 8, 13, 15, 16, 18, 19, 20, 21, 23, 24, 25, 26, 32, 34, 35, 36, 38, 39, 41, 43, 44, 45, 46, 47, 49], [0, 1, 3, 4, 5, 6, 9, 10, 11, 12, 14, 17, 22, 27, 28, 29, 30, 31, 33, 37, 40, 42, 48]]))
"""