def longest_consecutive_ones(n):
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Split the binary string on '0' and get the lengths of the segments
    ones_segments = binary_representation.split('0')
    
    # Find the maximum length of the segments of '1's
    longest_streak = max(len(segment) for segment in ones_segments)
    
    return longest_streak

# Example usage
number = 29  # Binary representation is '11101'
print(f"The longest consecutive 1's in the binary representation of {number} is: {longest_consecutive_ones(number)}")
