__author__ = 'bbb1991'


def inputting_amount():
    """
    Функция ввода и проверки суммы
    """
    while True:
        amount = int(input("Введите сумму кредитования: "))

        if amount < 20000:
            print("Ошибка! Минимальная сумма кредитования 20 000 тенге!")
        elif amount > 2000000:
            print("Ошибка! Максиимальная сумма кредитования 2 000 000 тенге!")
        else:
            if not amount % 10000 == 0:
                print("Внимание! Вы ввели некорректное значение!")
                print("Значение суммы будет округлена до ближайшего корректного значения:", end=' ')

                # Округление необходима, т.к. это условия оформления
                if amount % 10000 < 5000:
                    amount -= amount % 10000
                else:
                    amount += 10000 - amount % 10000
                print(amount)
            break
    return amount


def inputting_term(min_term, max_term):
    """ Ввод и проверка срока кредитования """
    while True:
        term = int(input("\nВведите срок кредитования: "))
        if term < min_term:
            print("Ошибка! Минимальный срок кредитования %d мес." % min_term)
        elif term > max_term:
            print("Ошибка! Максимальный срок кредитования %d мес." % max_term)
        else:
            if term % 3 != 0:
                print("Введена некорректное значение. Шаг кредитования составляет 3 мес.")
                print("Значение будет округлена до ближайшего значения: ", end='')

                # Округление необходима, т.к. это условия оформления
                if term % 3 < 1.5:
                    term -= term % 3
                else:
                    term += 3 - term % 3

                print(term)
            break
    return term