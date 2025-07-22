"""
Use a monotonic decreasing stack to track indices whose next greater element is not yet found
Loop through the array twice (2 * n) to simulate circular behavior
When nums[i] > nums[stack[-1]], update the result for that index and pop the stack
"""
"""
Time Complexity: O(n) - One pass - Each element is pushed and popped at most once
Space Complexity: O(n) - Monotonic Stack
"""

class nextGreaterElement:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr
            if i < n:
                stack.append(i)
        return res

if __name__ == "__main__":
    obj = nextGreaterElement()
    print(obj.nextGreaterElements([1, 2, 1]))        
    print(obj.nextGreaterElements([1, 2, 3, 4, 3]))   
    print(obj.nextGreaterElements([5, 4, 3, 2, 1])) 
