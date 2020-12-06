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

- Since the first approach we used for the solver was simulated annealing, we tried to make solutions that would be hard to solve with simulated annealing, which are inputs that have very few possible solutions. We placed the students in two rooms, and made the students in the same room have high happiness and low stress and the students in different rooms have low happiness and high stress. This ensured that there was only one optimal solution and we could find it easily. In retrospect, our inputs are pretty easily solved with a greedy algorithm, so we probably would have tried making our inputs have more solutions, but still "spaced out" from each other. We could see this in some of the other inputs, which had some people at the optimal solution and many at another less optimal solutions.
- We ended up using multiple algorithms: a simulated annealing based algorithm, which starts the students in different rooms and moves them around randomly, a greedy algorithm, which places one student in each room then tries to maximize happiness at every step while keeping the stress below the maximum, and a random algorithm, which just assigns students randomly repeatedly. The simulated annealing algorithm is valuable because it allows us to test across a wide range of inputs in a relatively efficient fashion, and it provided us with a solid baseline for the small and medium inputs. The greedy algorithm is valuable because even though it looks for far fewer solutions, it does so extremely quickly, so by simply shuffling the students before running the algorithm, we can test for a variety of different scenarios. Finally, the random algorithm wors great when there are not very many solutions to test; i.e. the small inputs. By running a few iterations of the random algorithm, we were able to solve all of the small inputs very quickly. For our final outputs, we simply chose the best output over the course of running all of the different algorithms; we did this using `comparator.py`, which compares two sets of outputs and writes the best option to a folder.
- We tried many variations on all of our algorithms.
    - Simulated annealing: One change we tried was how we initially assigned the students: assigning them randomly, assigning one per room, or assigning them to match our current solution. The thought process was that assigining them one of those ways would put us closer to a solution. However, they didn't do much to overcome the problem with simulated annealing on larger inputs, which is that solutions are simply to sparse. We also tried different ways of moving the students: moving a random student into a random room (or creating a new room if possible), swapping two students, and moving based on a heuristic on happiness and stress. All of them occasionally produced improvements, but moving random students and swapping two students produced similar results, and we ultimately could not produce a good enough heuristic, if it exists, to consistently get better results. Finally we tried using happiness and stress values to produce an energy value that would get us closer to a valid optimal solution if we were currently at an invalid solution, but this also produced negligible results and produced wildly different energy values depending on the happiness value of the optimal solution.
    - Greedy: After implementing a naive greedy algorithm, we noticed that it would begin by placing all students in one room, so we changed the algorithm to begin by placing one student in each room, then running greedy. This gave us significantly better results. However, the problem with greedy is that the results don't change very much test to test, and shuffling the order the students are entered can only do so much. We tried adding a random element, which would place a student randomly half the time, but this also did not do much for performance.
    - Random: The random algorithm did great for smalls, but for mediums and larges, there were too many possible solutions and it did not perform very well. We tried having a greedy portion kick in after a certain student (essentially making a greedy algorithm with more initial randomness), but this also didn't do too much.
- We used a simulated annealing Python module on [Github](https://github.com/perrygeo/simanneal), which allowed us to easily implement and alter our algorithm.
- If given more time, we would try other approaches to the problem. Although we couldn't figure out a silver bullet integer linear programming approach, we realized late on it is possible to constrain certain variables and make an LP that way. We probably would have tried constraining some variables and running an ILP solver to see if we could get better solutions. We also probably would have tried tinkering with our existing solutions more, including possibly working to find a better heuristic for simulated annealing that would have led it to find better solutions, especially for the larger inputs. There aren't many other things we would do if given more time, unless we could have found a different approach that yielded significantly better results. 