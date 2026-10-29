class Calculator:
    def menu(self):
        print("Добро пожаловать в калькулятор!/Welcome to the calculator!")
        print("Выберите язык/Choose language:")

        while True:
            chosen_language = input("1. Русский\n2. English\n")
            if chosen_language == "1":
                self._operation_menu("ru")
                return
            if chosen_language == "2":
                self._operation_menu("en")
                return
            print("Неверный выбор языка. Попробуйте ещё раз./Invalid language choice. Try again.")

    def _operation_menu(self, language):
        while True:
            if language == "ru":
                print("Выберите операцию:")
                print("1. Сложение")
                print("2. Вычитание")
                print("3. Умножение")
                print("4. Деление")
                print("5. Выход")
                operation = input("Введите номер операции: ")
            else:
                print("Choose an operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Exit")
                operation = input("Enter the operation number: ")

            if operation == "5":
                self.exit_program(language)
                return
            self.perform_operation(operation, language)

    def perform_operation(self, operation, language):
        if operation not in {"1", "2", "3", "4"}:
            if language == "ru":
                print("Неверный выбор операции.")
            else:
                print("Invalid operation choice.")
            return

        if language == "ru":
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        else:
            if num2 == 0:
                if language == "ru":
                    print("Ошибка! Деление на ноль невозможно.")
                else:
                    print("Error! Division by zero is not possible.")
                return
            result = num1 / num2

        if language == "ru":
            print(f"Результат: {result}")
        else:
            print(f"Result: {result}")

    def exit_program(self, language):
        if language == "ru":
            print("Выход из программы. До свидания!")
        else:
            print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    Calculator().menu()
