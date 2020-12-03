# CS 170 Project Fall 2020

Take a look at the project spec before you get started!

Requirements:

Python 3.6+

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

If using pip to download, run `python3 -m pip install networkx`


Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
  - These are the functions run by the autograder to validate submissions

# Reflection

- Since the first approach we used for the solver was simulated annealing, we tried to make solutions that would be hard to solve with simulated annealing, which are inputs that have very few possible solutions. We placed the students in two rooms, and made the students in the same room have high happiness and low stress and the students in different rooms have low happiness and high stress. In retrospect, our inputs are pretty easily solved with a greedy algorithm, so we probably would have tried making our inputs have more solutions, but still "spaced out" from each other.
- We ended up using multiple algorithms: a simulated annealing based algorithm, which starts the students in different rooms and moves them around randomly, a greedy algorithm, which tries to maximize happiness at every step while keeping the stress below the maximum, and a random algorithm, which just assigns students randomly repeatedly. We ran all of them and picked the best outputs.
- We tried different ways of moving the students in simulated annealing and different ways of selecting greedily. For simulated annealing, we tried assigning the students randomly or assigning one per room to start. For greedy, we tried putting one student in each room before selecting greedily.
- We used a simulated annealing Python module on [Github](https://github.com/perrygeo/simanneal).
- If given more time, we would try other approaches to the problem (like linear programming or other ways to solve these type of problems), as well as tinkering with our existing methods.