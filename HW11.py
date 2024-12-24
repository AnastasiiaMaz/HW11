# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення ,
# якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.


while True:
    # Ввод данных
    num1 = input("Enter the first number: ")
    operation = input("Enter action (+, -, *, /): ")
    num2 = input("Enter the second number: ")

    # Преобразование целых чисел в дробные
    try:
        num1 = float(num1)
        num2 = float(num2)

        # Выбор действия с помощью match
        match operation:
            case '+':
                print(f"Result: {num1 + num2}")
            case '-':
                print(f"Result: {num1 - num2}")
            case '*':
                print(f"Result: {num1 * num2}")
            case '/':
                if num2 == 0:
                    print("Error: division by 0 is impossible!")
                else:
                    print(f"Result: {num1 / num2}")
            case _:  # Аналог else
                print("Invalid operation. Please try again.")

    except ValueError:
        print("Error: Please enter correct numbers!")

    # Запрос на продолжение
    cont = input("Do you want to continue? (y/n): ")
    if cont != 'y':
        print("Program terminated.")#если вводим "no/n" программа завершена
        break
