import numpy as np


def read_input(file):
    with open(file) as f: 
        data = f.read().splitlines()
    return data

def traverse(data, step_size):
    bot_row = len(data)
    col_length = len(data[0])
    row, col = 0, 0
    tree_count = 0
    
    row_step_size, col_step_size = step_size
    
    while row < bot_row: 
        # Check if hit tree
        if row < bot_row and data[row][col % col_length] == '#': 
            tree_count += 1

        # Traverse down 
        row += row_step_size
        col += col_step_size

    if step_size == (1, 3):
        print(f"Result part 1: {tree_count}")
    return tree_count



if __name__ == "__main__":
    file = 'input/day03.txt'
    data = read_input(file)
    data = np.array(data)

    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    result = 1
    for slope in slopes: 
        result *= traverse(data, slope)

    print(f"Result part 2: {result}")

