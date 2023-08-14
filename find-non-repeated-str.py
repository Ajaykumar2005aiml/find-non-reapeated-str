s=input()
m=[]
for i in range(len(s)):
  m.append(s[i])
k=[]
for i in range(len(m)):
  if m.count(m[i])==1:
    k.append(m[i])
for i in range(len(k)):
  print(k[i],end='')
