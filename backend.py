##Standard Libraries

## Third Party Libraries

## Functions

def conversion_from_decimal(number, divider):
    remainder = []
    dict_hexadecimal_letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    while number >= 1:

        if (number%divider) >=10:
            remainder.append(dict_hexadecimal_letters[(number%divider)])
            print(remainder)
        else:
            remainder.append(number % divider)

        print(number, "/", divider, "=", number//divider, "Remainder = ", remainder[len(remainder)-1])
        number = number // divider

    return "".join(str(x) for x in remainder[::-1])


def decimal_to_binary_conversion(number):
    return conversion_from_decimal(number,2)

def decimal_to_hexadecimal_conversion(number):
    return conversion_from_decimal(number, 16)
  
def decimal_to_octal_conversion(number):
    return conversion_from_decimal(number, 8)


def conversion_to_decimal(number, divider):
    dict_hexadecimal_letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    counter = 0
    sum = 0
    current = 0
    start = 0
    first_two_chars = "0x"

    if first_two_chars == str(number)[:2]:
        number = number[2:]

    for x in str(number)[::-1]:

        if x != "x":
            if x in dict_hexadecimal_letters:
                x = dict_hexadecimal_letters[x]
            
            current = (int(x) * (divider **counter))
            print(x, "*", divider, "to the", counter, "= ", current)
            sum = sum + current

            counter += 1 

    return sum

def hexadecimal_to_decimal_conversion(number):
    return conversion_to_decimal(number, 16)
    
def binary_to_decimal_conversion(number):
    return conversion_to_decimal(number, 2)

def octal_to_decimal_conversion(number):
    return conversion_to_decimal(number, 8)
 

#octal to hexa
# octal to binary

#binary to octal
# binary to hexa

## hexa to octal
## hexa to binary
### hex decimal function

## binary decimal function


if __name__ == "__main__":

    number_1 = 45

    # print(decimal_to_binary_conversion(number_1))
    # print(decimal_to_hexadecimal_conversion(number_1))

    print(hexadecimal_to_decimal_conversion("0x4B6"))
    print(binary_to_decimal_conversion(110))

