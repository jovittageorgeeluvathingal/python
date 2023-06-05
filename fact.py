x=[4,5,6]
y=[]
for j in x:
  fact=1
  for i in range(1,j+1):
      fact=fact*i
  y.append(fact)
  print(y)
