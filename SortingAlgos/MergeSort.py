#Merge Sort
#Time Complexity: O(nlogn), You go through the entire list (n), logn times. 
#Space Complexity: O(n), the function will only ever have n recursive functions stored in space
#Notes: A very important sorting algorithm, worth learning since it's hard to come up with on the fly. Also highlights the nlogn limit for sorting algorithms. 
#If a sorting algorithm uses comparisons ("<" or ">"), its worst case cannot mathematically be better than O(nlogn).
def mergeSort(list):
    listLength = len(list)
    if listLength == 1:
        return list
    midpoint = listLength //2
    left = list[:midpoint]
    right = list[midpoint:]
    return merge(mergeSort(left),mergeSort(right))
def merge(left,right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j +=1
    output += left[i:]
    output += right[j:]
    return output


    

            

