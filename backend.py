##Standard Libraries

## Third Party Libraries

## Functions

def decimal_from_conversion(number, divider):
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
    return decimal_from_conversion(number,2)

def decimal_to_hexadecimal_conversion(number):
    return decimal_from_conversion(number, 16)
  


def hexadecimal_to_decimal_conversion(number):
    print(0)
def binary_to_decimal_conversion(number):
    binary = [x for x in str(number)]

    # prefix and post fix
    # remainder = []

    # while number >= 1:
    #     remainder.append(number % 2)
    #     print(number, "/", 2, "=", number//2, "Remainder = ", remainder[len(remainder)-1])
    #     number = number // 2

    # return "".join(str(x) for x in remainder[::-1])


 
# In hexadecimal, the digits 0-9 are the same as decimal, while 10-15 are represented by the letters A-F. 

### hex decimal function

## binary decimal function


if __name__ == "__main__":

    number_1 = 26

    print(decimal_to_binary_conversion(number_1))
    print(decimal_to_hexadecimal_conversion(number_1))

    print(binary_to_decimal_conversion(11010))

