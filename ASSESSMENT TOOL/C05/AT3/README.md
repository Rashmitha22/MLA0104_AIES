# Cybersecurity Threat Detection Expert System

## Aim

To develop an explainable rule-based expert system that detects cybersecurity threats from repeated login failures, unusual login locations, privilege escalation, suspicious file access and abnormal network traffic.

## Introduction

The project represents the same cybersecurity knowledge as Prolog facts and rules. It correlates evidence belonging to the same user and device, then derives conclusions such as brute-force attempt, compromised account, possible data exfiltration and critical threat.

## Files

- `cybersecurity_expert.pl` — complete Prolog knowledge base.
- `test_queries.pl` — SWI-Prolog unit tests.
- `run_validation.py` — dependency-free validation of the same rule chain and screenshot generator.
- `outputs/query_results.txt` — actual recorded validation output.
- `screenshots/real_validation_output.png` — screenshot created from the executed validation run.

## Pseudocode

1. Load the observed cybersecurity facts.
2. Check whether failed login count is at least five.
3. Detect brute-force and suspicious-login conditions.
4. Combine both conditions to identify account compromise.
5. Correlate suspicious file access with abnormal traffic from the owned device.
6. Combine compromise, privilege escalation and exfiltration evidence.
7. Classify the event as a critical threat and recommend response actions.

## Run in SWISH

1. Open [SWISH](https://swish.swi-prolog.org/).
2. Copy all code from `cybersecurity_expert.pl` into the left editor.
3. Enter one query in the query box without typing `?-`.
4. Select **Run**.

Example queries:

```prolog
critical_threat(alice).
all_recommendations(alice, Actions).
critical_threat(bob).
```

Do not enter `[cybersecurity_expert].` in SWISH. SWISH automatically executes the program in its editor, and sandbox restrictions may reject file-consult commands.

## Run the Validation Package

```bash
python run_validation.py
```

The command writes the genuine output to `outputs/query_results.txt` and regenerates `screenshots/real_validation_output.png`.

## Result

All eight validation checks pass. The system identifies Alice's critical threat and response recommendations, while the unsupported query for Bob correctly returns false.

## Output Screenshot

![Real validation output](screenshots/real_validation_output.png)

## Conclusion

The expert system provides transparent and reusable threat-detection rules. Prolog is suitable for this prototype because it represents relationships clearly and supports direct goal-based reasoning.
