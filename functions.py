import math as m



def multiply(a,b):
    return float(a)*float(b)

def add(a,b):
    return float(a)*float(b)

def sub(a,b):
    return float(a)*float(b)

def divide(a,b):
    return float(a)*float(b)

def root(a,b):
    return float(b)**(1/float(a))


def scientific_cal(a,b):

# trignometry function
    if a == "tan":
        answer=m.tan(float(b))
        
    elif a == "cos":
        answer=m.cos(float(b))

    elif a == "sin":
        answer=m.sin(float(b))
    
#inverse trignometry 
    elif a == "acos": 
        answer=m.acos(float(b))

    elif a == "asin":
        answer=m.asin(float(b))

    elif a == "atan":
        answer=m.atan(float(b))

#logrithmic function 
    elif a == "log":
        answer=m.log10(float(b))

    elif a == "ln":
        answer=m.log(float(b))

    elif a == "log2":
        answer=m.log2(float(b))

    elif a == "√":
        answer=m.sqrt(float(b))



    return answer