% Medical Diagnosis Expert System

% Disease rules

diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

diagnosis(common_cold) :-
    symptom(sneezing),
    symptom(runny_nose),
    symptom(sore_throat).

diagnosis(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

diagnosis(typhoid) :-
    symptom(fever),
    symptom(headache),
    symptom(stomach_pain).

diagnosis(asthma) :-
    symptom(shortness_of_breath),
    symptom(wheezing),
    symptom(chest_tightness).

diagnosis(migraine) :-
    symptom(headache),
    symptom(nausea),
    symptom(sensitivity_to_light).

% Sample symptom facts

symptom(fever).
symptom(cough).
symptom(body_pain).
