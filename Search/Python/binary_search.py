'''
Binary seach of ints. Timecomplexity O(log n)

Compare x with the middle element.
If x matches with middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
Else (x is smaller) recur for the left half.
'''
from randomGen import randomArray
from randomGen import numberToSeach
import sys

def binarySeach(arrToSearch, leftMostElement, length, searchedValue):
    if length >= leftMostElement:
        mid = int(leftMostElement + (length - leftMostElement) / 2)

        if mid == sys.maxsize:
            mid += 1

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
if find != -1:
     print("Integer exists at: " + str(find))
else:
     print("Integer does not exist")

#---------------------------------------------------Searcing for multiple elements...Not working...YET!---------------------------------------------------
'''
indexArray.append(find)
arrToSearch[find] = sys.maxsize
while find != -1:
    find = (binarySeach(arrToSearch, leftMostElement, length, searchedValue))
    indexArray.append(find)
    arrToSearch[find] = sys.maxsize
    print(indexArray)
    print(arrToSearch)
print(indexArray)

if len(indexArray) > 1:
    for i in range(len(indexArray) - 1):
        print("Integer exists at: " + indexArray[i])

elif indexArray == -1:
    print("Integer does not exist")


'''
