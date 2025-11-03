a= float(input("enter the first number :"))
b= float(input("enter the 2nd number :"))
c= float(input("enter the 3rd number :"))
if a>=b and a>=c:
    biggest =a
elif b>=a and b>=c:
    biggest =b
else:
    biggest =c
    print("biggest number is :",biggest)