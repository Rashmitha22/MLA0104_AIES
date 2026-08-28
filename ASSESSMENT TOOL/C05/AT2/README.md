# Intelligent Machine Fault Diagnosis and Maintenance Decision Expert System Using Prolog

## Overview
This project implements a rule-based expert system using SWI-Prolog for preliminary machine fault diagnosis and maintenance decision support in a manufacturing environment.

## Assessment
- Course: Artificial Intelligence and Expert Systems
- Assessment: CO5 Assessment Tool 2 – Industry Problem-Based Assignment
- Domain: Manufacturing
- Topic: Machine Fault Diagnosis Expert System

## Faults Covered
1. Imbalance
2. Shaft Misalignment
3. Bearing Wear
4. Mechanical Looseness
5. Lubrication Failure
6. Pressure System Fault
7. Motor Overload

## Main AI / Expert-System Concepts
- Production rules
- Forward chaining
- Backward chaining
- Unification
- Backtracking
- Explainable rule-based inference

## Main File
`machine_fault_expert.pl`

## How to Run
1. Install SWI-Prolog.
2. Open SWI-Prolog in this project folder.
3. Load the file:
```prolog
?- [machine_fault_expert].
```
4. Run the queries in `test_queries.txt`.

## Example
```prolog
?- scenario(1), forward_chain(m1, Faults).
Faults = [imbalance].
```

## Repository Contents
- `machine_fault_expert.pl` – complete Prolog knowledge base and inference logic
- `README.md` – project documentation
- `test_queries.txt` – six test cases and expected outputs
- `GITHUB_UPLOAD_INSTRUCTIONS.txt` – simple upload steps
- `screenshots/README.txt` – filenames to use for real SWI-Prolog execution screenshots

## Important
The screenshots folder is intentionally left for genuine SWI-Prolog execution screenshots. Do not upload fabricated execution images.

## Author
Rashmitha Senthil Kumar
