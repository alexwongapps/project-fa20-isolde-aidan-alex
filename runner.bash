#!/bin/bash

for j in {1..5}; do
    echo $j
    for i in {1..242}; do
        python3 solver.py $i 1
    done
    python3 comparator.py  
    for i in {1..242}; do
        python3 solver.py $i 0
    done
    python3 comparator.py  
done