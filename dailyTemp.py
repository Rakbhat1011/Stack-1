"""
Use a monotonic stack to store indices of decreasing temperatures
For each day i, pop from the stack until you find a warmer day — calculate the difference
Push the current day i onto the stack for future comparisons
"""
"""
Time Complexity: O(n) - One pass
Space Complexity: O(n) - Monotonic Stack
"""

class dailyTemp:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] 

        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)

        return answer

if __name__ == "__main__":
    obj = dailyTemp()
    print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(obj.dailyTemperatures([30, 40, 50, 60])) 
    print(obj.dailyTemperatures([30, 60, 90])) 
