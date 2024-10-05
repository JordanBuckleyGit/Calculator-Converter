# Hey this is a caclulator for conversions
# Created by Jordan Buckley

def binaryBase2ToDecimal():
    binary = input("Please enter your binary number: ")
    decimal = 0
    
    length = len(binary)
    for i in range(length):
        digit = int(binary[length - 1 - i])  # Reverse index to go from right to left
        
        # If the binary digit is 1, we calculate the contribution to the decimal value
        if digit == 1:
            decimal += 2 ** i
    
    print(f"The decimal equivalent of binary {binary} is: {decimal}")

def decimalToBinaryBase2():
    decimal = int(input("Please enter your decimal number: "))
    
    # Edge case for 0
    if decimal == 0:
        print(f"The binary equivalent of decimal {decimal} is: 0")
        return
    
    # Initialize an empty string to store the binary result
    binary = ""
    
    while decimal > 0:
        remainder = decimal % 2  # Get the remainder when divided by 2
        binary = str(remainder) + binary  # Prepend the remainder to the binary string
        decimal = decimal // 2  # Update the decimal number by dividing it by 2
    
    print(f"The binary equivalent of decimal {decimal} is: {binary}")

def binaryBase4ToDecimal():
    binary_base4 = input("Please enter your base-4 binary number: ")
    decimal = 0
    
    length = len(binary_base4)
    for i in range(length):
        # Convert the current character to an integer (base 4 digit)
        digit = int(binary_base4[length - 1 - i])  # Reverse index to go from right to left
        
        # Check if the digit is valid (0, 1, 2, or 3)
        if digit not in [0, 1, 2, 3]:
            print("Invalid input: Base-4 digits must be 0, 1, 2, or 3.")
            return
        
        # Calculate the decimal value of this digit at its position
        decimal += digit * (4 ** i)
    
    print(f"The decimal equivalent of base-4 binary {binary_base4} is: {decimal}")

def decimalToBinaryBase4():
    decimal = int(input("Please enter your decimal number: "))

    # Edge case for 0
    if decimal == 0:
        print(f"The binary equivalent of decimal {decimal} is: 0")
        return
    
    binary_base4= ""

    while decimal > 0:
        remainder = decimal % 4  # Get the remainder when divided by 4 (base-4 digit)
        binary_base4 = str(remainder) + binary_base4  # Prepend the remainder to the binary string
        decimal = decimal // 4  # Update the decimal number by dividing it by 4
    
    # Output the final binary base-4 number
    print(f"The base-4 binary equivalent of your decimal number is: {binary_base4}")

def hexadecimalToDecimal():
    print("working on it.......")




def decimalToHexadecimal():
    decimal = int(input("Please enter your decimal number: "))

    # Edge case for 0
    if decimal == 0:
        print(f"The hexadecimal equivalent of decimal {decimal} is: 0")
        return
    
    hexadecimal = ""

    while decimal > 0:
        remainder = decimal % 16  # Get the remainder when divided by 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal  # For 0-9
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal  # For A-F
        decimal = decimal // 16  # Update the decimal number by dividing it by 16
    
    print(f"The hexadecimal equivalent of the input decimal number is: {hexadecimal}")


def main():
     while(True):
        print("\n--Welcome To The Conversion Calculator Menu--")
        print("_" * 35)
        print("1. Binary(base2) to Decimal")
        print("2. Decimal to Binary(base-2)")
        print("3. Binary(base4) to Decimal")
        print("4. Decimal to Binary(base-4)")
        print("5. Hexadecimal to Decimal")
        print("6. Decimal to Hexadecimal")
        print("0. Exit")
        print("_" * 35)
        option = int(input("Choose an option (0-6): "))
        print("\n")

        if option == 1:
            binaryBase2ToDecimal()
        elif option == 2:
            decimalToBinaryBase2()
        elif option == 3:
            binaryBase4ToDecimal()
        elif option == 4:
            decimalToBinaryBase4()
        elif option == 5:
            hexadecimalToDecimal()
        elif option == 6:
            decimalToHexadecimal()
            pass
        else:
            print("Thanks for using my calculator!!")
            break

main()
