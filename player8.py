a1=raw_input().split()
g=" "
for i in range(0,len(a1)):
   a1[i]=a1[i].capitalize()
c=a1[0]
for i in range(1,len(a1)):
   c=c+g+a1[i]
print c
