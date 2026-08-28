% Intelligent Machine Fault Diagnosis and Maintenance Decision Expert System
:- dynamic symptom/2.

fault_rule(imbalance, [abnormal_vibration, radial_vibration, reduced_speed]).
fault_rule(misalignment, [abnormal_vibration, axial_vibration, excessive_temperature]).
fault_rule(bearing_wear, [abnormal_vibration, unusual_noise, excessive_temperature]).
fault_rule(mechanical_looseness, [abnormal_vibration, rattling_noise, unstable_operation]).
fault_rule(lubrication_failure, [excessive_temperature, unusual_noise, bearing_heat]).
fault_rule(pressure_system_fault, [pressure_change, reduced_speed, unstable_operation]).
fault_rule(motor_overload, [excessive_temperature, reduced_speed, high_current]).

maintenance(imbalance, 'Inspect rotor/fan, clean deposits, check balance and dynamically rebalance.').
maintenance(misalignment, 'Check coupling and shaft alignment; perform precision realignment.').
maintenance(bearing_wear, 'Inspect bearing condition and lubrication; replace damaged bearing if confirmed.').
maintenance(mechanical_looseness, 'Inspect mounts, bolts, baseplate and bearing housing; tighten or repair loose parts.').
maintenance(lubrication_failure, 'Verify lubricant type, level and delivery; correct lubrication and inspect bearing damage.').
maintenance(pressure_system_fault, 'Inspect pressure source, valves, filters, lines and leakage; restore normal pressure.').
maintenance(motor_overload, 'Check mechanical load and electrical current; remove overload and inspect motor cooling.').

all_present(_, []).
all_present(M, [S|Ss]) :-
    symptom(M,S),
    all_present(M,Ss).

probable_fault(M, Fault) :-
    fault_rule(Fault, Required),
    all_present(M, Required).

recommendation(M, Fault, Action) :-
    probable_fault(M, Fault),
    maintenance(Fault, Action).

verify_fault(M, Fault) :-
    probable_fault(M, Fault).

explain(M, Fault, Required, Action) :-
    fault_rule(Fault, Required),
    all_present(M, Required),
    maintenance(Fault, Action).

forward_chain(M, Faults) :-
    findall(F, probable_fault(M,F), Raw),
    sort(Raw, Faults).

clear_case :- retractall(symptom(_,_)).
add(M,S) :- assertz(symptom(M,S)).

scenario(1) :-
    clear_case,
    add(m1,abnormal_vibration),
    add(m1,radial_vibration),
    add(m1,reduced_speed).

scenario(2) :-
    clear_case,
    add(m2,abnormal_vibration),
    add(m2,axial_vibration),
    add(m2,excessive_temperature).

scenario(3) :-
    clear_case,
    add(m3,abnormal_vibration),
    add(m3,unusual_noise),
    add(m3,excessive_temperature).

scenario(4) :-
    clear_case,
    add(m4,pressure_change),
    add(m4,reduced_speed),
    add(m4,unstable_operation).

scenario(5) :-
    clear_case,
    add(m5,excessive_temperature),
    add(m5,reduced_speed),
    add(m5,high_current).

scenario(6) :-
    clear_case,
    add(m6,abnormal_vibration),
    add(m6,unusual_noise),
    add(m6,excessive_temperature),
    add(m6,bearing_heat).
