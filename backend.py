# ##Standard Libraries

# ## Third Party Libraries

# ## Functions

# def conversion_from_decimal(number, divider):
#     remainder = []
#     dict_hexadecimal_letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

#     while number >= 1:

#         if (number%divider) >=10:
#             remainder.append(dict_hexadecimal_letters[(number%divider)])
#             # print(remainder)
#         else:
#             remainder.append(number % divider)

#         # print(number, "/", divider, "=", number//divider, "Remainder = ", remainder[len(remainder)-1])
#         number = number // divider

#     return "".join(str(x) for x in remainder[::-1])


# def decimal_to_binary_conversion(number):
#     return conversion_from_decimal(number,2)

# def decimal_to_hexadecimal_conversion(number):
#     return conversion_from_decimal(number, 16)
  
# def decimal_to_octal_conversion(number):
#     return conversion_from_decimal(number, 8)


# def conversion_to_decimal(number, divider):
#     dict_hexadecimal_letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

#     counter = 0
#     sum = 0
#     current = 0
#     start = 0
#     first_two_chars = "0x"

#     if first_two_chars == str(number)[:2]:
#         number = number[2:]

#     for x in str(number)[::-1]:

#         if x != "x":
#             if x in dict_hexadecimal_letters:
#                 x = dict_hexadecimal_letters[x]
            
#             current = (int(x) * (divider **counter))
#             # print(x, "*", divider, "to the", counter, "= ", current)
#             sum = sum + current

#             counter += 1 

#     return sum

# def hexadecimal_to_decimal_conversion(number):
#     return conversion_to_decimal(number, 16)
    
# def binary_to_decimal_conversion(number):
#     return conversion_to_decimal(number, 2)

# def octal_to_decimal_conversion(number):
#     return conversion_to_decimal(number, 8)
 

# #octal to hexa
# # octal to binary

# def octal_to_binary_conversion(number):
#     dict_octal_binary_numbers = {0: "000", 
#                                  1: "001",
#                                  2: "010",
#                                  3: "011",
#                                  4: "100",
#                                  5: "101",
#                                  6: "110",
#                                  7: "111"}
    
#     result = ""

#     for x in str(number)[::-1]:
#         result = result + dict_octal_binary_numbers[int(x)]

#     return int(result)

# def binary_to_octal_conversion(number):
#     dict_octal_binary_numbers = {"000": 0, 
#                                  "001": 1,
#                                  "010": 2,
#                                  "011": 3,
#                                  "100": 4,
#                                  "101": 5,
#                                  "110": 6,
#                                  "111": 7}
#     result = ""


#     for i in range(0, len(str(number)), 3):

#         result = result + str(dict_octal_binary_numbers[str(number)[i:i+3]])      

#     return result



# def binary_to_hexa_conversion(number):
#     dict_binary_to_hexa = {"0000": 0,
#                            "0001": 1,
#                            "0010": 2,
#                            "0011": 3,
#                            "0100": 4,
#                            "0101": 5,
#                            "0110": 6,
#                            "0111": 7,
#                            "1000": 8,
#                            "1001": 9,
#                            "1010": "A",
#                            "1011": "B",
#                            "1100": "C",
#                            "1101": "D",
#                            "1110": "E",
#                            "1111": "F"}

#     result = ""
#     for i in range(0, len(str(number)), 4):

#         result = result + str(dict_binary_to_hexa[str(number)[i:i+4]])      

#     return result

# def hexa_to_binary_conversion(number):
#     dict_binary_to_hexa = {0: "0000",
#                            1: "0001",
#                            2: "0010",
#                            3: "0011",
#                            4: "0100",
#                            5: "0101",
#                            6: "0110",
#                            7: "0111",
#                            8: "1000",
#                            9: "1001",
#                            10: "1010",
#                            11: "1011",
#                            12: "1100",
#                            13: "1101",
#                            14: "1110",
#                            15: "1111"}

#     result = ""

#     ### need to mod 4 to check, and add 00 to pad
#     for i in range(0, len(str(number)), 4):

#         result = result + str(dict_binary_to_hexa[str(number)[i:i+4]])      

#     return result

# def octal_to_hexa_conversion(number):
#     print(0)

# def hexa_to_octal_conversion(number):
#     print(0)






if __name__ == "__main__":

    decimal_test = 45
    binary_test = "101101"
    hexa_test = "2D"
    octal_test = "55"
    
    # ##works
    # print("Decimal to Binary", decimal_to_binary_conversion(decimal_test))
    # print("Decimal to Hexadecimal", decimal_to_hexadecimal_conversion(decimal_test))
    # print("Decimal to Octal", decimal_to_octal_conversion(decimal_test))

    # ##works
    # print("-------")
    # print("Binary to Decimal", binary_to_decimal_conversion(binary_test))
    # print("Hexadecimal to Decimal", hexadecimal_to_decimal_conversion(hexa_test))
    # print("Octal to Decimal", octal_to_decimal_conversion(octal_test))

    # print("Octal to Binary", octal_to_binary_conversion(55))
    # print("Octal to Binary", binary_to_octal_conversion(101101))


    # print("Binary to Hexadecimal", binary_to_hexa_conversion(1010101101001))
