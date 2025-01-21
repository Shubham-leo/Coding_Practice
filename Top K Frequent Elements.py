"""minheap that's kept at size k, 
if its bigger than k pop the min, 
by the end it should be left with 
k largest"""

def topKFrequent(nums, k) :
    from collections import defaultdict
    count = defaultdict(list)
    # create skeleton for the dict
    freq = [[]for i in range(len(nums)+1)]

    for n in nums:
        # travers dict and get count of each element(0 is for default case)
        count[n]=1+count.get(n,0)
    for n,c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res

nums = [1,1,1,2,2,3] 
k = 2
print(topKFrequent(nums,k))