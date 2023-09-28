def poisk(x, y):    # поиск индекса
    if y in x:
        return x.index(y)
    else:
        return 'element not found'
def rem(x, y):    # удаление элемента
    a = list(x)
    if y in x:
        a.remove(y)
        b = tuple(a)
        return b
    else:
        return 'element not found'
def kolvo(x, y):   # коллво символов
    if y in x:
        a = 0
        for i in x:
            if i == y:
                a += 1

            else:
                continue
        return a
    else:
        return 'element not found'
def sliyani(x, y):   # слияние кортежей
    a = list(x)
    b = list(y)
    ab = a+b
    ab = tuple(ab)
    return ab




b = ['juk', 'pcache', False]
a = [1, 3, 3, -5, 7, 1]

print("Сумма",sum(a))
print('Максимальное число',max(a))
print("Уникальный список",set(a))

ob = a + b
print('Слияние',ob)


kor = (2, 2, 1, 5, 5, 5, 10)
kot = ('babochka', 1, True)

print('Поиск индекса',poisk(kor, 1))
print('Удаление из кортежа',rem(kor, 2))
print('Кол - во символов',kolvo(kor, 5))

gav = sliyani(kor, kot)
print('Слияние кортежей в один',gav)



