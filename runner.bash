#!/bin/bash

for i in {1..10}; do
    echo $i
    python3 solver.py
    python3 comparator.py
done