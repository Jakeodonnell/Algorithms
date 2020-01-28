from random import randint
def randomArray():
    found = False
    arrToSearch = []
    #100 random integers between 0 and 100 
    for _ in range(100):
        arrToSearch.append(randint(0,100))
        
    print(arrToSearch)
    return arrToSearch

def numberToSeach():
    searchedValue = int(input('Enter integer to search for in range 0 - 100: '))

    while searchedValue < 0 or searchedValue > 100:
        searchedValue = int(input('Enter integer to search for in range 0 - 100:'))

    return searchedValue