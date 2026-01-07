class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        rev = 0
        if is_negative:
            x = x*-1
        while x > 0:
            last_integer = x % 10
            rev = (rev * 10) + last_integer
            x = x // 10
        if is_negative:
            rev = -rev
        if rev > (2**31) -1 or rev < (-2**31):
            return 0
        return rev

        