a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c=input("Enter operation: ")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b3
        ):
    return a*b
def div(a,b):
    return a/b
if(c=='+'):
  print(add(a,b))
  
elif(c=='-'):
  print(sub(a,b))
elif(c=='*'):
  print(mul(a,b))
elif(c=='/'):
  print(div(a,b))
else:
  print("invalid")
