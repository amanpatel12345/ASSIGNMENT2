
#Arithmetic Operators:

a = 10
b = 5
addition = a + b;         # Addition operator (+)
subtraction = a - b;      # Subtraction operator (-)
multiplication = a * b;   # Multiplication operator (*)
division = a / b;         # Division operator (/)
modulus = a % b;          # Modulus operator (%)

#Assignment Operators:

x = 10
x += 5;       # Addition assignment operator (+=)
x -= 3;       # Subtraction assignment operator (-=)
x *= 2;       # Multiplication assignment operator (*=)
x /= 4;       # Division assignment operator (/=)
x %= 3;       # Modulus assignment operator (%=)

#Comparison Operators:

p = 5
q = 10
isEqual = (p == q);   # Equal to operator (==)
isNotEqual = (p != q);# Not equal to operator (!=)
isGreater = (p > q);  # Greater than operator (>)
isLess = (p < q);     # Less than operator (<)
isGreaterOrEqual = (p >= q);   # Greater than or equal to operator (>=)
isLessOrEqual = (p <= q);      # Less than or equal to operator (<=)

#Logical Operators:

c = True
d = False
print("c and d is",c and d)  # Logical AND operator (&&)
print("c or d is",c or d)    # Logical OR operator (||)
print("not d is",not d)      # Logical NOT operator (!)

#Bitwise Operators:

m = 5;  # binary: 0101
n = 3;  # binary: 0011
bitwiseAnd = m & n;     # Bitwise AND operator (&)
bitwiseOr = m | n;      # Bitwise OR operator (|)
bitwiseXor = m ^ n;     # Bitwise XOR operator (^)
bitwiseComplement = ~m; # Bitwise complement operator (~)
leftShift = m << 1;     # Left shift operator (<<)
rightShift = m >> 1;    # Right shift operator (>>)

#identity operator:

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)     # False - x and y refer to different memory locations
print(x is z)     # True - x and z refer to the same memory location
print(x is not y) # True - x and y do not refer to the same memory location
print(x is not z) # False - x and z refer to the same memory location

#membership operator:

message = "Hello, world!"

print("Hello" in message)           # True - "Hello" is present in the string
print("world" in message)           # True - "world" is present in the string
print("Python" not in message)      # True - "Python" is not present in the string
print("Hello" not in message)       # False - "Hello" is present in the string