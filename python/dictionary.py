"""x={"name":"vvera","course":"mca","clg name":"mits","fee":60000}
print(x.keys())
print(x.values())
print(x.copy())
x["company"]="cisco"
z={"software":"engineer","profession":"developer"}
x.update(z)
x.pop("course")
x["compamy"]="cisco"
x.popitem()
print(x.items())
x.clear()"""
#set
x={1,2,3,4,5,6,6}
y={1,2,5,6,6,78,8,9,8,9}
print(x)
x.add(7)
print(x)
x.remove(6)
print("union",x|y)


