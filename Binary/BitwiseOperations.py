#Python has standard bitwise operations
# & = and
# | = or
# ~ = logical complement of number, equivalent to -x - 1
# ^ = exclusive or

def bitwise_and(x,y):
    return bin(x & y)
# 1100 & 0011 -> 0
print(bitwise_and(0b1100, 0b0011))
# 1111 & 0111 -> 0111
print(bitwise_and(0b1111,0b0111))

def bitwise_or(x,y):
    return bin(x | y)

# 0011 | 1000 -> 1011
print(bitwise_or(0b0011, 0b1000))
# 1111 | 0000 -> 1111
print(bitwise_or(0b1111, 0b0000))

def bitwise_complement(x):
    return bin(~x)
# 1000 -> -1001
print(bitwise_complement(0b1000))
# 1010 -> -1011
print(bitwise_complement(0b1010))

def bitwise_xor(x,y):
    return bin(x ^ y)
# 1111 ^ 1111 -> 0000
print(bitwise_xor(0b1111,0b1111))
# 1100 ^ 1010 -> 0110
print(bitwise_xor(0b1100,0b1010))