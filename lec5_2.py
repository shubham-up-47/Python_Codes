a = "Aman Sir"  
b1 = "Aman"
b2 = a.upper()            # str.upper() returns new str having all letters capital
b3 = a.lower()            # str.lower() returns new str having all letters small 

 
   #Searching str2 in str1
if(a.find(b1)>=0):        # Method 1
	print("Yes")
else:
	print("No")
if(b1 in a):              # Method 2  
	print("Yes")
else:
	print("No")
 

   #Printing string, char by char
for i in range(0,len(a)): # Method 1
	print(a[i])
for b4 in a:              # Method 2  
	print(b4)


   #Printing string, all capital/all small
print(b2)
print(b3)