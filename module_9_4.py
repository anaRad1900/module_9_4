from random import choice

# Задача 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
compare_chars = lambda f, s: f == s
result = list(map(compare_chars, first, second))
print(result)

# Задача 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")
    return write_everything

# Использование для записи
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задача 3: Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Использование
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())