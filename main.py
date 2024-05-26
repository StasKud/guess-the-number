import random

def main():
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    guessed_numbers = []
    numbers_less_than = []
    numbers_greater_than = []

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте его угадать!")

    while attempts < max_attempts:
        try:
            user_input = input(f"Попытка {attempts + 1} из {max_attempts}. Введите число: ")
            user_guess = int(user_input)
            guessed_numbers.append(user_guess)

            if user_guess < number_to_guess:
                print("Ваше число меньше загаданного.")
                numbers_less_than.append(user_guess)
            elif user_guess > number_to_guess:
                print("Ваше число больше загаданного.")
                numbers_greater_than.append(user_guess)
            else:
                print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts + 1} попыток.")
                break

            attempts += 1
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    if attempts == max_attempts and user_guess != number_to_guess:
        print(f"К сожалению, вы не угадали число {number_to_guess}. Попробуйте снова!")

    with open('log.txt', 'w') as log_file:
        log_file.write("История игры:\n")
        log_file.write(f"Загаданное число: {number_to_guess}\n")
        log_file.write(f"Количество попыток: {attempts}\n")
        log_file.write("Введенные числа: " + ', '.join(map(str, guessed_numbers)) + "\n")
        log_file.write("Числа меньше загаданного: " + ', '.join(map(str, numbers_less_than)) + "\n")
        log_file.write("Числа больше загаданного: " + ', '.join(map(str, numbers_greater_than)) + "\n")
        if guessed_numbers and guessed_numbers[-1] == number_to_guess:
            log_file.write("Результат: Число угадано.\n")
        else:
            log_file.write("Результат: Число не угадано.\n")

if __name__ == "__main__":
    main()

