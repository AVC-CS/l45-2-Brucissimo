import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while total <= 100:
        number = random.randint(1, 10)
        numbers.append(number)
        total += number
    
    sum_numbers_exclude_last = sum(numbers[:-1])


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
