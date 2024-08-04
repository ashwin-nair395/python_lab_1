#Slicing Operator
str=("Python is easy")
print(str)
print(str[1:5])
print(str[0])
print(str[ :14])
print(str[0: ])
print(str[-1])
print(str*2)  


#Tuple
Tup1=('a','bc',78,1.23)
Tup2=('d',78)
print(Tup1)
print(Tup2)
print(Tup1[0])
print(Tup2[0:])
print(Tup1+Tup2)
print(Tup1[ :3])
print(Tup1[1:3])

#List
List1=['a','bc',78,1.23]
List2=['d',78]
print(List1*2)
print(List2*2)
print(List1[1])
print(List2[1])
print(List1[0])
print(List1+List2)

#Dictionary
dict={"Vegetable":"Carrot\n""Cucumber\n""Potato","Price":"20\n""30\n""40"}
print(dict['Vegetable'])
print(dict['Price'])
print(dict)

#Type Conversion
x=2.90
print(int(x))
y=3
print(float(y))
print(round(x))

#Program to calculate area of triangle using Herons Formula
a=float(input("Enter 1st side"))
b=float(input("Enter 2nd side"))
c=float(input("Enter 3rd side"))
print("a =",a)
print("b =",b)
print("c =",c)
s= (a+b+c)/2
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print("Area is ",area)

#Program to calculate the distance between 2 points
x1=int(input("Enter First Digit"))
x2=int(input("Enter Second Digit"))
y1=int(input("Enter Third Digit"))
y2=int(input("Enter Fourth Digit"))
print("1st Digit=",x1)
print("2nd Digit=",x2)
print("3rd Digit=",y1)
print("4th Digit=",y2)
distance=(((x2-x1)**2+(y2-y1)**2)*0.5)
print("Distance=",distance)


#Program to calculate the area of circle
r=float(input("Enter Radius"))
Area=(3.14*r*r)
print("Area of the circle is:",Area)


#Program to print the digit at 1's place
x=int(input("Enter a value"))
print("Your Entered Number is:",x)
number=x%10
print("The Number at 1's place is:",number)

#Program to print the ASCII values
x=input("Enter a Char")
print("Char is:",x)
print("The ASCII value of your entered char is:",ord(x))



#Program to find datatype
c=int(input("Enter Your Data:"))
print("Dataype is",type(c))
      

#Sequence
List_A=[1,2,3,4,5,6]
print(List_A)
List_B=['A','B','C','D','E']
print(List_B)
List_C=["Namaste","India"]
print(List_C)
List_D=[1,'a',"sfg"]
print(List_D)
seq=List_A[0::1]
print(seq)
List_A[3]=50
print(List_A)
del List_B[3]
print(List_B)
List_E=List_C
print(List_E)
print(len(List_E))
List_F=(List_A+List_B+List_C+List_D)
print(List_F)


