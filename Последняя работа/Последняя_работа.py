import os
import random

print("Выберете сложность:")
print("(1) - Легко")
print("(2) - Нормально")
print("(3) - Сложно\n")

# ввод сложности (1 - легко, 2 - нормально, 3 - сложно)
difficulty = input("Ввод: ")
difficulty = int(difficulty)

# проверка на корректность ввода
if difficulty != 1 and difficulty != 2 and difficulty != 3:
    print("Операции \"" + difficulty + "\" нет")
    exit()

# если была выбрана сложность 'Легко', то количество примеров будет 5
# если была выбрана сложность 'Нормально', то количество примеров будет 10
# если была выбрана сложность 'Сложно', то количество примеров будет 15
number_of_expressions = difficulty * 5

print("Введите величину генерируемых чисел")

# ввод диапазона генерируемых чисел
bounds = input("Ввод: ")
bounds = int(bounds)

# проверка чтобы вводимое значение было больше 1
if bounds < 1:
    print("Ввод не корректный")
    exit()

print("Сложность: " + str(difficulty))
print("Величина чисел: " + str(bounds) + "\n")

counter = 0
correct_answers = 0
operations = ["+", "-", "*", "/", "**"]

# главный цикл
while counter < number_of_expressions:

    # генерация случайных чисел в заданых рамках и выбор случайно операции (+, -, *, /, **)
    number1 = random.randint(1, bounds)
    number2 = random.randint(1, bounds)
    operation = random.choice(operations)

    result = int()

    if operation == "+":
        result = number1 + number2

    if operation == "-":
        result = number1 - number2

    if operation == "*":
        result = number1 * number2

    if operation == "/":
        # проверка на дробные числа при делении
        # т.е. например если первое число = 1, а второе число = 3,
        # то при делении 1 на 3 получается дробное число (в данном случае оно бесконечное)
        # и эта проверка помогает избежать такие случаи
        result = number1 / number2
        if (result).is_integer() == False:
            continue
        else:
            result = int(result)

    if operation == "**":
        result = number1 ** number2

    # ввод результата от лица пользователя
    user_input = input(str(number1) + " " + operation + " " + str(number2) + " = ")
    user_input = int(user_input)

    # если ответ верен, то увеличиваем счетчик верных ответов на 1
    if user_input == result:
        correct_answers = correct_answers + 1

    counter = counter + 1

# количество верных ответов в процентом соотношении
percent_of_correct_answers = correct_answers / number_of_expressions * 100

print("Правильных ответов: " + str(correct_answers) + " / " + str(number_of_expressions))
print("Процент верных ответов: " + str(percent_of_correct_answers))

if (percent_of_correct_answers >= 90):
    print("Оценка: 5")

if (percent_of_correct_answers >= 75 and percent_of_correct_answers < 90):
    print("Оценка: 4")

if (percent_of_correct_answers >= 60 and percent_of_correct_answers < 75):
    print("Оценка: 3")

if (percent_of_correct_answers < 60):
    print("Оценка: 2")
