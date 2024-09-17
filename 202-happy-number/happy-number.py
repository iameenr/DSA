class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow = get_next(n)
        fast = get_next(get_next(n))
        
        while slow != fast:
            # print(slow, fast)
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return slow == 1
