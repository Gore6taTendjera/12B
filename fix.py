from bs4 import BeautifulSoup

try:
    # Отваряне на HTML файла
    with open('Начало.html', 'r', encoding='utf-8') as file:
        html = file.read()
except FileNotFoundError:
    print('Грешка: HTML файлът не е намерен')
    exit()

# Парсване на HTML кода
soup = BeautifulSoup(html, 'html.parser')

# Извличане на всички елементи
elements = soup.find_all()

# Извличане на всички класове
classes = []
for element in elements:
    if 'class' in element.attrs:
        classes.extend(element['class'])

try:
    # Отваряне на CSS файла
    with open('asd.css', 'r') as file:
        css = file.read()
except FileNotFoundError:
    print('Грешка: CSS файлът не е намерен')
    exit()

# Разделяне на CSS файла на правила
rules = css.split('}')

# Преглед на всички правила
for rule in rules:
    # Проверка дали правилото съдържа класове
    if '.' in rule:
        # Извличане на имената на класовете
        rule_classes = [c.strip() for c in rule.split('{')[0].split('.') if c]
        # Проверка дали класовете се използват в HTML документа
        if not any(c in classes for c in rule_classes):
            # Ако класовете не се използват, премахване на правилото
            css = css.replace(rule + '}', '')

try:
    # Записване на новия CSS файл
    with open('new-styles.css', 'w') as file:
        file.write(css)
except IOError:
    print('Грешка: Не може да се запише новият CSS файл')