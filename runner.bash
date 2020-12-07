#!/bin/bash

for j in {1..1}; do
    echo $j
    for i in {1..242}; do
        python3 solver.py $i
    done
    python3 comparator.py  
    for i in {1..242}; do
        python3 solver2.py $i
    done
    python3 comparator.py  
done