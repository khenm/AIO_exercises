def levenshtein_distance(source: str, target: str):
    """Levenshtein distance is presented as
    the differences between 2 strings, which is the minimum 
    number of steps to convert string 'source' to string 'target'
    according to 3 transformations:
    - Delete a character
    - Add a character
    - Change a character to another.

    Args:
        source (str): the source string
        target (str): the target string to be converted to
    """
    # step 1 -- create a matrix, in which
    # rows represent insertion, columns represent deletion and
    # diagonals represent substitution.
    M: int = len(source) + 1  # number of rows
    N: int = len(target) + 1  # number of columns
    trans_matrix = [[0 for _ in range(N)] for _ in range(M)]

    # step 2 -- finish the first and second row
    for i in range(M):
        trans_matrix[i][0] = i
    for j in range(N):
        trans_matrix[0][j] = j

    # step 3 -- calculate the remaining cells
    for i in range(1, M):
        for j in range(1, N):
            deletion_cost: int = trans_matrix[i - 1][j] + 1
            insertion_cost: int = trans_matrix[i][j - 1] + 1
            match_cost: int = 0 if source[i - 1] == target[j - 1] else 1
            substitution_cost: int = trans_matrix[i - 1][j - 1] + match_cost
            trans_matrix[i][j] = min(
                deletion_cost, insertion_cost, substitution_cost)

    # step 4 -- backtrace
    path: list[tuple] = []
    current_row = M - 1
    current_col = N - 1
    path.append((current_row, current_col))
    while current_row != 0 and current_col != 0:
        # delete
        deletion_cost = trans_matrix[current_row - 1][current_col]
        deletion_cell = (deletion_cost, (current_row - 1, current_col))
        # insert
        insertion_cost = trans_matrix[current_row][current_col - 1]
        insertion_cell = (insertion_cost, (current_row, current_col - 1))
        # substitute
        substitution_cost = trans_matrix[current_row - 1][current_col - 1]
        substitution_cell = (
            substitution_cost, (current_row - 1, current_col - 1))
        _, next_position = min(
            deletion_cell, substitution_cell, insertion_cell)
        path.append(next_position)
        current_row, current_col = next_position  # get next position

    # step 5 -- result
    print(f'Minimum edit cost: {trans_matrix[M - 1][N - 1]}')
    print("Trace: ")
    for i in range(len(path)):
        if (i == len(path) - 1):
            print(path[i])
            break
        print(path[i], end=" -> ")


def main():
    source: str = 'yu'
    target: str = 'you'
    levenshtein_distance(source=source, target=target)


if __name__ == "__main__":
    main()
