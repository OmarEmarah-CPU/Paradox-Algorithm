def A():
    print("One")
    return B

def B():
    print("Two")
    return A

A()()()()()()()()
