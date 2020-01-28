#Linear seach of ints. Timecomplexity O(N)
from randomGen import randomArray
from randomGen import numberToSeach

found = False
arrToSearch = randomArray()
searchedValue = numberToSeach()

#linear seach
for i in range(len(arrToSearch)):
    if(arrToSearch[i] == searchedValue):
        found = True
        print("found at index " + str(i) + "...Printing integer at index " + str(i) + " : "+ str(arrToSearch[i]))

if(found == False):
    print("Number does no exist")