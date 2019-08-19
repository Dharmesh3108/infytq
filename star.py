list1=[]
list2=[]
list3=[]
n=int(input())
for i in range(1,n+1):
  if(i%2!=0):
    list1.append(i)
    if(n%2==0):
      l=len(list1)-1
    else:
      l=len(list1)-2  
for j in range(l,-1,-1):
  list2.append(list1[j])
list3=list1+list2  
print(list3)
b=len(list3)
for k in range(0,b):
  l=(n-list3[k])//2
  a=list3[k]
  while(l!=0):
    print(" ",end="")
    l=l-1
  while(a!=0):
    print("*",end="")
    a=a-1
  print()  
