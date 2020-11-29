import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from simanneal import Annealer
from breakout import *
import glob
from os.path import *
import sys

def generate_dic(rooms):
    dic = {}
    for i in range(0, len(rooms)):
        for student in rooms[i].students:
            dic[student] = i
    return dic

def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    problem = BreakoutProblem(G, s)
    zoom, happiness = problem.anneal()
    mapping = generate_dic(zoom.rooms)
    return mapping, len(zoom.rooms)



# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in
"""
if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k = solve(G, s)
    assert is_valid_solution(D, G, s, k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    write_output_file(D, 'out/test.out')
"""

# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('inputs/small/*')
    for input_path in inputs:
        output_path = 'outputs/small/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D, k = solve(G, s)
        assert is_valid_solution(D, G, s, k)
        cost_t = calculate_happiness(D, G)
        write_output_file(D, output_path)
