a = int(input("How many size of the number?"))
list=[]
for i in range (a):
    b = int(input("Enter the number: "))
    list.append(b)
print(list)
c = int(input("Enter the element that you want to search:"))
for x in range(a):
    if list[x]==c:
        print("The element in a position",x+1)
    