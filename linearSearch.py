

def linear(container, item):
        
    #the running time of this algorithm is O(N)
    #use linear search if the data structure is unordered

    for index in range(len(container)):
        if container[index] == item:
        #if we find the item : we return the index of that item
            return index

#if the search miss when the item is not present in the underlying datastruc(container)

    return "no result"



num = [1,2,3,4,5,6,7,8,9,10]

print(linear(num, 10))
