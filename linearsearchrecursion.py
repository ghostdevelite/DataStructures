

def linearrecur(container,num,index=0):

#create a base case so that you wont get stack error


    if index >= len(container):

        return 1

    if container[index] == num:

        return index
    #to make it a recursion makesure that you call the function to iterate the search
    return linearrecur(container,num,index+1)

num = [1,22,44,66,111,33]
print(linearrecur(num,111))
