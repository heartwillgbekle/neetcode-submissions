class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # move left pointer to next alphanumeric
            while l < r and not s[l].isalnum():
                l += 1

            # move right pointer to previous alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1

            # compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

            


        