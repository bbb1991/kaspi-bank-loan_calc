__author__ = 'bbb1991'

"""
Вид кредитования: "Экспресс кредитование" или "Кредит наличными 15 минут"
Условия: Пенсионные отчисления не обяззательны, минимум 4 мес опыта на последнем месте
"""
INTEREST_RATE = 26.99       # Годовая процентая ставка кредитования для первичных и постоянных клиентов
INTEREST_RATE_BC = 23.99    # Годовая процентая ставка кредитования для лучших клиентов
BANKING_SERVICES = 2.19     # Банковское обслуживаение, в месяц, списывается в дату платежа

MIN_TERM = 3
MAX_TERM = 24