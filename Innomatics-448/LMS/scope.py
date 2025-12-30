# Global variables
a = 10
b = 11
c = 12

def ABC():
    # local variables
    d = 6
    e = 8
    if "h" in globals().keys():
        print("Not creating a new variable named a sice a is already a global")
    else:
        h = 10
    print(locals().keys())


if __name__ == "__main__":
    print(globals().keys())
    ABC()