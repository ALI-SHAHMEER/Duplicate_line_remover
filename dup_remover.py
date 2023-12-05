def remove_duplicate_lines(filename):
    # Read the file contents into a list of lines
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Create a set to store unique lines
    unique_lines = set()

    # Filter out duplicate lines
    filtered_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.add(line)
            filtered_lines.append(line)

    # Write the filtered lines to a new file
    with open('output.txt', 'w') as f:
        f.writelines(filtered_lines)

# Example usage
filename = "pak_link.txt"
remove_duplicate_lines(filename)