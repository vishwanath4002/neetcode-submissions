class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            c = [0] * 26
            for j in i:
                c[ord(j)-97] += 1
            d[tuple(c)].append(i)
        
        return list(d.values())