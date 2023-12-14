def find_duplicates_with_index(input_list):
    index_positions = {}

    for index, value in enumerate(input_list):
        if value in index_positions:
            index_positions[value].append(index)
        else:
            index_positions[value] = [index]

    # Filter out non-duplicates
    duplicates = {value: positions for value, positions in index_positions.items() if len(positions) > 1}

    return duplicates


# Example Usage
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 6, 7, 8, 8, 9]
result = find_duplicates_with_index(my_list)

print("List:", my_list)
print("Duplicate Items with Index Positions:", result)
