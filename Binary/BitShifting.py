#Bitshifts are NOT done in place, they need to be stored in new variables
#Returns x with the bits left shifted by y places. This is the same as multiplying x * 2^y, so it is a cheap replacement for any multiplication by a power of 2.
def shift_left_y_times(x,y):
    return bin(x << y)

# 1100 -> 11000
print(shift_left_y_times(0b1100, 1))
# 0010101 -> 101010000 
print(shift_left_y_times(0b0010101, 4))

#Returns x with the bits right shifted by y places. This is an arithmetic shift, meaning it will append the leftmost bit y times for negative numbers. 
#Equivalent to dividing x / 2^y, rounded towards negative infinity.
def shift_right_y_times(x,y):
    return bin(x >> y)

# 1100 -> 0110
print(shift_right_y_times(0b1100, 1))
# 0010101 -> 0000001
print(shift_right_y_times(0b0010101,4))


