def find_pair_with_sum(nums, target):
    seen = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            return f"Pair found ({complement}, {num})"

        seen.add(num)

    return "Pair not found."

# Example input 
nums1 = [5, 2, 6, 8, 1, 9]
target1 = 10
print(find_pair_with_sum(nums1, target1))

nums2 = [1, 2, 3, 4, 5, 6]
target2 = 10
print(find_pair_with_sum(nums2, target2))

nums3 = [8, 5, 3, 9, 2, 5]
target3 = 20
print(find_pair_with_sum(nums3, target3))