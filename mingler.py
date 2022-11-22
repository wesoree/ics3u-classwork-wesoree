bar = 5

def foo():
    global bar
    bar = 10
    print (bar)

print(bar)
foo()
print(bar)