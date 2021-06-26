# Домашнее задание номер 2 из урока 2 "Основы языка Python"
# Текст задания: Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('исходный список - ', my_list)
print("-" * 50)
new_list = []
for ch in my_list:
    sign = ''
    if ch.count('+'):
        ch = ch.replace("+", "")
        sign = '+'
    elif ch.count('-'):
        ch = ch.replace("-", "")
        sign = '-'
    if ch.isdigit():
        new_list.append('"')
        new_list.append(f'{sign}{int(ch):02}')
        new_list.append('"')
    else:
        new_list.append(ch)
print('новый список - ', new_list)
result = ' '.join(new_list)
print('строка полученная через join() - ', result)
result = ''
second = False
for ch in new_list:
    sign = ''
    if ch.count('+'):
        ch = ch.replace("+", "")
        sign = '+'
    elif ch.count('-'):
        ch = ch.replace("-", "")
        sign = '-'

    if ch.isdigit():
        result += sign + ch
    elif ch == '"':
        result += ch + (' ' if second else '')
        second = not second
    else:
        result += ch + ' '
print('требуемая строка - ', result)