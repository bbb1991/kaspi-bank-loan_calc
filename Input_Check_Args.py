__author__ = 'bbb1991'

MIN_SUM = 20000     # минимальная сумма кредитования
MAX_SUM = 1000000   # максимальная сумма кредитования
STEP_BY_MONTH = 3   # шаг кредитования в мес. (3, 6, 9 ... мес)
STEP_BY_SUM = 10000 # шаг кредитования в сумме (20000, 30000 ... тенге)


def inputting_amount():
    """
    Функция ввода и проверки суммы
    """
    while True:
        amount = int(input("Введите сумму кредитования: "))

        if amount < MIN_SUM:
            print("Ошибка! Минимальная сумма кредитования %d тенге!" % MIN_SUM)
        elif amount > MAX_SUM:
            print("Ошибка! Максиимальная сумма кредитования %d тенге!" % MAX_SUM)
        else:
            if not amount % STEP_BY_SUM == 0:
                print("Внимание! Вы ввели некорректное значение!")
                print("Значение суммы будет округлена до ближайшего корректного значения:", end=' ')

                # Округление необходима, т.к. это условия оформления
                if amount % STEP_BY_SUM < STEP_BY_SUM/2:
                    amount -= amount % STEP_BY_SUM
                else:
                    amount += STEP_BY_SUM - amount % STEP_BY_SUM
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
            if term % STEP_BY_MONTH != 0:
                print("Введена некорректное значение. Шаг кредитования составляет %d мес." % STEP_BY_MONTH)
                print("Значение будет округлена до ближайшего значения: ", end='')

                # Округление необходима, т.к. это условия оформления
                if term % STEP_BY_MONTH < 1.5:
                    term -= term % STEP_BY_MONTH
                else:
                    term += STEP_BY_MONTH - term % STEP_BY_MONTH

                print(term)
            break
    return term