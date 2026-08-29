% Cybersecurity Threat Detection Expert System

failed_login_count(alice, 6).
unusual_location(alice, berlin).
privilege_escalation(alice).
suspicious_file_access(alice, payroll_db).
abnormal_network_traffic(ws17).
owns(alice, ws17).

repeated_login_failures(User) :-
    failed_login_count(User, Count),
    Count >= 5.

brute_force_attempt(User) :-
    repeated_login_failures(User).

suspicious_login(User) :-
    unusual_location(User, _).

compromised_account(User) :-
    brute_force_attempt(User),
    suspicious_login(User).

privilege_misuse(User) :-
    privilege_escalation(User),
    suspicious_file_access(User, _).

possible_data_exfiltration(User) :-
    owns(User, Device),
    suspicious_file_access(User, _),
    abnormal_network_traffic(Device).

high_risk_account(User) :-
    compromised_account(User),
    privilege_escalation(User).

critical_threat(User) :-
    high_risk_account(User),
    possible_data_exfiltration(User).

recommend(User, isolate_device) :-
    critical_threat(User).

recommend(User, reset_credentials) :-
    critical_threat(User).

recommend(User, review_access_logs) :-
    privilege_misuse(User).

all_recommendations(User, Actions) :-
    setof(Action, recommend(User, Action), Actions).
