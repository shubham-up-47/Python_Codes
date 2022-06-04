    #List [Array]
l = [1,5,2,20,9]
l1 = [21,100]
l2 = l*3
l3 = []             # Empty list
print(l)
print(l[2])
print(l2)
    
    #List slicing
l4 = l[1:3]
print(l4)


    #List functions
l.insert(2,7)       # l.insert(i,x) inserts x at index i by shifting others 
print(l)
l.append(11)        # l.append(x) adds x at end of list l
print(l)
l.extend(l1)        # l.extend(l1) adds l1 at end of list l
print(l)
l.sort()            # l.sort() sorts list l
print(l)
l.pop(3)            # l.pop(i)  deletes element at index i
print(l)
print(l.count(20))  # l.count(x) returns no of occurance of x in list
print(len(l))       # len(l) returns length of list
print(sum(l))       # sum(l) returns sum of list elements

