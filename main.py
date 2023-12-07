from sys import argv



def is_happy(number, power, result):
    """
    Check if a given number is a happy number.

    Parameters:
    number (int): The number to be checked.
    power (int): The power used to calculate the sum of the digits.
    result (int): The expected result of the calculation to define if the number
    is happy or not.
    
    Returns:
    bool: True if the number is happy, False otherwise.
    """
    # numbers_list = list
    numbers_set = set()
    while number != result and number not in numbers_set:
        # numbers_list.append(number)
        numbers_set.add(number)
        number = sum(int(digit) ** power for digit in str(number))
    return number == result

def generate_happy_numbers(last_number, power, final_result=1):
    """
    Generate all happy numbers up to a given number.

    Parameters:
    last_number (int): The last number to generate happy numbers up to.
    power (int): The power used to calculate the sum of the digits.
    final_result (int, optional): The expected result of the calculation to
    define if the number is happy or not. Defaults to 1.
    
    Returns:
    list: A list of all happy numbers up to the last number.
    """
    happy_numbers = []
    for number in range(1, last_number + 1):
        if is_happy(number, power, final_result):
            happy_numbers.append(number)
    return happy_numbers

if __name__ == "__main__":
    try:
        last_number = int(argv[1])
        power = int(argv[2])
        if last_number <= 0 or power <= 0:
            raise ValueError
        if len(argv) == 3:
            happy_numbers = generate_happy_numbers(last_number, power)
            print(happy_numbers)
        elif len(argv) == 4:
            final_result = int(argv[3])
            happy_numbers = generate_happy_numbers(last_number, power, final_result)
            print(happy_numbers)
    except ValueError:
        print("format: python main.py <last_number:int> <power:int> [<final_result:int> optional]")
        print("the integers need to be positive and greater than 0")

    