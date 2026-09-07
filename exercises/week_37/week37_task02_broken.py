def process_class_scores(scores: list[float], pass_threshold: float = 50.0) -> float:
    """Removes failing scores and returns the average of passing students."""
    # Remove all scores below the passing threshold
    for score in scores:
        if score < pass_threshold:
            scores.remove(score)

    # Return the average of passing scores
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


# Test dataset of scores
student_scores = [45, 30, 85, 90, 25, 10, 60]
avg = process_class_scores(student_scores)

# Print the average of passing scores (should be 78.33)
print(f"Average: {avg:.2f}")