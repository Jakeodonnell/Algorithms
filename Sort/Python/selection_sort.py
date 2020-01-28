#Selectionsort time complexity is O(N^2)
from randomGen import randomArray
from randomGen import numberToSeach
import math

def selection_sort(length):
    for i in range(length):

        #search for a smaller element in the array.
        min_index = i
        for j in range(i+1, length):
            if arrToSearch[min_index] > arrToSearch[j]:
                min_index = j
                
        temp = arrToSearch[min_index]
        arrToSearch[min_index] = arrToSearch[i]
        arrToSearch[i] = temp 


arrToSearch = randomArray()
selection_sort(len(arrToSearch))

print(arrToSearch)