class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}

        for word in strs:
            box= "".join(sorted(word))
            if box not in seen:
                seen[box] =[]
            seen[box].append(word)
        return list(seen.values())     

