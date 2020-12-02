import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from simanneal import Annealer
from breakout import *
import glob
from os.path import *
import sys
from os.path import basename, normpath
import glob

def generate_dic(rooms):
    dic = {}
    for i in range(0, len(rooms)):
        for student in rooms[i].students:
            dic[student] = i
    return dic

def generate_dic_from_lists(rooms):
    dic = {}
    for i in range(len(rooms)):
        for student in rooms[i]:
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
    """
    rooms = greedy_happiness(G, s)
    if rooms is None:
        return {}, -1
    rooms = [r for r in rooms if len(r) != 0]
    return generate_dic_from_lists(rooms), len(rooms)
    """


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

def main():
    """
    inputs = glob.glob('inputs/testing/*')
    couldnt = []
    done = 0
    for input_path in inputs:
        print("doing #" + str(done) + ": " + input_path)
        done += 1
        output_path = 'outputs/testing/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D, k = solve(G, s)
        if k != -1:
            assert is_valid_solution(D, G, s, k)
            cost_t = calculate_happiness(D, G)
            write_output_file(D, output_path)
            print("done, used " + str(k) + " rooms")
        else:
            couldnt += [input_path]
    print(couldnt)
    """
    num = sys.argv[1]
    print("Doing #" + str(num))
    input_path = "inputs/testing-small/small-" + str(num) + ".in"
    output_path = "outputs/testing-small/small-" + str(num) + ".out"
    G, s = read_input_file(input_path)
    D, k = solve(G, s)
    if k != -1:
        assert is_valid_solution(D, G, s, k)
        write_output_file(D, output_path)
        print("done, used " + str(k) + " rooms")

# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    main()

