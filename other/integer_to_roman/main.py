class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        thousands = num // 1000
        ans += thousands * "M"
        num %= 1000
        if num >= 900:
            ans += "CM"
            num -= 900
        if num >= 500:
            ans += "D"
            num -= 500
        if num >= 400:
            ans += "CD"
            num -= 400
        hundreds = num // 100
        ans += hundreds * "C"
        num %= 100
        if num >= 90:
            ans += "XC"
            num -= 90
        if num >= 50:
            ans += "L"
            num -= 50
        if num >= 40:
            ans += "XL"
            num -= 40
        tenth = num // 10
        ans += tenth * "X"
        num %= 10
        if num == 9:
            ans += "IX"
            return ans
        if num >= 5:
            ans += "V"
            num -= 5
        if num == 4:
            ans += "IV"
            return ans
        return ans + num * "I"