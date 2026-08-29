/*
  CyberShield-ES
  Cybersecurity threat detection using knowledge representation and reasoning.

  Load in SWI-Prolog:
      ?- [cybersecurity_expert_system].
*/

% ----------------------------
% Observed cybersecurity facts
% ----------------------------

% Failed-login observations.
failed_login_count(alice, 6).
failed_login_count(charlie, 7).
failed_login_count(david, 1).
failed_login_count(bob, 1).

% Location and privilege observations.
unusual_location(alice, berlin).
privilege_escalation(alice).

% Sensitive-file observations.
suspicious_file_access(alice, payroll_db).
suspicious_file_access(david, customer_db).

% Device-traffic observations.
abnormal_network_traffic(ws17).
abnormal_network_traffic(ws30).

% User-device relationships.
owns(alice, ws17).
owns(charlie, ws21).
owns(david, ws30).
owns(bob, ws10).

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
% Explicit forward-chaining engine
% ----------------------------

% Observable facts are converted into symbolic working-memory facts.
forward_seed(User, repeated_login_failures) :-
    failed_login_count(User, Count),
    Count >= 5.

forward_seed(User, suspicious_login) :-
    unusual_location(User, _).

forward_seed(User, privilege_escalation) :-
    privilege_escalation(User).

forward_seed(User, sensitive_file_access) :-
    suspicious_file_access(User, _).

forward_seed(User, abnormal_owned_device_traffic) :-
    owns(User, Device),
    abnormal_network_traffic(Device).

% Production rules used by the forward-chaining engine.
forward_rule(brute_force_attempt,
             [repeated_login_failures]).

forward_rule(compromised_account,
             [brute_force_attempt, suspicious_login]).

forward_rule(privilege_misuse,
             [privilege_escalation, sensitive_file_access]).

forward_rule(possible_data_exfiltration,
             [sensitive_file_access, abnormal_owned_device_traffic]).

forward_rule(high_risk_account,
             [compromised_account, privilege_escalation]).

forward_rule(critical_threat,
             [high_risk_account, possible_data_exfiltration]).

forward_rule(isolate_device,
             [critical_threat]).

forward_rule(reset_credentials,
             [critical_threat]).

forward_rule(review_access_logs,
             [privilege_misuse]).

% Repeatedly fires every applicable rule until no new fact can be added.
forward_chain(User, FinalFacts) :-
    findall(Fact, forward_seed(User, Fact), SeedFacts0),
    sort(SeedFacts0, SeedFacts),
    format('Initial facts for ~w: ~w~n', [User, SeedFacts]),
    forward_fixpoint(SeedFacts, FinalFacts),
    format('Final closure for ~w: ~w~n', [User, FinalFacts]).

forward_fixpoint(CurrentFacts, FinalFacts) :-
    findall(Conclusion,
            ( forward_rule(Conclusion, Conditions),
              all_present(Conditions, CurrentFacts),
              \+ memberchk(Conclusion, CurrentFacts)
            ),
            NewFacts0),
    sort(NewFacts0, NewFacts),
    ( NewFacts = [] ->
        FinalFacts = CurrentFacts
    ;
        format('Newly derived facts: ~w~n', [NewFacts]),
        append(CurrentFacts, NewFacts, ExpandedFacts0),
        sort(ExpandedFacts0, ExpandedFacts),
        forward_fixpoint(ExpandedFacts, FinalFacts)
    ).

all_present([], _).
all_present([Condition|Conditions], Facts) :-
    memberchk(Condition, Facts),
    all_present(Conditions, Facts).

% ----------------------------
% Explanation facility
% ----------------------------

explain_critical_threat(User) :-
    format('Goal: critical_threat(~w)~n', [User]),
    trace_goal(critical_threat(User), 0),
    format('Conclusion: critical_threat(~w) is proved.~n', [User]).

trace_goal(critical_threat(User), Depth) :-
    trace_line(Depth, critical_threat(User)),
    Next is Depth + 1,
    trace_goal(high_risk_account(User), Next),
    trace_goal(possible_data_exfiltration(User), Next).

trace_goal(high_risk_account(User), Depth) :-
    trace_line(Depth, high_risk_account(User)),
    Next is Depth + 1,
    trace_goal(compromised_account(User), Next),
    trace_goal(privilege_escalation(User), Next).

trace_goal(compromised_account(User), Depth) :-
    trace_line(Depth, compromised_account(User)),
    Next is Depth + 1,
    trace_goal(brute_force_attempt(User), Next),
    trace_goal(suspicious_login(User), Next).

trace_goal(brute_force_attempt(User), Depth) :-
    trace_line(Depth, brute_force_attempt(User)),
    Next is Depth + 1,
    trace_goal(repeated_login_failures(User), Next).

trace_goal(repeated_login_failures(User), Depth) :-
    trace_line(Depth, repeated_login_failures(User)),
    Next is Depth + 1,
    failed_login_count(User, Count),
    Count >= 5,
    trace_fact(Next, failed_login_count(User, Count)).

trace_goal(suspicious_login(User), Depth) :-
    trace_line(Depth, suspicious_login(User)),
    Next is Depth + 1,
    unusual_location(User, Location),
    trace_fact(Next, unusual_location(User, Location)).

trace_goal(privilege_escalation(User), Depth) :-
    privilege_escalation(User),
    trace_fact(Depth, privilege_escalation(User)).

trace_goal(possible_data_exfiltration(User), Depth) :-
    trace_line(Depth, possible_data_exfiltration(User)),
    Next is Depth + 1,
    owns(User, Device),
    suspicious_file_access(User, File),
    abnormal_network_traffic(Device),
    trace_fact(Next, owns(User, Device)),
    trace_fact(Next, suspicious_file_access(User, File)),
    trace_fact(Next, abnormal_network_traffic(Device)).

trace_line(Depth, Goal) :-
    Indent is Depth * 2,
    format('~*cProve ~q~n', [Indent, 32, Goal]).

trace_fact(Depth, Fact) :-
    Indent is Depth * 2,
    format('~*cFact  ~q~n', [Indent, 32, Fact]).

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
