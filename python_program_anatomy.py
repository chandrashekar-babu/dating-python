from time import ctime as now

def greet(n):
    msg = "Welcome to Python"
    print msg, n

name = "john"
greet(name)
print "The time now is", now()

