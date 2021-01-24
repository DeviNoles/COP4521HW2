def log(*args):
    print("Calling function " + __name__)
    for i in args:
        print(i)
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", args[0])
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@log("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")