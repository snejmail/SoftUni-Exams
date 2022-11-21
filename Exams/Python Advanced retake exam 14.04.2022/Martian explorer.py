from collections import deque


def calculate_position(matrix, row, col):
    if row < 0:
        row = len(matrix) - 1
    if col < 0:
        col = len(matrix) - 1
    if row >= len(matrix):
        row = 0
    if col >= len(matrix):
        col = 0
    return row, col


size = 6
matrix = []
martian_row = 0
martian_col = 0
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
suitable_area = False

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if matrix[row][col] == "E":
            martian_row, martian_col = row, col

commands = deque(input().split(', '))
while commands:

    command = commands.popleft()
    if command == "up":
        next_row, next_col = calculate_position(matrix, martian_row - 1, martian_col)
        martian_row, martian_col = next_row, next_col
    elif command == "down":
        next_row, next_col = calculate_position(matrix, martian_row + 1, martian_col)
        martian_row, martian_col = next_row, next_col
    elif command == "right":
        next_row, next_col = calculate_position(matrix, martian_row, martian_col + 1)
        martian_row, martian_col = next_row, next_col
    elif command == "left":
        next_row, next_col = calculate_position(matrix, martian_row, martian_col - 1)
        martian_row, martian_col = next_row, next_col

    if matrix[martian_row][martian_col] == "R":
        print(f"Rover got broken at ({martian_row}, {martian_col})")
        break

    if matrix[martian_row][martian_col] == "W":
        print(f"Water deposit found at ({martian_row}, {martian_col})")
        water_deposit += 1
    elif matrix[martian_row][martian_col] == "M":
        print(f"Metal deposit found at ({martian_row}, {martian_col})")
        metal_deposit += 1
    elif matrix[martian_row][martian_col] == "C":
        print(f"Concrete deposit found at ({martian_row}, {martian_col})")
        concrete_deposit += 1

    matrix[martian_row][martian_col] = "E"

    if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
        suitable_area = True

if suitable_area:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

