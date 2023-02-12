l = [1,4,6,3,8,0]

def Roma(x):
    result_list = []
    for i in x:
        if i % 2 == 0:
            result_list.append(i) 
    return result_list
    
print(Roma([2,4,5,7,9,1,3]))
print(Roma(l))
