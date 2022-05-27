
from random import randint
# Interpolation Search
# search in sorted array

def interploationSearch(arr:list,low , high , x):
    """
    get list of elements and search for x in it.
    """
    # check for end condition
    if (low <= high and x >= arr[low] and x <= arr[high]):

        # this algorithm is based on binary search
        # mid = low + (high - low) // 2 
        # 
        # but we find the next index to search base on interplotaion algorithm 
        position = low + ((high - low) // (arr[high] - arr[low]) *
                    (x - arr[low]))

        if x == arr[position]:
            return position

        if x < arr[position]:
            return interploationSearch(arr=arr,low=low,high=position-1,x=x)
        
        if x > arr[position]:
            return interploationSearch(arr=arr,low = position+1,high=high,x=x)

        return -1


# test
arr1 = [randint(0,1000000) for i in range(100000000)]
arr1.sort()

x = arr1[46]

interploationSearch(arr1,0,len(arr1)-1,x)