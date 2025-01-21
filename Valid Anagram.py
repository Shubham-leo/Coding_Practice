def isAnagram(self, s: str, t: str) -> bool:
    sstr = "".join(sorted(s))
    tstr = "".join(sorted(t))

    return sstr == tstr