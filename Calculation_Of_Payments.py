__author__ = 'bbb1991'

from math import pow

#                   Базовая формула аннуитетного платежа:

#                                           (ставка / 12 мес)
#       платеж = сумма кредита * ---------------------------------------
#                                  1 - (1 + (ставка / 12 мес) ^ срок

#                   Еще одна формула аннуитетного платежа:

#                                  (ставка / 12 мес) * (1 + (ставка / 12 мес)) ^ срок
#       платеж = сумма кредита * -------------------------------------------------------
#                                         ((1 + (ставка / 12 мес)) ^ срок) - 1


def calc(term, amount, rate, service):
    """ Расчет ежемесячного платежа """

    rate = (rate / 100) / 12    #Процентная ставка исчисляется в процентах, и в расчет берется месяц, т.е. делим на 12
    service = amount * (service / 100)

    return int(amount * rate / (1 - 1 / pow((1 + rate), term)) + service)


def x(term, amount, rate, monthly_fee, service):
    balance_of_debt = amount
    service = amount * (service / 100)

    for i in range(1, term + 1, 1):
        month = i
        credited = balance_of_debt * ((rate / 100) / 12) + service
        print(month, "\t\t", monthly_fee, "\t\t\t\t", int(credited), "\t\t\t\t\t", int(balance_of_debt))
        balance_of_debt -= monthly_fee - credited

