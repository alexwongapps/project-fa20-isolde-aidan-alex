#!/bin/bash

for j in {1..5}; do
    echo $j
    for i in {1..242}; do
        python3 solver2.py $i 1
    done
    python3 comparator2.py  
    for i in {1..242}; do
        python3 solver2.py $i 0
    done
    python3 comparator2.py  
done