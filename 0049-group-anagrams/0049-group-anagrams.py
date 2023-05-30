class Solution:
    def groupAnagrams(self, strs):
        strs2 = []
        for i in range(len(strs)):
            strs2.append(''.join(sorted(strs[i])))
        strs3 = list(set(strs2))
        lists = [[] for i in range(len(strs3))]
        for i in range(len(strs)):
            for j in range(len(strs3)):
                if strs2[i] == strs3[j]:
                    lists[j].append(strs[i])
        return lists
        