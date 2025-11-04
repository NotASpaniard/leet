def firstMissingPositive(nums):
    n = len(nums)
    i = 0
    while i < n:
        if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            correct_pos = nums[i] - 1
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1

test_cases = [
    [3, 5, 12, 4, 2],    # → 1
    [8, 4, 2, 1],        # → 3  
    [1, 2, 3, 4, 5, 6],  # → 7
    [-1, -2, 0],         # → 1
    [1, 1, 2, 4],        # → 3
    [7, 8, 9, 11]        # → 1
]

print("KẾT QUẢ:")
for i, test in enumerate(test_cases):
    test_copy = test.copy()
    result = firstMissingPositive(test_copy)
    print(f"Test {i+1}: {test} → {result}")