#Selection Sort
#Time Complexity: O(n^2), goes over entire list in each iteration of the initial loop through the list. Not a very good algorithm
#Space Complexity: O(1), only stores in pointers, in place algorithm
#Notes: Highlights a slow sorting algorithm. Not very important.
def selectionSort(list):
    length = len(list)
    for step in range(length):
        minIndex = step

        for i in range(step + 1, length):
            if list[i] < list[minIndex]:
                minIndex = i
        (list[step], list[minIndex]) = (list[minIndex], list[step])
