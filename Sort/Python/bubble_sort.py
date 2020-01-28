#Bubble sort, time complexity O(N^2)
from randomGen import randomArray
from randomGen import numberToSeach
import math

def bubble_sort(length):
    for i in range(length):
        for j in range(0, length-i-1):
            if arrToSearch[j] > arrToSearch[j + 1]:
                temp = arrToSearch[j]
                arrToSearch[j] = arrToSearch[j + 1]
                arrToSearch[j + 1] = temp


arrToSearch = randomArray()
bubble_sort(len(arrToSearch))

print(arrToSearch)