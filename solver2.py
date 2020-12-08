import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from simanneal import Annealer
from breakout2 import *
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

def solve(G, s, load=None, moves=1):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    """
    current_bunch = []
    for i in range(10):
        problem = BreakoutProblem(G, s, load=load)
        problem.steps = 1000
        problem.updates = 10
        zoom, happiness = problem.anneal()
        current_bunch.append((zoom.rooms.copy(), happiness))
    current_bunch.sort(key=lambda c: c[1])
    current_bunch = current_bunch[:3]
    for i in range(5):
        print([c[1] for c in current_bunch])
        for j in range(10):
            problem = BreakoutProblem(G, s, rooms=choice([c[0] for c in current_bunch]))
            problem.steps = 1000
            problem.updates = 10
            zoom, happiness = problem.anneal()
            current_bunch.append((zoom.rooms.copy(), happiness))
        current_bunch.sort(key=lambda c: c[1])
        current_bunch = current_bunch[:3]
    mapping = generate_dic(zoom.rooms)
    return mapping, len(zoom.rooms)
    """
    """
    problem = BreakoutProblem(G, s, load=load)
    problem.steps = 100000
    problem.updates = 100
    problem.Tmax = 100000.0
    problem.Tmin = 10.0
    zoom, happiness = problem.anneal()
    mapping = generate_dic(zoom.rooms)
    return mapping, len(zoom.rooms)
    """
    """
    # rooms = greedy_happiness(G, s)
    rooms = true_random(G, s)
    if rooms is None:
        return {}, -1
    rooms = [r for r in rooms if len(r) != 0]
    return generate_dic_from_lists(rooms), len(rooms)
    
    """
    if moves == 0:
        r = check_switches(G, s, load=load)
        if r is not None:
            last = r.copy()
        else:
            return {}, -1
        while r is not None:
            r = check_switches(G, s, rs=r)
            if r is not None:
                last = r.copy()
        return generate_dic_from_lists(last), len(last)
    else:
        r = check_moves(G, s, load=load)
        if r is not None:
            last = r.copy()
        else:
            return {}, -1
        while r is not None:
            r = check_moves(G, s, rs=r)
            if r is not None:
                last = r.copy()
        return generate_dic_from_lists(last), len(last)
    
    
    

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
    already_done = [1, 2, 4, 6, 7, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 26, 29, 30, 33, 34, 35, 38, 39, 40, 41, 43, 46, 47, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 63, 64, 70, 73, 74, 76, 77, 79, 81, 83, 84, 85, 88, 89, 90, 96, 100, 101, 103, 105, 109, 110, 111, 112, 113, 114, 115, 117, 119, 121, 122, 123, 125, 128, 129, 131, 132, 134, 136, 137, 140, 141, 143, 145, 147, 151, 152, 156, 157, 158, 159, 160, 161, 162, 166, 167, 169, 172, 174, 175, 177, 178, 181, 184, 187, 196, 199, 201, 202, 203, 206, 207, 208, 209, 213, 216, 217, 218, 220, 222, 223, 226, 227, 230, 233, 235, 237, 238, 240, 241]
    # already_done = [7, 18, 33, 43, 51, 54, 56, 65, 69, 73, 77, 81, 91, 112, 114, 121, 123, 127, 131, 134, 151, 169, 171, 174, 178, 184, 187, 201, 202, 207, 213, 215, 222]
    """
    inputs = glob.glob('compinputslarge/*')
    couldnt = []
    done = 0
    for i in range(len(inputs)):
        input_path = inputs[i]
        
        done += 1
        print("doing #" + str(done) + ": " + input_path)
        output_path = 'comp2large/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D, k = solve(G, s)
        if k != -1:
            assert is_valid_solution(D, G, s, k)
            write_output_file(D, output_path)
            # print("done, used " + str(k) + " rooms")
        else:
            couldnt += [input_path]
    
    """
    num = int(sys.argv[1])
    moves = int(sys.argv[2])
    print("Doing #" + str(num))
    if num not in already_done:
        input_path = "compinputsmed/medium-" + str(num) + ".in"
        current_sol_path = "comp1med/medium-" + str(num) + ".out"
        output_path = "comp2med/medium-" + str(num) + ".out"
        G, s = read_input_file(input_path)
        D, k = solve(G, s, load=current_sol_path, moves=moves)
        if k != -1:
            assert is_valid_solution(D, G, s, k)
            write_output_file(D, output_path)
            #print("done, used " + str(k) + " rooms, happiness " + str(calculate_happiness(D, G)))
    #else:
        #print("Already done")
    

# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    main()

