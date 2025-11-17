def longest_increasing_subsequence(nums):
    subsequence_count = 1
    current = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= current:
            current = nums[i]
            subsequence_count += 1
    return subsequence_count


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(longest_increasing_subsequence(nums))
