class FamilyTreeKB:
  def __init__(self):
    self.facts = set()          # Known relationships (facts)
    self.rules = []             # inference rules

  def add_fact(self, fact):
    self.facts.add(fact)        # add known relationships (facts) to the KB

  def add_rule(self, conditions, conclusion):
    self.rules.append((conditions, conclusion))     # add inference rules

  def match(self, fact, condition):                  # Match a fact to a condition, handling variables
    if len(fact) != len(condition):
        return None  # Mismatch in length
    substitution = {}
    for f, c in zip(fact, condition):
        if c.startswith("!"):  # Negation (e.g., "!= X")
             if f == substitution.get(c[1:], f):
                return None
        elif c.isupper():  # Variable (e.g., "X")
            if c in substitution:
                if substitution[c] != f:
                    return None
            else:
                substitution[c] = f
        elif f != c:  # Constant mismatch
            return None
    return substitution

  def substitute(self, pattern, substitution):                # Substitute variables in a pattern with actual values
      return tuple(substitution.get(p, p) for p in pattern)

  def generate_combinations(self, conditions):                # Generate all combinations of facts matching the conditions
      from itertools import product
      return product(self.facts, repeat=len(conditions))

  def forward_chain(self):                                      # Forward chaining to infer new rules from known facts
    while True:
        new_fact_added = False
        for conditions, conclusion in self.rules:
          for fact_set in self.generate_combinations(conditions):
            substitutions = [self.match(f, c) for f, c in zip(fact_set, conditions)]
            if all(substitutions):
             # Combine substitutions
              merged_sub = {}
              for sub in substitutions:
                merged_sub.update(sub)
            # Substitute variables in conclusion
            derived_fact = self.substitute(conclusion, merged_sub)
            if derived_fact not in self.facts:
                self.facts.add(derived_fact)
                new_fact_added = True
                print(f"Derived fact: {derived_fact}")
        if not new_fact_added:
            break
    return self.facts


kb = FamilyTreeKB()             # create family tree KB

# add basic family relationships (Facts)
kb.add_fact(("parent", "John", "Mary"))
kb.add_fact(("parent", "John", "Tom"))
kb.add_fact(("parent", "Sarah", "Mary"))
kb.add_fact(("parent", "Sarah", "Tom"))
kb.add_fact(("parent", "Mary", "Sam"))
kb.add_fact(("parent", "Tom", "Lisa"))

# add rules to infer other relationships(facts)
kb.add_rule([("parent", "X", "Y")], ("child", "Y", "X"))    # If X is parent of Y, then Y is child of X
kb.add_rule([("parent", "X", "Y"), ("parent", "X", "Z"), ("Y", "!=", "Z")], ("siblings", "Y", "Z"))     # siblings rule
kb.add_rule([("parent", "X", "Y"), ("parent", "Y", "Z")], ("grandparent", "X", "Z"))                    # grandparent rule

# Apply forward chaining to infer relationships
print("Initial Facts:", kb.facts)
kb.forward_chain()
print("Final Facts:", kb.facts)
