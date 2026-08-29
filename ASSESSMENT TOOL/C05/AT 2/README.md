# Intelligent Machine Fault Diagnosis and Maintenance Decision Expert System Using Prolog

## Aim
To develop a rule-based expert system in Prolog that diagnoses probable machine faults from observed operating symptoms and recommends suitable maintenance actions.

## Introduction
Unexpected machine failures can interrupt manufacturing, increase maintenance cost, and reduce productivity. This project uses a Prolog expert system to reason from machine-condition observations such as abnormal vibration, excessive temperature, unusual noise, pressure change, reduced speed, unstable operation, bearing heat, and high current.

The system covers imbalance, shaft misalignment, bearing wear, mechanical looseness, lubrication failure, pressure-system fault, and motor overload. It demonstrates forward chaining, backward chaining, unification, and backtracking.

## Pseudocode

### Forward Chaining
1. Read machine observations.
2. Store each observation as a symptom fact.
3. Check every fault rule.
4. Verify whether all required symptoms are present.
5. Derive the matching fault.
6. Continue checking the remaining rules.
7. Return all supported faults and maintenance actions.

### Backward Chaining
1. Receive a suspected fault as the goal.
2. Find the rule whose conclusion matches the suspected fault.
3. Retrieve the required symptoms.
4. Prove every required symptom from working memory.
5. If all succeed, prove the fault.
6. Otherwise fail or backtrack.

## Test Cases and Outputs

### Test Case 1 - Imbalance
Query: `scenario(1), forward_chain(m1, Faults).`
Real SWISH output: `Faults = [imbalance]`

### Test Case 2 - Misalignment
Query: `scenario(2), verify_fault(m2, misalignment).`
Real SWISH output: `true`

### Test Case 3 - Bearing Wear
Query: `scenario(3), recommendation(m3, Fault, Action).`
Expected from the same knowledge base: `Fault = bearing_wear`

### Test Case 4 - Pressure System Fault
Query: `scenario(4), forward_chain(m4, Faults).`
Real SWISH output: `Faults = [pressure_system_fault]`

### Test Case 5 - Motor Overload
Query: `scenario(5), forward_chain(m5, Faults).`
Real SWISH output: `Faults = [motor_overload]`

### Test Case 6 - Multi-Fault Reasoning
Query: `scenario(6), recommendation(m6, Fault, Action).`
Real SWISH output shown: `Fault = bearing_wear`

Additional query: `scenario(6), forward_chain(m6, Faults).`
Real SWISH output: `Faults = [bearing_wear, lubrication_failure]`

## Screenshots
The `screenshots` folder contains genuine screenshots cropped from the user's actual SWISH execution session. No generated console screenshot is presented as real execution evidence.

## Technology Used
- SWI-Prolog / SWISH
- Prolog
- Rule-Based Expert System
- Forward Chaining
- Backward Chaining
- Unification
- Backtracking

## Main Program
`machine_fault_expert.pl`

## Author
Rashmitha Senthil Kumar
