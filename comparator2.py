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
    inputs = glob.glob('compinputsmed/*')
    done = 0
    changed = 0
    kept = 0
    improvement = 0
    for input_path in inputs:
        first_path = 'comp1med/' + basename(normpath(input_path))[:-3] + '.out'
        second_path = 'comp2med/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        try:
            D1 = read_output_file(first_path, G, s)
            h1 = calculate_happiness(D1, G)
        except:
            h1 = 0
        try: 
            D2 = read_output_file(second_path, G, s)
            h2 = calculate_happiness(D2, G)
        except:
            h2 = 0
        if h1 + h2 > 0:
            done += 1
            # print("doing #" + str(done) + ": " + input_path)
            if h1 < h2:
                write_output_file(D2, first_path)
                # print("chose comp2: " + str(h2) + " vs. " + str(h1))
                changed += 1
                improvement += (h2 - h1) / h1
            else:
                # print("chose comp1: " + str(h1) + " vs. " + str(h2))
                kept += 1
    print("changed " + str(changed) + ", kept " + str(kept))
    print("average improvement: " + (str(0) if changed == 0 else (str(round(improvement / changed * 100, 1)) + "%")))