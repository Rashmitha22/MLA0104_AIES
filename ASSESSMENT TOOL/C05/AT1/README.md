
**Cybersecurity Threat Detection Using Knowledge Representation and Reasoning in SWI-Prolog**

## Aim

To design and implement a rule-based cybersecurity expert system using SWI-Prolog that analyses security evidence and identifies threats such as brute-force attacks, suspicious logins, compromised accounts, privilege misuse, data exfiltration and critical threats.

## Introduction

Cybersecurity systems generate many login, file-access and network events. Manually examining every event is difficult and may delay threat detection. A single security event may not confirm an attack, but several related events can indicate a serious threat.

CyberShield-ES is a rule-based expert system developed using SWI-Prolog. It represents security observations as facts and cybersecurity knowledge as logical rules. The system uses unification, backward chaining and backtracking to identify threats and recommend suitable defensive actions.

The system analyses repeated login failures, unusual login locations, privilege escalation, suspicious file access and abnormal network traffic. Based on these observations, it derives conclusions such as account compromise, high-risk activity and critical cybersecurity threats.

## Pseudocode

```text
BEGIN

    READ cybersecurity facts

    IF failed login count is greater than or equal to 5 THEN
        Detect repeated login failures
        Infer brute-force attempt
    END IF

    IF login occurs from an unusual location THEN
        Infer suspicious login
    END IF

    IF brute-force attempt AND suspicious login are detected THEN
        Infer compromised account
    END IF

    IF privilege escalation AND suspicious file access are detected THEN
        Infer privilege misuse
    END IF

    IF user owns the device
       AND user accesses a sensitive file
       AND device produces abnormal network traffic THEN
        Infer possible data exfiltration
    END IF

    IF compromised account AND privilege escalation are detected THEN
        Classify the account as high risk
    END IF

    IF high-risk account AND possible data exfiltration are detected THEN
        Infer critical cybersecurity threat
    END IF

    GENERATE applicable defensive recommendations

    DISPLAY threat diagnosis and recommendations

END
```

## Result

The CyberShield-ES program was executed using SWI-Prolog. For the user `alice`, the system detected:

* Repeated login failures
* Brute-force attempt
* Suspicious login
* Compromised account
* Privilege misuse
* Possible data exfiltration
* High-risk account
* Critical cybersecurity threat

The system generated the following defensive recommendations:

```text
isolate_device
reset_credentials
review_access_logs
```

The negative query for the unsupported user `bob` returned `false`, showing that the system does not generate a critical-threat conclusion without supporting facts.

## Conclusion

CyberShield-ES successfully demonstrates cybersecurity threat detection using Prolog facts and rules. It combines multiple security observations to produce explainable threat conclusions and defensive recommendations.

Prolog is suitable for this expert system because it supports logical rules, unification, backward chaining and backtracking. The system provides transparent and consistent reasoning. It can be extended in the future using real security logs, timestamps, adaptive thresholds, additional threat categories and a graphical monitoring interface.
