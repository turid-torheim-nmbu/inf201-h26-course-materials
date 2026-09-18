def create_game_board(size: int = 3) -> list[list[str]]:
    """Creates a square board initialized with empty slots ('-')."""
    # The original code creates 3 references to the EXACT SAME inner list ["-"]
    # This list comprehension instead works like a for loop, creating a new list for each iteration
    return [["-"] * size for _ in range(size)]


def sanitize_scores(scores: list[int], threshold: int) -> list[int]:
    """Replaces any score below threshold with 0, keeping higher scores intact."""
    # This function has invalid syntax (placement) of the conditional logic in the list comprehensions
    # We need the condition (if-else) first, then the for loop
    return [score if score >= threshold else 0 for score in scores]


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """Flattens a 2D matrix into a 1D list."""
    # The nested loop variables were in the wrong order, as you can see by writing the statement out as loops:
    # result = []
    # for item in sublist:  # 'sublist' has not been defined yet
    #     for sublist in matrix:
    #    result.append(item)
    return [item for sublist in matrix for item in sublist]


# --- Test Execution ---
# Test 1: Board modification
board = create_game_board(3)
board[0][0] = "X"
print("Board Output:")
for row in board:
    print(row)
# Expected: Only top-left slot is "X"

# Test 2: Score sanitization
raw_scores = [85, 42, 90, 55]
cleaned = sanitize_scores(raw_scores, threshold=60)
print(cleaned)
# Expected: [85, 0, 90, 0]

# Test 3: Matrix flattening
grid = [[1, 2], [3, 4]]
flat = flatten_matrix(grid)
print(flat)
# Expected: [1, 2, 3, 4]
