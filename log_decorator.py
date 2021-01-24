import time
import sys

def log(*args):
    if(len(args)==1):
        
        def wrap(f):
       # print("Inside wrap()")
            def wrapped_f(*args):
                orig_stdout = sys.stdout
                fi = open("logger.txt", "a")
                sys.stdout = fi
                fi.write("********************************************\n")
                fi.write("Calling function " + f.__name__ +"\n")
            #   print("Inside wrapped_f()")
                fi.write("Arguments:\n")
                for arg in args:
                    retVal = "\t- " + str(arg)+" of type "+type(arg).__name__+"\n"
                    fi.write(retVal+"\n")
                #star timer here
            
                fi.write("Output: " +"\n")
                start_time = time.perf_counter()
                retValue = str(f(*args))
                end_time = time.perf_counter()
                timeOut = "Execution time "+"%.5f s" % (end_time-start_time)+"\n"
                fi.write(timeOut)
                #end timer
                sys.stdout = orig_stdout
                if(retValue != None):
                    retVal = "Return value: "+ str(retValue)+ " of type "+ type(retValue).__name__+"\n"
                    fi.write(retVal)
                else:
                    fi.write("No return value."+"\n")
                fi.write("********************************************\n\n")
                
            return wrapped_f
        return wrap
    else:
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

