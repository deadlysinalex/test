import math # Makes the math library available. 
def main() : 
 print ("This program finds the real solutions to a quadratic") 
 
 a = float (input ("Enter coefficient a: ") ) 
 b = float (input ("Enter coefficient b: ") ) 
 c = float (input ("Enter coefficient c: ") )
 
 discRoot = math.sqrt (b*b -4*a*c)
 
 root1 = (-b + discRoot) / (2 * a) 
 root2 = (-b - discRoot) / (2 * a) 
 
 print ("The solutions are: ", root1, root2 )
 
main()
