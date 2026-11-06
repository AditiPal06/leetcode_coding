#two sum
# 4 6 7 8 3; 10 [4,6], [7,3] or [0,1] [2,4]
# 0,4 ; 1, 6

#seen = will hold numbers and its positions
def two_sum(nums, target):
    seen = {}
    ans = []
    for i,j in enumerate(nums):
        if target - j in seen:
            ans.append([i,seen[target-j]])
        seen[j] = i
    return ans

print(two_sum([4, 6, 7, 8, 3], 10))

# Find max sum of k consecutive elements, find all anagrams in a string.

def max_sum(nums,k):
    if len(nums)<k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    left = 0
    for right in range(k, len(nums)):
        window_sum = window_sum - nums[left] + nums[right]
        max_sum = max(max_sum,window_sum)
        left = left + 1
    return max_sum

print(max_sum([2, 1, 5, 1, 3, 2],3))


# The Length Longest Substring Without Repeating Characters
# def length_of_longest_substring(s: str) -> int:
# print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left = left + 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring("pwwkew"))  # Output: 3 ("wke")
print(length_of_longest_substring("abcabcbb"))  # Output: 3





