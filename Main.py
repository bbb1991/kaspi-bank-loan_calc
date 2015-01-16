__author__ = 'bbb1991'

import Express_Loan
import Cash_Loan
import Input_Check_Args
import Calculation_Of_Payments

credit_amount = 0       #Сумма кредитования
credit_term = 0         #Срок кредитования
INTEREST_RATE = 0       #Годовая процентая ставка кредитования
BANKING_SERVICES = 0    #Банковское обслуживаение, в месяц, списывается в дату платежа
is_best_client = False

"""
Disclaimer. Внимание! Калькулятор создан на основе калькулятора, используемыми менеджерами-универсалами
каспи банка. Формулы аннуитетного платежа найдены в сети. Нет возможности проверять расчеты досконально на практике.
За любое расхождение по суммам автор не несет ответственности.
Вы предупреждены.
"""

print("Привет! Я кредитный калькулятор для kaspi bank!\n")

credit_amount = Input_Check_Args.inputting_amount()  #Ввод и проверка суммы
if credit_amount <= 300000:     #Проверка вида кредитования
    credit_term = Input_Check_Args.inputting_term(Express_Loan.MIN_TERM, Express_Loan.MAX_TERM)
else:
    credit_term = Input_Check_Args.inputting_term(Cash_Loan.MIN_TERM, Cash_Loan.MAX_TERM)

if input("Являетесь ли Вы лучшим клиентом банка? [y/n]: ") == 'y':  #Проверка на статуса "Лучший клиент
    is_best_client = True


# годовая процентная ставка изменяется согласно сумме кредитования
# до 300 000 тенге это "экспресс кредитование"
# больше 300 000 тенге это "кредит наличными"
if credit_amount <= 300000:          #Блок экспресс кредитования
    if is_best_client:
        INTEREST_RATE = Express_Loan.INTEREST_RATE_BC
    else:
        INTEREST_RATE = Express_Loan.INTEREST_RATE

    BANKING_SERVICES = Express_Loan.BANKING_SERVICES    #Банкеовское обслуживание независимо от срока
else:                               #Блок "Кредит наличными"
    if is_best_client:
        INTEREST_RATE = Cash_Loan.INTEREST_RATE_BC
    else:
        INTEREST_RATE = Cash_Loan.INTEREST_RATE

    if credit_term <= 24:           #Банковское обслуживание согласно срокам
        BANKING_SERVICES = Cash_Loan.BANKING_SERVICES_6_24
    elif credit_term <= 48:
        BANKING_SERVICES = Cash_Loan.BANKING_SERVICES_27_48
    else:
        BANKING_SERVICES = Cash_Loan.BANKING_SERVICES_48_60

monthly_payment = Calculation_Of_Payments.calc(credit_term, credit_amount, INTEREST_RATE, BANKING_SERVICES)

print("\nКороткая информация:")
print("\tСрок кредитования: %d" % credit_term)
print("\tСумма кредитования: %d" % credit_amount)
print("\tЕжемесячный платеж:", end=' ')
print(monthly_payment)
print("\tПереплата всего:", end=' ')
print(monthly_payment * credit_term - credit_amount)

print("\n")
print("Месяц:\tЕжемесячный платеж:\tНачисленный процент:\tОстаток долга:")
Calculation_Of_Payments.x(credit_term, credit_amount, INTEREST_RATE, monthly_payment, BANKING_SERVICES)