#!/bin/bash

for i in {1..5}; do
    python3 solver.py $i
done
python3 comparator.py