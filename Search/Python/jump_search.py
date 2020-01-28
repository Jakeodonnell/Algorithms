#Jump seach of ints. Timecomplexity O(sqrt(N)), used to get a bit faster searching than linear
from randomGen import randomArray
from randomGen import numberToSeach
import math

def jump_search(arrToSearch, length, searchedValue):
    jump_length = int(math.sqrt(length))
    location = 0
    while(location + jump_length <= length and arrToSearch[location] < searchedValue):
        location += (location + jump_length)

    for i in range(location, (location - jump_length), -1):
        if arrToSearch[i] == searchedValue:
            return i
    return -1

arrToSearch = randomArray()
arrToSearch.sort()
print(arrToSearch)

searchedValue = numberToSeach()
index = jump_search(arrToSearch, len(arrToSearch), searchedValue)

if index != -1:
    print("found at index: " + str(index))
if index == -1:
    print("not found")