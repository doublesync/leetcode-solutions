class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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
            # first two characters of the string may have a 'case'
            potential_case = s[:2]
            if potential_case in cases:
                # remove the characters
                s = s.replace(potential_case, "", 1)
                # add the value of the case to the response
                response += cases[potential_case]
            elif char in numerals:
                # remove the characters
                s = s.replace(char, "", 1)
                # add the value of the char to the response
                response += numerals[char]
        return response
