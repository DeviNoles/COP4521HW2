import time

def log(*args):
    def wrap(f):
       # print("Inside wrap()")
        def wrapped_f(*args):
            print("********************************************")
            print("Calling function " + f.__name__)
         #   print("Inside wrapped_f()")
            print("Arguments:")
            for arg in args:
                print("\t- ", arg, " of type ", type(arg).__name__)
            #star timer here
           
            print("Output: ")
            start_time = time.perf_counter()
            retValue = f(*args)
            end_time = time.perf_counter()
            print("Execution time ", "%.5f s" % (end_time-start_time))
            #end timer
            if(retValue != None):
                print("Return value: ", retValue, " of type ", type(retValue).__name__)
            else:
                print("No return value.")
            print("********************************************")
        return wrapped_f
    return wrap

@log("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
@log()
def wasteTime(a,b,c):
    time.sleep(1)
    return(a,b,c)
#print("After decoration")

#print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
#print(wasteTime(5,4,3))
@log()
def factorial(*nums_list):
    results = []
    for number in nums_list:
        res = number
        for i in range(number-1,0,1):
            res = i*res
        results.append(res)
        return results
@log("logger.txt")
def waste_time(a,b,c):
    print("Wasting Time")
    time.sleep(5)
    return a,b,c
@log("logger.txt")
def gcd(a,b):
    print("THE GCD of ", a, " and", b, " is ", end="")
    while a!=b:
        if a>b:
            a -= b
        else:
            b -= a
        print(abs(a))
        return abs(a)
@log()
def print_hello():
    print("Hello!")
@log(10)
def print_goodbye():
    print("Goodbye!")
if __name__ == "__main__":
    factorial(4,5)
    waste_time("one", 2, "3")
    gcd(15,9)
    print_hello()
    print_goodbye()