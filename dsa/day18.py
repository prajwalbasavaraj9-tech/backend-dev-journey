# - Longest consecutive sequence (leet code 128).

def longest_consecutive_sequence(arr):
    
    maximum_length_sequence = 0
    longest_sequence = []
    
    for num in arr:
        current_sequence = [num]
        
        while num + 1 in arr:
            num = num + 1
            current_sequence.append(num)
            
        print(f"found Sequences - {current_sequence}")
        
        if len(current_sequence) > maximum_length_sequence:
            maximum_length_sequence = len(current_sequence)
            longest_sequence = current_sequence
            
    print('-' * 25)
    print(f"longest sequence in array-{longest_sequence}")
    return maximum_length_sequence

arr = [1, 99, 101, 98, 2, 5, 3, 1, 100]
print(longest_consecutive_sequence(arr))