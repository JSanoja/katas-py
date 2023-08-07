def tidyNumber(n):
    arr = list(str(n))
    index=0
    for i in arr:
        print(index, int(i), int(arr[index]))
        if  (int(i) < int(arr[index-1])) and index != 0:
            return True
        index+= 1
    return False
    
print(tidyNumber(12))
print(tidyNumber(21))
