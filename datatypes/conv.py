# python program to convert into decimal number system
n1 = 0o17
n2 = 0b1110010
n3 = 0x1c2
print('octal 17 = ',int(n1))
print('Binary 1110010 = ',int(n2))
print('Hexadecimal 1c2 = ',int(n3))

str = "1c2"     # string str contains a hexidecimal number
print(int(str,16)) # hence base is 16. Convert sr into int
print('\n')
s1 = "17"
s2 ="1110010"
s3 = "1c2"
print('octal 17 = ',int(s1,8))
print('Binary 1110010 = ',int(s2,2))
print('Hexadecimal 1c2 = ',int(s3,16))
print('\n')
a=10
print(bin(a))
print(oct(a))
print(hex(a))
"""
Results:
octal 17 =  15
Binary 1110010 =  114
Hexadecimal 1c2 =  450
450


octal 17 =  15
Binary 1110010 =  114
Hexadecimal 1c2 =  450


0b1010
0o12
0xa
"""