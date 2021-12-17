#Binary is a base two number system. The four basic mathematical operations
#addition, subtraction, multiplication, and division are all done practically the same, with the only difference being the change in base

# Addition: 
#  0110 
# +0010
# -------
#  1000         Explanation: Go from right to left and add up the columns. 0 + 0 = 0. 1 + 1 = 2, but since 2 isn't allowed in base 2, we have to send it to the next column.
#               That means the current column has a value of 0. We go to the next column, and add 1 + 0 = 0, but we need to use the one we carried over. 1 + 1 + 0 = 2,
#               So we need to send a one to the next column and get a zero for the current column. Finally, we get 0 + 0 = 0, but we use the one we carried over for 0 + 0 + 1 = 1. 
#               and a final answer of 1000
#
# Subtraction:
#  0110
# -0011
# ------
#  0011         Explanation: Go from right to left, and subtract the columns. The trick with subtraction comes when you have a higher number on the bottom row than the one 
#               on the bottom. In that case, you must "borrow" the number from the left. In this example, you end up with 0 - 1 = -1, so you borrow from the left and get
#               10 - 1 = 1, in base ten this is 2 - 1 = 1. Going to the next row, you have 0 - 1 = -1 again, since you used the 1 from the top column already. So repeat this process, and
#               take the one from the left and get a value of 10 - 1 = 1. Finally your last two columns are 0 - 0 = 0, for a final answer of 0011.
#
#
# Multiplication:
#           11101
#          x 1001
#           ------
#           11101
#          00000x
#         00000xx
#       +11101xxx
#       ----------
#        100000101     Explanation: Take the rightmost bit of the smaller number, and multiply that by all the numbers in the other number. This is just normal multiplication, where 1x1 = 1 and 0 x 1 = 0,
#                       Once done, go to the next number in the smaller number and multiply that by every number, but first adding a placeholder 0 (shown as x in example).
#                       repeat this process for every bit in the smaller number, then add (see above) up all the results for your total. 
#
# Division
#   For now just read this https://www.cuemath.com/numbers/binary-division/