print("Enter values and choose operation:\n 1:Addition \n 2:Subtraction \n 3:Multiplication \n 4.Division")
n=int(input( "Enter operation number:"))
a=int(input("Enter first number"))
b=int(input("Enter second number"))
add=a+b
sub= a-b
mul= a*b
div= a/b
if n==1:
    print(add)
elif n==2:
    print(sub)
elif n==3:
    print(mul)
elif n==4:
    print (div)
