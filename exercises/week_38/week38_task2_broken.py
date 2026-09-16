# Each of these three functions have an error
# Fix the errors and include a comment stating why it was wrong

def create_game_board(size: int = 3) -> list[list[str]]:
    """Creates a square board initialized with empty slots ('-')."""
    return [["-"] * size] * size


def sanitize_scores(scores: list[int], threshold: int) -> list[int]:
    """Replaces any score below threshold with 0, keeping higher scores intact."""
    return [score for score in scores if score >= threshold else 0]


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """Flattens a 2D matrix into a 1D list."""
    return [item for item in sublist for sublist in matrix]


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
# Expected: [85, 0, 90, 0]

# Test 3: Matrix flattening
grid = [[1, 2], [3, 4]]
flat = flatten_matrix(grid)
# Expected: [1, 2, 3, 4]
