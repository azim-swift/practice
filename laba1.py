#Вариант 7. Натуральные числа.
#Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр. 
#Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.


def convert_number_to_words(number):
    words_dict = {
        '0': 'нуль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join([words_dict[digit] for digit in str(number)])

def process_lexemes(file_name, k):
    lexemes = []
    current_lexeme = ''
    previous_digit = ''
    consecutive_count = 1

    with open(file_name, 'r') as file:
        while True:
            block = file.read(1024)

            if not block:
                break

            for char in block:
                if char.isnumeric():
                    if char == previous_digit:
                        consecutive_count += 1
                    else:
                        if consecutive_count > k:
                            lexemes.append((previous_digit * consecutive_count,
                                            convert_number_to_words(previous_digit),
                                            consecutive_count))
                        previous_digit = char
                        consecutive_count = 1
                elif previous_digit:
                    if consecutive_count > k:
                        lexemes.append((previous_digit * consecutive_count,
                                        convert_number_to_words(previous_digit),
                                        consecutive_count))
                    previous_digit = ''
                    consecutive_count = 1

    return lexemes

# тест
file_name = 'input.txt'
k = int(input('Введите k: '))
lexemes = process_lexemes(file_name, k - 1)

for lexeme in lexemes:
    number, number_words, repetitions = lexeme
    print(f"Число: {number}, Повторяющееся число: {number_words}, Всего повторений числа: {repetitions}")
