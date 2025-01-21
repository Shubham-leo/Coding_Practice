def groupAnagrams(strs) :
    #M.NlogN times
    # nl2=[]
    # for i in strs:
    #     nl=[]
    #     for j in strs:
    #         if "".join(sorted(i)) == "".join(sorted(j)):
    #             nl.append(j)
    #     if nl not in nl2:
    #         nl2.append(nl)
    # return nl2
    from collections import defaultdict
    d = defaultdict(list)
    for word in strs:
        key ="".join(sorted(word))
        d[key].append(word)
    print(d)
    return d.values()




strs =["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))