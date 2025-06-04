x=[1,2,3,4,'shri',4,3,'shri',5,6]

#how to remove duplicates
y=set(x)
print(y)

#without using set datatype to maintain data in ordered format.
z=list(dict.fromkeys(x).keys())
print(z)
