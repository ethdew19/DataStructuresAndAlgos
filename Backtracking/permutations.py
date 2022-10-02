#Find all permutations of a list
#Solution credit: neetcode 150
def perms(list):
    res = []

    #Base case: 1 element
    if len(list) == 1:
        return [list[:]] #Cheap way to make copy of list

    for _ in range(len(list)):
        temp = list.pop(0)
        permutations = perms(list)
        for perm in permutations:
            perm.append(temp)
        res.extend(permutations)
        list.append(temp)
    
    return res



print(perms([1,2,3,4])) 

# [[4, 3, 2, 1], [3, 4, 2, 1], [2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1], [1, 4, 3, 2], [4, 1, 3, 2], [3, 1, 4, 2],
# [1, 3, 4, 2], [4, 3, 1, 2], [3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 4, 3], [4, 2, 1, 3], [2, 4, 1, 3],
# [1, 4, 2, 3], [4, 1, 2, 3], [3, 2, 1, 4], [2, 3, 1, 4], [1, 3, 2, 4], [3, 1, 2, 4], [2, 1, 3, 4], [1, 2, 3, 4]]