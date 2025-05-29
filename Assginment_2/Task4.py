def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    # Calculate width of the rangoli line
    width = 4 * size - 3

    # Generate the lines of the rangoli
    lines = []
    for i in range(size):
        # Left part: letters from the current letter down to 'a'
        left = alpha[size-1:size-1-i:-1]
        # Middle part: the letter at the center for this line
        middle = alpha[size-1-i]
        # Right part: letters from 'a' back up to current letter, excluding the middle letter
        right = alpha[size-i:size]

        # Combine left + middle + right with hyphens
        row = '-'.join(left + middle + right)
        # Center align the row string to the required width
        lines.append(row.center(width, '-'))

    # Print the top half and middle of the rangoli
    top = lines[::-1]  
    # Bottom half is all lines except the middle line (since it's already printed)
    bottom = lines[1:]  

    # Join the rangoli lines with newline characters
    return '\n'.join(top + bottom)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)