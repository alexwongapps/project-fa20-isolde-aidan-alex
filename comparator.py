import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_happiness
from simanneal import Annealer
from breakout import *
import glob
from os.path import *
import sys
from os.path import basename, normpath
from solver import *

# Given two sets of outputs, writes the output of the best happiness to the first file for each input
# Requires a folder "inputs" with the input files, and two folders "comp1" and "comp2" with the two output sets to compare
# The folders should have no subfolders
# The folders should have the same files (e.g. for file small-1, there should be inputs/small-1.in, comp1/small-1.out, comp2/small-1.out)
# Since this will overwrite the outputs in "comp1", you should make sure those are backed up (push them to Git or something)
if __name__ == '__main__':
    inputs = glob.glob('inputs/*')
    done = 0
    for input_path in inputs:
        print("doing #" + str(done) + ": " + input_path)
        done += 1
        first_path = 'comp1/' + basename(normpath(input_path))[:-3] + '.out'
        second_path = 'comp2/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D1, k1 = read_output_file(first_path, G, s)
        D2, k2 = read_output_file(second_path, G, s)
        h1 = calculate_happiness(D1, G)
        h2 = calculate_happiness(D2, G)
        if h1 < h2:
            write_output_file(D2, output_path)