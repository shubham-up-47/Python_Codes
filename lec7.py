  # Dictionary (d) [ 'Key':Value pairs are stored here ] [ Has no indexing i.e. unordered data]
d1 = {'Harman':90,'Babbar':100,'Rahul':80,'Ajay':95}    # storing student's name & marks 
print(d1)
k1 = d1.keys()          # storing keys list of dictionary d
print(k1)
v1 = d1.values()        # storing values list of dictionary d
print(v1)


  # Updating-Adding-Deleting 'Key':Value pairs
d1['Harman'] = 100     # Updating
print(d1)
d1['Aman'] = 85        # Adding
print(d1)
del d1['Harman']       # Deleting
print(d1)


m1 = d1['Babbar']      # Printing marks of Babbar
print(m1)

if('Harman' in d1):    # Searching a Key
	print("Yes")
else:
	print("No")

print(len(d1))         # Printing length of a dictionary

for i in d1:
	print(i,d1[i])     # i=key & d[i]=value, then Key Value pair will be printed  






