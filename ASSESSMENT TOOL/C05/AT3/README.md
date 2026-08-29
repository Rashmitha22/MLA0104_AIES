# Cybersecurity Threat Detection Expert System

## Aim

To develop an explainable rule-based expert system that detects cybersecurity threats from repeated login failures, unusual login locations, privilege escalation, suspicious file access and abnormal network traffic.

## Introduction

The project represents the same cybersecurity knowledge as Prolog facts and rules. It correlates evidence belonging to the same user and device, then derives conclusions such as brute-force attempt, compromised account, possible data exfiltration and critical threat.


## Pseudocode

1. Load the observed cybersecurity facts.
2. Check whether failed login count is at least five.
3. Detect brute-force and suspicious-login conditions.
4. Combine both conditions to identify account compromise.
5. Correlate suspicious file access with abnormal traffic from the owned device.
6. Combine compromise, privilege escalation and exfiltration evidence.
7. Classify the event as a critical threat and recommend response actions.

## Result

All eight validation checks pass. The system identifies Alice's critical threat and response recommendations, while the unsupported query for Bob correctly returns false.


## Conclusion

The expert system provides transparent and reusable threat-detection rules. Prolog is suitable for this prototype because it represents relationships clearly and supports direct goal-based reasoning.
