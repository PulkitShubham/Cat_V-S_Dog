print("........................................Mini Project........................................")
print("In this project user will enter single or multiple numbers and our system will ")
print("predict the entered number or number's is/are valid number(s) in a Fibonacci Series or not:")
l1=list(map(int,input("Enter Number(s): ").split(",")))
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
x=max(l2)
l3=[]
a=0
b=1
i=0
c=0
while c<=x:
    l3.append(c)  # List of Fibonacci series
    a=b
    b=c
    c=a+b
    i=i+1
#  To get output on new lines
for i in l2:
    if i in l3:
        print(i,"is valid")
    else:
        print(i,"is invalid")

# To get output in same line:
#l4=[]
#for i in l2:
#     if i in l3:
#         p=[i,"is valid"]
#     else:
#         p=[i,"is invalid"]
#     l4.append(p)
# for i in range(len(l4)):
#     for j in range(2):
#         l4[i][j]=str(l4[i][j])
#         print(l4[i][j],end=" ")
