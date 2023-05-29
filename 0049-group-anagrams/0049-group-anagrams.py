class Solution:
    def groupAnagrams(self, strs):
        strs2 = []
        x = -1
        s = len(strs)
        for i in range(s):
            strs2.append(''.join(sorted(strs[i])))
        strsset = set(strs2)
        ss = len(strsset)
        lists = [[] for j in range(ss)]
        strs3 = list(strsset)
        for i in range(s):
            for j in range(ss):
                if strs2[i] == strs3[j]:
                    lists[j].append(strs[i])
        return lists
        