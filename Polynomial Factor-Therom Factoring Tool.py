#Advanced Functions



x3 = 0
x2 = 0
x = 0                  #Varibles 
remain = 0
r = -1

from math import sqrt



       

#User input
try:
  print("f(x) = x^3 + x^2 + x + r (Factor tool)")            
  x3 = int(input("x^3?: "))
  x2 = int(input("x^2: "))
  x = int(input("x: "))
  remainder = int(input("remain  (Y intercept): "))

  print("f(x) = " + str(x3) + "x^3 + " + str(x2) + "x^2 + " + str(x) + "x + " + str(remainder))
except:
  print("Invalid Charactered Entered")
  exit()


#Processing y-intercept value
factors=[] 

if remainder > 0: 
        for i in range(1,remainder+1):
            if remainder % i == 0:
                factors.append(i)
                
        
elif remainder < 0: 
        for i in range(remainder,0):
            if remainder % i == 0:
                factors.append(i)
            

 #synthetic division algorithm
while  True:
 try:
  r = r+1
  nx1 = 0
  nx2 = 0
  nx3 = 0
  nx4 = 0
  factorv = factors[r]
  
  nx1 = x3 * factors[r]
  nx2 = nx1 + x2                      
  nx3 = x + (nx2 * factors[r]) 
  nx4 = remainder + (nx3 * factors[r])


  if nx4 == 0:
      break 
 except:
   print("Equation cannot be factored")  
   exit()
  

   
  
#output

operator = ""
factored = (0-factorv);
if factored > 0:
  operator = "+"

print("")
print("The Partial Factored Function: f(x) = " +  "(x" + operator + str(factored) + ")(" + str(nx1) + "x^2 + " + str(nx2) + "x + " + str(nx3) + ")")

#Quadratic Equation
a = nx1
b = nx2
c = nx3
try:
  eq1a = -b + (sqrt(b*b - 4*a*c))
  eq1 = eq1a/2*a
  eq2a = -b - (sqrt(b*b - 4*a*c))
  eq2 = eq2a/2*a
  eq2f = 0-eq2
  eq1f = 0-eq1
  eq1opr = ""
  eq2oper = ""
  if eq1f > 0:
    eq1opr = "+"
  if eq2f > 0:
    eq2oper = "+"
  print("Fully Factored: f(x) = " +  "(x" + operator + str(factored) + ")(x" + eq1opr + str(eq1f) + ")(x" + eq2oper + str(eq2f) + ")" )
except:
  print("Equation can't be simplfied any further")
  exit()


