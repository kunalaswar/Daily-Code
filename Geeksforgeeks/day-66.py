class Solution:
    def countFibonacciNumbers(self, arr):
        
        # Step 1: Find the maximum element in the array
        max_val = max(arr)
        
        # Step 2: Generate all Fibonacci numbers up to max_val
        fib_set = set()
        a, b = 0, 1
        while a <= max_val:
            fib_set.add(a)
            a, b = b, a + b
        
        # Step 3: Count how many elements in arr are Fibonacci numbers
        count = 0
        for num in arr:
            if num in fib_set:
                count += 1
        
        return count
    
s = Solution()
print(s.countFibonacciNumbers ([4, 2, 8, 5, 20, 1, 40, 13, 23]))
print(s.countFibonacciNumbers ([4, 7, 6, 25]))