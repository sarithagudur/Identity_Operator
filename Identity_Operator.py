# 1) Store the value 5 in `x`.
x= 20
y= 20

# 2) Check if the datatype of `x` is exactly `int` using the identity operator `is`.
if type(x) is int:
    print(True)
else:
    print(False)
# - If it is an int, print "true"

# - Otherwise, print "false"

# 3) Store the value 5.5 in `x`.

# 4) Check if the datatype of `x` is NOT `float` using `is not`.
if type (x) is not float:
    print(True)
else:
    print(False)
    
# - If it is not a float, print "true"

# - Otherwise, print "false"

# 5) Store the value 20 in `x` and 20 in `y`.

# 6) Check if `x` and `y` refer to the same object (same identity) using `is`.
if x is y:
    print("Same identity")
if x is not y:
    print("Different identity")
# - If yes, print "x & y SAME identity"

# 7) Change `y` to 30.

# 8) Check if `x` and `y` do NOT refer to the same object using `is not`.

# - If yes, print "x & y have DIFFERENT identity"
