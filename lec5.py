   #String
a = "Hi Hi Hi Harman Sir"  
                   # 0 1 2 .... 16 17 18 [Index (0 to 18) of each char] 
print(a[1])        # Accessing char of string   
print(a[4])         

 
   #String slicing 
b1 = a[:5]         # char string from a, index (start to 4) 
print(b1)
b2 = a[1:5]        # char string from a, index (1 to 4) 
print(b2)
b3 = a[3:]         # char string from a, index (3 to end) 
print(b3)


   #String functions
print(len(a))      # len(str) returns length of string
c1 = "Hi"
print(a.count(c1)) # str1.count(str2) returns no of occurance of str2 in str1
c2 = "Harman"
print(a.find(c2))  # str1.find(str2) returns start index of str2, present in str1 
x = a.find(c2)
print(a[x:])       # prints part of string in a, starting from c2
c3 = "Aman"
print(a.find(c3))  # str1.find(str2) returns -1 if str2 is not present in str1
c4 = a.replace(" ","=")
print(c4)          # str.replace(str1,str2) returns new str, in which all str1 replaced with str2 
