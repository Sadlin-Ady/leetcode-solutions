def isAnagram(self, s: str, t: str) -> bool:
    l=[]
    for i in s:
        l.append(i)
    for j in t:
        if j in l:
            l.remove(j)
    return len(s)==len(t) and len(l)==0  