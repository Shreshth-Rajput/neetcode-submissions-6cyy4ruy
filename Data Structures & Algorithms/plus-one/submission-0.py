class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        k = 1
        carry = 0
        i = 0
        while k or carry:
            if i >= len(digits):
                digits.append(0)
            new_digit = (digits[i] + k + carry)
            k = 0
            carry = new_digit // 10
            digits[i] = new_digit % 10
            i += 1
        
        digits.reverse()
        return digits

