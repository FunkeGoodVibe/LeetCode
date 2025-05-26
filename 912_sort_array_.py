'''
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 104 <= nums[i] <= 5 * 10^4
'''

class Solution:
        
    def mergeSort(nums):

        if len(nums) < 2:
            return nums

        result = []          # moved!
        mid = int(len(nums) / 2)
        y = Solution.mergeSort(nums[:mid])
        z = Solution.mergeSort(nums[mid:])
        while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        result += y
        result += z
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        #Bubble Sort
        # for i in range(len(nums)):
        #     for j in range(0, len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = temp
        # return nums

        return Solution.mergeSort(nums)