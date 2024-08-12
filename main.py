import math

# 1a) Recursive function to calculate the number of digits in the binary representation of n
def calculate_binary_digits(n):
    """
    Calculates the number of digits in the binary representation of a positive integer n

    :parameter:
    --------------------------------------------------------------------------------------
        n: A positive integer

    :return:
    --------------------------------------------------------------------------------------
        The number of digits in the binary representation of n.
    """
    if n == 1:
        return 1
    else:
        return 1 + calculate_binary_digits(math.floor(n/2))

# 1b) Main code block to run the function on the problem instances and print the output
if __name__ == "__main__":
    print(f'Number of digits in the binary expansion of 256: {calculate_binary_digits(256)}')
    print(f'Number of digits in the binary expansion of 750: {calculate_binary_digits(750)}')



