#exercise
print(3+5)
print("3"+"5")
print(int("3")+5)

def printState():
    print ("Red Light on? " + str(redLight))
    print ("Yellow Light on? " + str(yellowLight))
    print ("Green Light on? " + str(greenLight))

redLight = True
yellowLight = False
greenLight = False

printState()

print (type(redLight))

x=10
y=20.0
z=1j
print(type(x))
print(type(y))
print(type(z))

x = int(1)
y = int(2.8)
z = int("3")

print(type(x))
print(type(y))
print(type(z))

day = "Beautiful"
print (day[1])

day = "Beautiful"
print (day[0:5])

print (day[-3])
print (day[-3:])
print (day[-5:3])
print (day[-5:-3])

day = "Beautiful"
print(str(day == "Beautiful") + ": Today is " + day)

#27
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
print (str(num1) + " + " + str(num2) + " = " + str(num1+num2))
print (str(num1) + " * " + str(num2) + " = " + str(num1*num2))
print (str(num1) + " / " + str(num2) + " = " + str(num1/num2))
print (str(num1) + " Modulo " + str(num2) + " = " + str(num1%num2))
print (str(num1) + " exponent " + str(num2) + " = " + str(num1**num2))

#28 a
temp = int(input("Please enter the temperature in degrees Celsius "))
Fah = int(temp*9/5 + 32)
print ("Fahrenheit" + ": " + str(Fah))

#b
rad = float(input("Please enter the radius of the circle"))
import math
pi = math.pi
cir = 2*pi*rad
area = pi*rad*rad
print ("Area: " + str(area))
print ("Circumference: " + str(cir))

#c
rad = float(input("Please enter the radius of the sphere"))
import math
pi = math.pi
area = 4*pi*rad*rad
print("Area: " + str(area))

#d
h = float(input("Please enter the height of the cylinder: "))
r = float(input("Please enter the radius of the cylinder: "))
import math
pi = math.pi
cir = 2*pi*r
CircleArea = float(pi*rad*rad)
LateralArea = float(h*cir)
TotalArea = float(cir*h+2*CircleArea)
print("Total area of the cylinder: " + str(TotalArea))

#e
firstName = [input("Please enter your first name: ")]
surname = [input("Please enter your surname: ")]
alist = (firstName[0])
blist = (surname[0])
print (alist + blist)

#f
age = int(input("Please enter your age: "))
print(age>=18)
