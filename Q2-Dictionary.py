d={'Name:':'Rittika','Stream:':'CSE'}
print(type(d))
print(d)
D=d.copy()
print(D)
D.popitem()
print(D)
print(d.fromkeys("Name:","ABC"))
D.clear()
print(D)
a,b,c=input("Enter data").split('/')
print(a,b,c)
str1=input("Enter data")
str2=str1.replace('/','.')
print(str2)
