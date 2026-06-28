from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 📏 Golden Rule: If the strings aren't the same length, 
        # they can't possibly be perfect structural twins! 
        if len(s) != len(t): 
            return False

        # 🗺️ We need two maps to keep track of our character disguises.
        # s_mapper tracks what character in 's' translates to in 't'.
        # t_mapper makes sure no two characters in 's' try to map to the same character in 't'.
        s_mapper: List[int] = [None] * 256
        t_mapper: List[int] = [None] * 256

        # 🕵️‍♂️ Time to investigate each character pair side-by-side...
        for current_index in range(len(s)):
            
            # ✨ A brand new pair! Neither character has been mapped yet.
            if (
                s_mapper[ord(s[current_index])] is None and 
                t_mapper[ord(t[current_index])] is None
            ):
                # 🤝 Register their exclusive partnership in both directions.
                s_mapper[ord(s[current_index])] = t[current_index]
                t_mapper[ord(t[current_index])] = s[current_index]
                
            # 🚨 BUSTED! We have a disguise violation!
            # This happens if a character in 's' tries to map to a different character than before,
            # OR if a character in 't' is already paired with someone else.
            elif (
                s_mapper[ord(s[current_index])] != t[current_index] or 
                t_mapper[ord(t[current_index])] != s[current_index]
            ):
                return False # ❌ Not isomorphic!
        
        # 🎉 We made it to the end without a single mapping violation!
        # These strings are a perfect 1:1 match.
        return True
    