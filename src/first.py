def findCommon(l1,l2):
    common = []
    for item in l1:
        if item in l2 and item not in common:
            common.append(item)
    return common


l1 = [1,2,3,4]
l2 = [3,4,5,6]

result = findCommon(l1,l2)
print(result)