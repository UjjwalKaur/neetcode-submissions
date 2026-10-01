class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum_of_squares = 0;
        length = len(str(n))

        while sum_of_squares != 1:
            sum_of_squares = 0
            for i in range(length):
                sum_of_squares += (n%10)*(n%10)
                n = n//10
            if sum_of_squares in seen:
                return False
            seen.add(sum_of_squares)
            n = sum_of_squares
            length = len(str(n))
        return True