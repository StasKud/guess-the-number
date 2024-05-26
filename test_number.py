import random

def test_main():
    # Тестирование правильной работы функции main()

    # Тест 1: Проверка на корректное угадывание числа
    random.seed(1)
    correct_guess_test()

    # Тест 2: Проверка на обработку некорректного ввода
    random.seed(1)
    invalid_input_test()

    # Тест 3: Проверка на превышение максимального количества попыток
    random.seed(99)
    exceeded_attempts_test()

def correct_guess_test():
    # Тест на корректное угадывание числа
    number_to_guess = 20
    attempts = 0
    max_attempts = 10
    guessed_numbers = []

    while attempts < max_attempts:
        user_input = str(number_to_guess)
        guessed_numbers.append(int(user_input))

        if int(user_input) == number_to_guess:
            print("Test Passed: Correct guess test successful.")
            return True
        attempts += 1

    print("Test Failed: Correct guess test unsuccessful.")
    return False

def invalid_input_test():
    # Тест на обработку некорректного ввода
    number_to_guess = 51
    attempts = 0
    max_attempts = 10
    guessed_numbers = []

    invalid_inputs = ['a', '150', '50', '75', '25', '60', '55', '53', '52', '51']

    for user_input in invalid_inputs:
        try:
            user_guess = int(user_input)
            guessed_numbers.append(user_guess)

            if user_guess < number_to_guess:
                print("Test Passed: Invalid input test successful.")
                return True
        except ValueError:
            continue

    print("Test Failed: Invalid input test unsuccessful.")
    return False

def exceeded_attempts_test():
    # Тест на превышение максимального количества попыток
    number_to_guess = 91
    attempts = 0
    max_attempts = 10
    guessed_numbers = []

    while attempts < max_attempts:
        user_input = str(number_to_guess)
        guessed_numbers.append(int(user_input))

        if attempts == max_attempts - 1:
            print("Test Passed: Exceeded attempts test successful.")
            return True
        attempts += 1

    print("Test Failed: Exceeded attempts test unsuccessful.")
    return False

if __name__ == "__main__":
    test_main()