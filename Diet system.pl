% Disease-Based Diet Suggestion System

diet(diabetes, vegetables, sugary_foods).
diet(hypertension, low_salt_food, salty_foods).
diet(obesity, low_calorie_food, fried_foods).
diet(anemia, iron_rich_food, junk_food).
diet(heart_disease, low_fat_food, fatty_foods).
diet(constipation, fibre_rich_food, processed_foods).
diet(ulcer, soft_food, spicy_foods).

% Rule to display diet suggestion

suggest_diet(Disease) :-
    diet(Disease, RecommendedFood, AvoidFood),
    write('Disease: '),
    write(Disease),
    nl,
    write('Recommended food: '),
    write(RecommendedFood),
    nl,
    write('Food to avoid: '),
    write(AvoidFood),
    nl.
