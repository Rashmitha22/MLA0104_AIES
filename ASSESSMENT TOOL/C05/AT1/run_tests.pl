:- ['cybersecurity_expert_system.pl'].

:- begin_tests(cybershield_es).

test(repeated_login_failures) :-
    repeated_login_failures(alice).

test(brute_force_attempt) :-
    brute_force_attempt(alice).

test(suspicious_login) :-
    suspicious_login(alice).

test(compromised_account) :-
    compromised_account(alice).

test(privilege_misuse) :-
    privilege_misuse(alice).

test(possible_data_exfiltration) :-
    possible_data_exfiltration(alice).

test(high_risk_account) :-
    high_risk_account(alice).

test(critical_threat) :-
    critical_threat(alice).

test(unknown_user_has_no_critical_threat, [fail]) :-
    critical_threat(bob).

test(all_recommendations) :-
    all_recommendations(alice, Actions),
    Actions == [isolate_device, reset_credentials, review_access_logs].

:- end_tests(cybershield_es).

run_all_tests :-
    run_tests([cybershield_es]).

