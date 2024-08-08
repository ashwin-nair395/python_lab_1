#List
List_A=[1,2,3,4]
print(List_A)
List_B=['A','B','C','D']
print(List_B)
List_C=["Good","Caring"]
print(List_C)
List_D=[1,'G',"ASHWIN"]
print(List_D)

#Accessing the list:
List_A[::2]


#Updating the list
List_A[2]=10
print(List_A)
List_D[1]=('NAIR')
print(List_D)

#Deleting the elements from the list:
print(List_A)
del List_A[0:2]
print(List_A)
del List_B[1]
print(List_B)


#Cloning the list:
print(List_A)
print(List_B)
print(List_C)
print(List_D)
List_E=List_A
print(List_A)


#Basic List Operations:

#len():-returns length of list
print(List_C)
len(List_C)


#Concationation:-Joins 2 lists
print(List_C)
print(List_E)
List_G=List_C+List_E
print(List_G)


#Append():-We can add new elements in list
print(List_B)
print(List_D)
List_B.append('W')
print(List_B)
List_D.append('BTech')
print(List_D)


#clear():- Removes the elements
print(List_C)
List_C.clear()
print(List_C)


#copy():-It returns copy of a list
print(List_A)
List_A.copy()


#count():- Counts the number of occurence of elements in list.
List_R=[1,2,3,3,4,'Ashwin','A','b']
print(List_R)
A=List_R.count('Ashwin')
print(A)
B=List_R.count(3)
print(B)


#extend():- Adds all the elements of an iterable to the list
List_S=[1,2,3,4]
print(List_S)
List_S.extend([5,6])
print(List_S)


#index():- Returns the position of first occurence of the value x
List_J=[1,'a','Ashwin',3]
print(List_J)
print(List_J.index('Ashwin'))


#insert():- Insert element at x position index
List_U=[5,6,7,8,9,0]
List_U.insert(0,4)
print(List_U)


#pop():- Removes & Returns the last element
List_O=[1,2,3]
print(List_O)
List_O.pop()
print(List_O)


#remove():- removes and returns the first occurence of the element 
List_I=[1,2,3,3,4]
print(List_I)
List_I.remove(3)
print(List_I)


#reverse():- reverse the order and element in the list
List_Y=[1,2,3,4,5,6,7,8]
print(List_Y)
List_Y.reverse()
print(List_Y)


#sort():- Sort the element in ascending order
List_K=[100,99,98,97,96,95]
print(List_K)
List_K.sort()
print(List_K)