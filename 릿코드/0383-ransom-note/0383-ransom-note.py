class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

        # 2
        # st1, st2 = Counter(ransomNote), Counter(magazine) # count each letter 
        # if st1 & st2 == st1: # check intersection
        #     return True
        # return False