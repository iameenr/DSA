class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        #the Sieve of Eratosthenes
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        psqr = p*p
        while psqr < n:
            if is_prime[p]:
                for multiple in range(psqr, n, p):
                    is_prime[multiple] = False
            p += 1
            psqr = p*p

        return sum(is_prime)


        # if n <= 2: return 0

        # get_sqrt = lambda x: int(x**0.5)
        # def is_prime(num):
        #     for odd in range(3, get_sqrt(num)+1, 2):
        #         if num % odd == 0:
        #             return False
        #     return True

        # prime_count = 1
        # for num in range(3, n, 2):
        #     if is_prime(num):
        #         prime_count += 1
        #         # print(num, prime_count)
        # return prime_count


