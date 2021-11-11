# que 1 by recursion

n = 123

res = 0

n = list(str(n))

def program(n):
    if n:
        global res
        res += int(n[-1])
        n.pop()
        program(n)
    else:
        print(res)

# que 2

def function(n):

    i = 2

    while i-1 != n:
        for x in range(1,i):
            print(x, end=" ")
        for x in reversed(range(1,i-1)):
            print(x, end=" ")
        else:
            print("")
            i += 1
            
program(n) #ans 1
function(4) #ans 2