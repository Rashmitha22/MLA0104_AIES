def backward_chaining(
    goal,
    facts,
    rules,
    visited,
    trace,
    depth=0
):

    indentation = "    " * depth

    trace.append(
        f"{indentation}Trying to prove: {goal}"
    )

    # If the goal is already a known fact
    if goal in facts:
        trace.append(
            f"{indentation}Success: {goal} is a known fact"
        )
        return True

    # Prevent infinite loops
    if goal in visited:
        trace.append(
            f"{indentation}Failed: {goal} was already checked"
        )
        return False

    visited.add(goal)

    matching_rules = []

    for rule_number, rule in enumerate(rules, start=1):
        if rule["conclusion"] == goal:
            matching_rules.append(
                (rule_number, rule)
            )

    # No rule can derive the goal
    if not matching_rules:
        trace.append(
            f"{indentation}Failed: No rule concludes {goal}"
        )
        return False

    for rule_number, rule in matching_rules:
        premises = rule["premises"]

        trace.append(
            f"{indentation}Using Rule {rule_number}: "
            f"{' AND '.join(sorted(premises))} "
            f"-> {goal}"
        )

        all_premises_proved = True

        for premise in premises:
            trace.append(
                f"{indentation}Checking premise: {premise}"
            )

            premise_result = backward_chaining(
                premise,
                facts,
                rules,
                visited.copy(),
                trace,
                depth + 1
            )

            if not premise_result:
                all_premises_proved = False

                trace.append(
                    f"{indentation}Rule {rule_number} failed "
                    f"because {premise} could not be proved"
                )

                break

        if all_premises_proved:
            trace.append(
                f"{indentation}Success: {goal} proved "
                f"using Rule {rule_number}"
            )

            return True

    trace.append(
        f"{indentation}Failed: {goal} could not be proved"
    )

    return False


def format_fact(fact):
    """
    Format a fact for display.
    """

    return fact.replace("_", " ").title()


def main():
    print("=" * 70)
    print("                BACKWARD CHAINING")
    print("=" * 70)

    try:
        number_of_facts = int(
            input("Enter the number of known facts: ")
        )

        if number_of_facts < 0:
            print(
                "Error: Number of facts cannot be negative."
            )
            return

        facts = set()

        print("\nEnter the known facts:")

        for index in range(number_of_facts):
            fact = input(
                f"Fact {index + 1}: "
            ).strip().lower()

            if not fact:
                print(
                    "Error: Fact cannot be empty."
                )
                return

            facts.add(fact)

        number_of_rules = int(
            input("\nEnter the number of rules: ")
        )

        if number_of_rules < 0:
            print(
                "Error: Number of rules cannot be negative."
            )
            return

        rules = []

        print("\nEnter each rule.")
        print("Enter premises separated by commas.")
        print("Example premises: bird, can_fly")
        print("Example conclusion: flying_bird")

        for index in range(number_of_rules):
            print(f"\nRule {index + 1}")

            premise_input = input(
                "Enter premises: "
            ).strip().lower()

            conclusion = input(
                "Enter conclusion: "
            ).strip().lower()

            if not premise_input or not conclusion:
                print(
                    "Error: Premises and conclusion cannot be empty."
                )
                return

            premises = {
                premise.strip()
                for premise in premise_input.split(",")
                if premise.strip()
            }

            if not premises:
                print(
                    "Error: At least one premise is required."
                )
                return

            rules.append(
                {
                    "premises": premises,
                    "conclusion": conclusion
                }
            )

        goal = input(
            "\nEnter the goal to prove: "
        ).strip().lower()

        if not goal:
            print(
                "Error: Goal cannot be empty."
            )
            return

        trace = []

        result = backward_chaining(
            goal,
            facts,
            rules,
            set(),
            trace
        )

        print("\n" + "=" * 70)
        print("KNOWN FACTS")
        print("=" * 70)

        if facts:
            for fact in sorted(facts):
                print(
                    f"- {format_fact(fact)}"
                )
        else:
            print("No known facts.")

        print("\n" + "=" * 70)
        print("KNOWLEDGE BASE RULES")
        print("=" * 70)

        if rules:
            for index, rule in enumerate(
                rules,
                start=1
            ):
                premises_text = " AND ".join(
                    format_fact(premise)
                    for premise in sorted(
                        rule["premises"]
                    )
                )

                conclusion_text = format_fact(
                    rule["conclusion"]
                )

                print(
                    f"Rule {index}: "
                    f"IF {premises_text} "
                    f"THEN {conclusion_text}"
                )
        else:
            print("No rules entered.")

        print("\n" + "=" * 70)
        print("BACKWARD CHAINING TRACE")
        print("=" * 70)

        for step_number, message in enumerate(
            trace,
            start=1
        ):
            print(
                f"Step {step_number}: {message}"
            )

        print("\n" + "=" * 70)
        print("GOAL TEST")
        print("=" * 70)

        print(
            f"Goal: {format_fact(goal)}"
        )

        if result:
            print(
                "Goal status: Proved"
            )
        else:
            print(
                "Goal status: Not proved"
            )

        print("\n" + "=" * 70)
        print("FINAL RESULT")
        print("=" * 70)

        print(
            f"Known facts   : {len(facts)}"
        )

        print(
            f"Rules         : {len(rules)}"
        )

        print(
            f"Goal          : {format_fact(goal)}"
        )

        if result:
            print(
                "Result        : Goal successfully proved"
            )
        else:
            print(
                "Result        : Goal could not be proved"
            )

        print(
            f"Trace steps   : {len(trace)}"
        )

    except ValueError:
        print(
            "Error: Please enter valid integer values."
        )

    except Exception as error:
        print(
            f"Unexpected error: {error}"
        )


if __name__ == "__main__":
    main()
