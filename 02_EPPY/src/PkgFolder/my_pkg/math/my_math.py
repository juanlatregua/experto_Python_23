def add(a, b):
    return a + b

def mul(a,b):
    return a * b

def div(a, b):
    assert(b != 0)
    return a / b

def min(a,b):
    return a if a<b else b

if __name__ == "__main__":
    # tests
    assert(add(2,3) == 5)
    assert(add(0,3) == 3)
    assert(add(-1,3) == 2)
    assert(add(1,-4) == -3)
    assert(add(-1,-4) == -5)
    print("All Tests Passed Successfully")