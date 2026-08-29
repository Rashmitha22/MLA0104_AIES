:- begin_tests(cybersecurity_expert).
:- consult('cybersecurity_expert.pl').

test(repeated_failures) :- repeated_login_failures(alice).
test(brute_force) :- brute_force_attempt(alice).
test(compromised_account) :- compromised_account(alice).
test(privilege_misuse) :- privilege_misuse(alice).
test(data_exfiltration) :- possible_data_exfiltration(alice).
test(critical_threat) :- critical_threat(alice).
test(unsupported_user, [fail]) :- critical_threat(bob).

:- end_tests(cybersecurity_expert).
