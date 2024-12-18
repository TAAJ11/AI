facts = ["A", "B"]           # known facts

# (condition, conclusion) inference rules
rules = [
    (["A", "B"], "C"),       # If A and B are true, then infer C
    (["C"], "D"),            # If C is true, then infer D
    (["D"], "E")             # If D is true, then infer E
]

def backward_chaining(goal, facts, rules):
  if goal in facts:
    print(f"Goal {goal} is already a fact!")
    return True

  for condition, conclusion in rules:
    if conclusion == goal:
      print(f"Trying to infer {goal} using the rule: {conclusion} -> {goal}")

      # recursively check if all conditions are met
      all_conditions_met = True
      for cond in condition:
        if not backward_chaining(cond, facts, rules):
          all_conditions_met == False
          break
      if all_conditions_met:
        print(f"Goal {goal} inferred successfully!")
        return True

  print(f"Goal {goal} cannot be inferred!")
  return False

goal = "E"
print(f"Trying to prove goal: {goal}")
if backward_chaining(goal, facts, rules):
  print(f"Goal {goal} has been proven")
else:
  print(f"Goal {goal} cannot be proven")
