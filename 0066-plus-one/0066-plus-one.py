class Solution:
    def plusOne(s, d: list[int]):
        d.insert(0,0)
        l = len(d)
        c = 1
        for i in range(l):
            p = l - i - 1 
            x = d[p] 
            x = x+c
            c = int(x/10)
            x = x%10
            d[p] = x
        if d[0] == 0:
            d.pop(0)
        return d