def raise_to_power(base_num, pow_num): # taking two inputes
    result = 1 #creating a variable
    for index in range(pow_num): # looping through the power numbers
        result = result * base_num
    return result

print(raise_to_power(3, 4))


