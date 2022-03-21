def productarray(arr,index):
    if index == len(arr)-1:
        return arr[index]
    else:
        return arr[index]* productarray(arr,index+1)


arr=[1,2,3,4,5]
print(productarray(arr,0))