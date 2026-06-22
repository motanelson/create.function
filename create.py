print("\033c\033[47;31m\ngive me the .java file name to create ? \n ")
a=input().strip()
b=a.replace(".java","")
print("\ngive me the java function name to create ? \n ")
c=input().strip()
print("\ngive me the java return type to create ? \n ")
f=input().strip()
print("\ngive me the java number of inputs to create ? \n ")
g=input().strip()
print("\ngive me the java function to create ? \n ")
j=input().strip()
e="class "+b+"\n{\n    public static "+f+" "+c+"("
h="a"
i=ord(h)
for z in range(int(g)):
    if z!=0:
        e=e+" , "
    e=e+" "+f+" "+chr(i+z)+" "+" "

e=e+"){\n        return "+j+" ;\n\n    }\n}"
print (e)
