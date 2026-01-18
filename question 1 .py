
# Board Visualization

def visualizeBoard(board: list[list[int]]) -> None:
    size = len(board)
    print("\nBoard:")
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join("Q" if cell == 1 else "." for cell in row))
    print()


# Safety Check

def isSafe(board: list[list[int]], row: int, col: int, size: int) -> bool:
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < size:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Las Vegas 

def nQueensLasVegas(size: int) -> tuple[bool, list[list[int]]]:
    board = [[0 for _ in range(size)] for _ in range(size)]

    offset = 1  # used to vary choices deterministically

    for row in range(size):
        valid_positions = []

        for col in range(size):
            if isSafe(board, row, col, size):
                valid_positions.append(col)

        if not valid_positions:
            return False, board  # failure condition

        # Deterministic "pseudo-random" selection
        index = (row * offset) % len(valid_positions)
        chosen_col = valid_positions[index]
        board[row][chosen_col] = 1

        offset += 1

    return True, board


# Backtracking

def nQueensBacktracking(size: int) -> tuple[bool, list[list[int]]]:
    board = [[0 for _ in range(size)] for _ in range(size)]

    def solve(row: int) -> bool:
        if row == size:
            return True

        for col in range(size):
            if isSafe(board, row, col, size):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0

        return False

    success = solve(0)
    return success, board


# Backtracking with Starting Position

def nQueensBacktrackingVersion2(
    size: int, startingPosition: tuple[int, int]
) -> tuple[bool, list[list[int]]]:

    start_row, start_col = startingPosition
    board = [[0 for _ in range(size)] for _ in range(size)]
    board[start_row][start_col] = 1

    def solve(row: int) -> bool:
        if row == size:
            return True

        if row == start_row:
            return solve(row + 1)

        for col in range(size):
            if isSafe(board, row, col, size):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0

        return False

    success = solve(0)
    return success, board


# Input Manager

def main():
    while True:
        try:
            print("\nN-Queens Problem")
            print("1. Backtracking")
            print("2. Backtracking (with starting queen)")
            print("3. Las Vegas (no randomness)")
            print("4. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "4":
                print("Exiting program.")
                break

            size = int(input("Enter board size (N): "))
            if size <= 0:
                raise ValueError

            # Empty board
            empty = [[0 for _ in range(size)] for _ in range(size)]
            visualizeBoard(empty)

            if choice == "1":
                success, board = nQueensBacktracking(size)

            elif choice == "2":
                r = int(input("Enter starting row: "))
                c = int(input("Enter starting column: "))
                if not (0 <= r < size and 0 <= c < size):
                    print("Invalid starting position.")
                    continue
                success, board = nQueensBacktrackingVersion2(size, (r, c))

            elif choice == "3":
                success, board = nQueensLasVegas(size)

            else:
                print("Invalid choice.")
                continue

            # Final visualization
            visualizeBoard(board)
            print("Solution found!" if success else "No solution found.")

        except ValueError:
            print("Invalid input. Please enter integers only.")



# Program Entry Point

if __name__ == "__main__":
    main()



      

