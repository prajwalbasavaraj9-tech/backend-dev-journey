def longest_consecutive_sequence(arr):
    if not arr:
        return 0

    # Step 1: Convert list to set for O(1) average lookup time
    num_set = set(arr)
    longest_streak = 0

    # Step 2: Iterate through the set
    for num in num_set:
        # Step 3: Check if 'num' is the START of a sequence
        # If num - 1 exists, then 'num' is in the middle of a sequence, so skip it
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            # Step 4: Expand the sequence forward
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example
arr = [1, 99, 101, 98, 2, 5, 3, 1, 100]
print(f"Longest streak length: {longest_consecutive_sequence(arr)}")

