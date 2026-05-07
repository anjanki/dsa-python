#Bitwise operator it perform operation in bitwise &,|,~(nagation positive 5 give -6) << right shift and >> left shift
num1=4#0100
num2=2#0010
print(num1&num2)#0
print(num1|num2)#6
print(num1^num2)#same give 0 and diffrent give 1 so 0110
print(~num1)#revese 1011 , 2's complement 1100
print(num1<<2)#010000 extra two 00 added
print(num1>>2)#01 loose two bit

