import math
def f(x):
    return 4*math.e**-x*math.sin(x) - 1

def get_initial_guesses():
   while True:
        try:
            a = float(input("Enter the first initial guess: "))
            b = float(input("Enter the second initial guess: "))
            if f(a) * f(b) < 0:
                return a, b
            else:
                print("Invalid guesses. Please ensure that f(a) and f(b) have opposite signs.")
        except valueerror:
            print("Invalid value, plz input valid value: ")

def bisection_method(a, b, max_iterations):
    for i in range(max_iterations):
        c = (a + b) / 2  
        print("Iteration ",i + 1,": c = ",c," f(c) = ",f(c))

        if f(c)*f(a) == 0:  
            print("Exact root found: ",c)
            return c
        
        if f(a) * f(c) < 0:  
            b = c
        else: 
            a = c

    print("Approximate root after ",max_iterations," iterations: ",c)
    return c

a,b=get_initial_guesses()
bisection_method(a, b,1000)