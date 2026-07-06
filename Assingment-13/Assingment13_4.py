def binaryEquivalent(num):
    if num == 0:
        return "0"

    binary = ""

    while num > 0:
        rem = num % 2
        binary = str(rem) + binary
        num = num // 2

    return binary

def main():
    value = int(input("Enter a number: "))
    result = binaryEquivalent(value)
    print("Binary equivalent is:", result)

if __name__ == "__main__":
    main()