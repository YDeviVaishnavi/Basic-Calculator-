First = float(input("Enter first number =>  "))
Second = float(input("Enter second number =>  "))
opr = str(input("Enter Operation (+,-,/,*)=>  "))

if opr == "+":
  total = First + Second
elif opr == "-":
  total = First - Second
elif opr == "*":
  total = First * Second
elif opr == "/":
  total = First / Second
else:
  total = str("Please Enter A Valid Operation")

print (total)