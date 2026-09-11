from typing import Any


def calculate_grade_stats(
    student_list: list[dict[str, str]], pass_threshold: float = 50.0
) -> dict[str, Any]:
    """
    Calculate average score and identify passing students.

    A note about the type hints here:
    The hint dict[str, Any] indicates that the function returns a dictionary where the keys are strings
    and the values can be of any type.

    Args:
        student_list: List of dictionaries containing student names and scores.
        pass_threshold: Score threshold for passing. Default is 50.0.
    Returns:
        Dictionary containing average score, list of passed students, and total count.
    """

    # total_score is initialized to 0.0 to accumulate the total score of all students.
    # At the end of the loop, we will divide this total by the number of students to get the average score.
    total_score = 0.0
    passed_students = []

    for student in student_list:
        # The input score is a string, so we need to convert it to a float for calculations.
        score = float(student["score"])
        if score >= pass_threshold:
            passed_students.append(student["name"])
        total_score += score

    total_count = len(student_list)
    avg = total_score / total_count if total_count > 0 else 0.0

    return {
        "average": avg,
        "passed": passed_students,
        "total_count": total_count,
    }


def print_summary(
    stats_dict: dict[str, Any], course_name: str = "Python 101"
) -> None:
    """
    Print a formatted summary of class statistics.

    Args:
        stats_dict: Dictionary containing average score, list of passed students, and total count.
        course_name: Name of the course. Default is "Python 101".
    Returns:
        None, as this function prints the summary directly to the console.
    """
    print(f"=== Summary for {course_name} ===")
    print(f"Average Score: {stats_dict['average']:.2f}")
    print(f"Passed Students: {', '.join(stats_dict['passed'])}")


if __name__ == "__main__":
    data = [{'name': 'Charlie', 'score': '85.5'},
            {'name': 'River', 'score': '42.0'},
            {'name': 'Jordan', 'score': '68.0'}
            ]
    res = calculate_grade_stats(data)
    print_summary(res)
