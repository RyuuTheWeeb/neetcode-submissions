class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=[]
        n=[[] for _ in range(len(strs))]
        for i in range(len(strs)):
            s.append(["".join(sorted(strs[i]))])
        i=0
        while i<len(strs):
            j=i+1
            n[i].append(strs[i])
            while j<len(strs):
                if s[i]==s[j]:
                    n[i].append(strs[j])
                    if i!=j:
                        s.pop(j)
                        strs.pop(j)
                    continue
                j+=1
            i+=1
        return [x for x in n if x != []]