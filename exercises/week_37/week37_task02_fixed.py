

def process_class_scores(scores: list[float], pass_threshold: float = 50.0) -> float:
    """
    Returns the average score of passing students.

    Args:
        scores: List of student scores.
        pass_threshold: Score threshold for passing. Default is 50.0.
    Returns:
        Average score of passing students. Returns 0.0 if no students passed.
    """

    # The error of the previous version was that it modified the input list in place,
    # which can lead to unexpected behavior. You can see this by adding the line
    # print(f"All student scores after processing: {scores}") at the end of the broken script.
    # Instead, we create a new list of passing scores using list comprehension.
    passing_scores = [score for score in scores if score >= pass_threshold]
    # Without list comprehension, it looks like this:
    # passing_scores = []
    # for score in scores:
    #     if score >= pass_threshold:
    #         passing_scores.append(score)

    if not passing_scores:
        return 0.0

    return sum(passing_scores) / len(passing_scores)


# Test dataset with consecutive failing grades
student_scores = [45, 30, 85, 90, 25, 10, 60]
avg = process_class_scores(student_scores)

# Note: The original list of scores remains unchanged, as we are not modifying it in place.
print(f"Average: {avg:.2f}")
print(f"All student scores after processing: {student_scores}")
