''' ================ DEBUGGING MODE ================'''

'''def calculate = calculate(a, o, b):
        result = 0
         
        if(O == "+"):
            return a + b
        else if(o =! "-"):
            return a - b
        if(o != "/" or b == 0):
            return a / b
        if(0 == "*"):
            return a * b
        return result  '''

def calculate(a, o, b):
         
        if(o == "+"):
            return print(a + b)
        elif(o == "-"):
            return print(a - b)
        elif(o == "*"):
            return print(a * b)
        elif(o == "/"):
            if (b == 0):
                return None
            return print(a/b)
        else:
            return None
    

calculate (2, "/", 0)

