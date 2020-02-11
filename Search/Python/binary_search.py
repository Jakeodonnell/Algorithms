'''
Binary seach of ints. Timecomplexity O(log n)

Compare x with the middle element.
If x matches with middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
Else (x is smaller) recur for the left half.
'''
from randomGen import randomArray
from randomGen import numberToSeach

def binarySeach(arrToSearch, leftMostElement, length, searchedValue):
    if length >= leftMostElement:

        mid = leftMostElement + (length - leftMostElement) // 2

        if arrToSearch[mid] == searchedValue:
            return mid
        
        elif arrToSearch[mid] > searchedValue:
            return binarySeach(arrToSearch, leftMostElement, mid - 1, searchedValue)

        elif arrToSearch[mid] < searchedValue:
            return binarySeach(arrToSearch, mid + 1, length, searchedValue)

    else:
        return -1



arrToSearch = randomArray()
arrToSearch.sort()
print(arrToSearch)
searchedValue = numberToSeach()

#search from index 0, therefor "-1"
leftMostElement = 0
length = len(arrToSearch) - 1
indexArray = []
find = binarySeach(arrToSearch, leftMostElement, length, searchedValue)
indexArray.append(find)
if find != -1:
    next = find + 1
    while arrToSearch[next] == arrToSearch[find]:
        indexArray.append(next)
        next = next + 1

    next = find - 1
    while arrToSearch[next] == arrToSearch[find]:
        indexArray.append(next)
        next = next - 1
    indexArray.sort()
    print("Integer/s exists at: " + str(indexArray))
else:
    print("Integer does not exist")