try:
    with open('python.work/text.txt', 'w', encoding='utf-8') as file:
        print(file.write('Hello, My name is Murod, I\'m Back-End Development'))
except FileNotFoundError:
    print('Файл не найден')