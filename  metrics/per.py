def calculate_per(reference, hypothesis):
    reference = list(reference) 
    hypothesis = list(hypothesis)

    substitutions = sum(r != h for r, h in zip(reference, hypothesis))
    deletions = max(0, len(reference) - len(hypothesis))
    insertions = max(0, len(hypothesis) - len(reference))

    per = (substitutions + deletions + insertions) / len(reference)

    return per