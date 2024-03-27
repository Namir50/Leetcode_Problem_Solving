'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

#First approach
def majority_element(nums):
    candidate = None
    count = 0

    # Finding a candidate for majority element
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        else:
            if num == candidate:
                count += 1
            else:
                count -= 1

    return candidate

#Second Approach
def majority_element(nums):
    return max(nums, key=nums.count)



