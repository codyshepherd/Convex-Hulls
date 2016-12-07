# Convex-Hulls
A test suite for various solutions to the Convex Hull problem.

## Directions
Run `python tests.py` to generate 18 .json files containing time results of each algorithm/dataset combination. Note that this will take a couple of hours at least.

Run `python unpack.py` to convert .json files into a series of plots comparing runtime with asymptotic curves. 

## Algorithms
Graham's Scan

Quick Hull

Chan's Algorithm

## Tests
Each algorithm solves six different datasets of 10 different sizes each.

## Datasets (all 2-Dimensional)
Random uniform

Ring

Fuzzy Ring

Colinear

Fuzzy Linear

Fan, reverse-sorted
