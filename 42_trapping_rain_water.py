"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water
    
"""
Line by line:

from typing import List
Imports List so we can annotate height as a list of integers.

class Solution:
Defines the class expected by LeetCode-style problems.

def trap(self, height: List[int]) -> int:
Defines the function. It takes height, a list of bar heights, and returns an integer amount of trapped water.

left, right = 0, len(height) - 1
Creates two pointers: left starts at the first bar, right starts at the last bar.

left_max = right_max = 0
Tracks the tallest bar seen so far from the left side and from the right side.

water = 0
Initializes the answer.

while left < right:
Keeps processing while there are bars between the two pointers.

if height[left] < height[right]:
If the left bar is shorter, the trapped water on the left side depends on left_max.

left_max = max(left_max, height[left])
Updates the tallest bar seen from the left.

water += left_max - height[left]
Adds water trapped above the current left bar. If the bar is as tall as left_max, this adds 0.

left += 1
Moves the left pointer inward.

else:
Handles the case where the right bar is shorter or equal.

right_max = max(right_max, height[right])
Updates the tallest bar seen from the right.

water += right_max - height[right]
Adds water trapped above the current right bar.

right -= 1
Moves the right pointer inward.

return water
Returns the final total.

""" 


# Why it works: water above a bar is limited by the shorter of the tallest wall to its left and right. 
# With two pointers, whichever side has the shorter current height can be resolved immediately because 
# the opposite side already has a boundary tall enough.

# Complexity: O(n) time, O(1) extra space.