class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for item in strs:
            key="".join(sorted(item))
            if key not in d:
                d[key]=[]
            d[key].append(item)
        return list(d.values())