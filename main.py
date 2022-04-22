#implicit type conversion
num_int = 125
num_flo = 1.25
num_new = num_int + num_flo
print(num_new)
print(type(num_int))
print(type(num_flo))
print(type(num_new))#python converts a smaller type to the larger type to avoid data loss
'''num_flo = 1.33
num_string = "133"
num_new = num_flo + num_string
print(num_new)
print(type(num_string))
print(type(num_flo))
print(type(num_new))#Python cannot use implicit conversions in such cases.'''
#Explicit type conversions/typecasting
num_int = 145
num_string = "145"
print(type(num_int))
print(type(num_string))
num_string = int(num_string)
print(type(num_string))
num_sum = num_int + num_string
print(type(num_sum))
print(num_sum)




