from breakout import *
from parse import *
from utils import *

G, stress_budget = read_input_file("samples/10.in")
problem = BreakoutProblem(G, stress_budget)
zoom, happiness = problem.anneal()
print("\n")
print(zoom.rooms, happiness)