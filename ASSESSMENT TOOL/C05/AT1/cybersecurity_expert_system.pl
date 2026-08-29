/*
  CyberShield-ES
  Cybersecurity threat detection using knowledge representation and reasoning.

  Load in SWI-Prolog:
      ?- [cybersecurity_expert_system].
*/

% ----------------------------
% Observed cybersecurity facts
% ----------------------------

failed_login_count(alice, 6).
unusual_location(alice, berlin).
privilege_escalation(alice).
suspicious_file_access(alice, payroll_db).
abnormal_network_traffic(ws17).
owns(alice, ws17).

% ----------------------------
% Threat-diagnosis rules
% ----------------------------

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

% ----------------------------
% Recommended defensive actions
% ----------------------------

recommend(User, isolate_device) :-
    critical_threat(User).

recommend(User, reset_credentials) :-
    critical_threat(User).

recommend(User, review_access_logs) :-
    privilege_misuse(User).

recommend(User, enforce_mfa) :-
    brute_force_attempt(User),
    \+ compromised_account(User).

all_recommendations(User, Actions) :-
    setof(Action, recommend(User, Action), Actions).

% ----------------------------
% Explanation facility
% ----------------------------

explain_critical_threat(User) :-
    format('Goal: critical_threat(~w)~n', [User]),
    check(compromised_account(User)),
    check(privilege_escalation(User)),
    check(possible_data_exfiltration(User)),
    format('Conclusion: critical_threat(~w) is proved.~n', [User]).

check(Goal) :-
    format('Checking ~q ... ', [Goal]),
    ( call(Goal) ->
        writeln(true)
    ;
        writeln(false),
        fail
    ).

% ----------------------------
% Human-readable diagnosis
% ----------------------------

diagnose(User) :-
    format('=== CyberShield-ES Diagnosis: ~w ===~n', [User]),
    print_result('Repeated login failures', repeated_login_failures(User)),
    print_result('Brute-force attempt', brute_force_attempt(User)),
    print_result('Suspicious login', suspicious_login(User)),
    print_result('Compromised account', compromised_account(User)),
    print_result('Privilege misuse', privilege_misuse(User)),
    print_result('Possible data exfiltration', possible_data_exfiltration(User)),
    print_result('High-risk account', high_risk_account(User)),
    print_result('Critical threat', critical_threat(User)),
    ( all_recommendations(User, Actions) ->
        format('Recommended actions: ~w~n', [Actions])
    ;
        writeln('Recommended actions: none')
    ).

print_result(Label, Goal) :-
    ( call(Goal) -> Status = 'DETECTED' ; Status = 'NOT DETECTED' ),
    format('~w: ~w~n', [Label, Status]).

