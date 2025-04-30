
class Solution:
    # O(n)
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return sum( map(s1, s2) ) < 3 * (sorted(s1)==sorted(s2))