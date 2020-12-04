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

def solve(G, s, load=None):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    
    problem = BreakoutProblem(G, s, load=load)
    zoom, happiness = problem.anneal()
    mapping = generate_dic(zoom.rooms)
    return mapping, len(zoom.rooms)
    
    """
    # rooms = greedy_happiness(G, s)
    rooms = true_random(G, s, start_greedy_at=40)
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
    already_done = [1, 2, 6, 7, 9, 12, 14, 16, 18, 26, 33, 38, 39, 43, 46, 51, 53, 54, 56, 59, 60, 63, 64, 70, 73, 74, 77, 81, 84, 88, 89, 100, 103, 105, 111, 112, 114, 122, 123, 128, 132, 140, 143, 145, 147, 151, 157, 160, 161, 166, 169, 175, 178, 184, 187, 201, 202, 203, 206, 207, 208, 209, 213, 217, 218, 220, 222, 226, 227, 230, 233, 235]
    """
    inputs = glob.glob('compinputsmed/*')
    couldnt = []
    done = 0
    for i in range(len(inputs)):
        input_path = inputs[i]
        num = int(basename(normpath(input_path))[:-3].split("-")[1])
        
        done += 1
        if num not in already_done:
            print("doing #" + str(done) + ": " + input_path)
            output_path = 'comp2med/' + basename(normpath(input_path))[:-3] + '.out'
            G, s = read_input_file(input_path)
            D, k = solve(G, s, load='comp1med/' + basename(normpath(input_path))[:-3] + '.out')
            if k != -1:
                assert is_valid_solution(D, G, s, k)
                cost_t = calculate_happiness(D, G)
                write_output_file(D, output_path)
                # print("done, used " + str(k) + " rooms")
            else:
                couldnt += [input_path]
        else:
            print("medium-" + str(num) + " is already done")
    """
    
    num = int(sys.argv[1])
    print("Doing #" + str(num))
    if num not in already_done:
        input_path = "compinputsmed/medium-" + str(num) + ".in"
        current_sol_path = "comp1med/medium-" + str(num) + ".out"
        output_path = "comp2med/medium-" + str(num) + ".out"
        G, s = read_input_file(input_path)
        D, k = solve(G, s, load=current_sol_path)
        if k != -1:
            assert is_valid_solution(D, G, s, k)
            write_output_file(D, output_path)
            print("done, used " + str(k) + " rooms, happiness " + str(calculate_happiness(D, G)))
    else:
        print("Already done")
    

# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    main()

