Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

 
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105


METHOD:
- using hashmap to store indices of number
- for loop through array of numbers
- check if hashmap has the number
- if it has check if the difference of current index and saved index is less than k if yes return true
- else change hashmap[number] = i
- return false at end of loop

CODE:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        for i in range(len(nums)):
            if nums[i] in num_index:
                if abs(num_index[nums[i]] - i) <= k:
                    return True  
            num_index[nums[i]] = i       
        return False            

COMPLEXITY:
Time complexity: O(n)
Space complexity: O(k)
