#!/bin/bash

for i in {122..242}; do
    python3 solver.py $i
done
python3 comparator.py