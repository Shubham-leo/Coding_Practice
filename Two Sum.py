def twoSum(nums , target) :
    varMap ={}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in varMap:
            return [varMap[diff],i]
        varMap[n] = i
    return