expected = {
    "developer": {"Python Programming Test", "Cognitive Ability Test"},
    "sales": {"Communication Skills Test"}
}

predicted = {
    "developer": {"Python Programming Test", "Cognitive Ability Test"},
    "sales": {"Cognitive Ability Test"}
}

for role in expected:
    e = expected[role]
    p = predicted[role]
    correct = e & p
    precision = len(correct) / len(p) if p else 0
    recall = len(correct) / len(e) if e else 0
    print(f"{role} → Precision: {precision:.2f}, Recall: {recall:.2f}")
