class Solution(object):
    def romanToInt(self, s):
        response = 0
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        while s:
            char = s[0]
            potential_case = s[:2]
            if potential_case in cases:
                s = s.replace(potential_case, "", 1)
                response += cases[potential_case]
            elif char in numerals:
                s = s.replace(char, "", 1)
                response += numerals[char]
        return response
