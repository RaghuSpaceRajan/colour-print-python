rc = "\033[31;1m"
gc = "\033[32;1m"
yc = "\033[33;1m"
bc = "\033[34;1m"

ec = "\033[0m"


def p(var, options=None, **kwargs): 
    print(str(var), **kwargs)

def pr(var):
    print(rc + str(var) + ec)

def pg(var):
    print(gc + str(var) + ec)

def py(var):
    print(yc + str(var) + ec)

def pb(var):
    print(bc + str(var) + ec)

if __name__ == '__main__':
    p("Normal")
    pr("Red")
    pg("Green")
    py("Yellow")
    pb("Blue")
