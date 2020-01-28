from randomGen import randomArray
from randomGen import numberToSeach
import math

def insertion_sort(length):
    for i in range(1,length):
        key = arrToSearch[i]
        j = i - 1
        while j >= 0 and arrToSearch[j] > key:
            arrToSearch[j + 1] = arrToSearch[j]
            j = j - 1
        arrToSearch[j + 1] = key

arrToSearch = randomArray()
insertion_sort(len(arrToSearch))

print(arrToSearch)