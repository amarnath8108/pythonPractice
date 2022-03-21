input_number = input()
if input_number[0] == '0':
    input_number = input_number[1:]
reverse_number= input_number[::-1]
print("Reverse no {0}".format(reverse_number))
hex_number = hex(int(reverse_number))
print("Hexadecimal no {0}".format(hex_number[2:]))

'''input_string = input()
result=''
String_list = input_string.split(" ")
reverse_list = String_list[::-1]
for i in reverse_list:
    result = result +" "+i
print(result.strip())'''
