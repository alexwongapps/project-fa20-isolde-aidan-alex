#!/bin/bash

for i in {1..1}; do
    python3 solver.py $i
    python3 comparator.py
done