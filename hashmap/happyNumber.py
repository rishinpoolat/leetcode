"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1"""

METHOD
"to solve this we know what is the happy number which is sum the square of digits must be 1 
and if one number it not a happy number it has a cycle it is repeated his steps"

APPROACH
- firsly we get all of the digits and we get square of them after sum all of them
- subsequently we check this sum equal to 1 or a number that we before calculated is in the hashmap
- if that so we return False otherwise we continue to process if number can reach to 1 we return True

CODE:

class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = {}
        number = 0
        while True:
            for i in str(n):
                number += int(i)**2
            if number == 1:
                return True    
            if number in numbers:
                return False
            numbers[number] = 0
            n= number 
            number = 0       


COMPLEXITY
Time complexity: O(logn)
Space complexity:O(logn)

