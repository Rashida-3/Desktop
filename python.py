
a=[3,2,1,5,6]

for i in range(len(a)):
  # print(a[i])
  for j in range(i+1,len(a)):
    if a[i]>a[j]:
      a[i],a[j]=a[j],a[i]
print(a)