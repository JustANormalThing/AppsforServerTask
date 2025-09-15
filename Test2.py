import os
from abc import ABC, abstractmethod


class Credit(ABC):
    def __init__(self, bank_name, interest_rate, max_amount, allows_early_repayment, allows_increase_line):
        self.bank_name = bank_name
        self.interest_rate = interest_rate
        self.max_amount = max_amount
        self.allows_early_repayment = allows_early_repayment
        self.allows_increase_line = allows_increase_line

    @abstractmethod
    def display_info(self):
        pass

    def calculate_monthly_payment(self, amount, months):
        monthly_rate = self.interest_rate / 12 / 100
        return (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

class TargetCredit(Credit):
    def __init__(self, bank_name, interest_rate, max_amount, allows_early_repayment, allows_increase_line, purpose):
        super().__init__(bank_name, interest_rate, max_amount, allows_early_repayment, allows_increase_line)
        self.purpose = purpose

    def display_info(self):
        print(f"Целевой кредит банка: {self.bank_name}")
        print(f"Процентная ставка: {self.interest_rate}%")
        print(f"Максимальная сумма: {self.max_amount}")
        print(f"Досрочное погашение: {'Да' if self.allows_early_repayment else 'Нет'}")
        print(f"Возможность увеличить кредитную линию: {'Да' if self.allows_increase_line else 'Нет'}")
        print(f"Цель кредита: {self.purpose}")
        print("-" * 40)

class BankCredit(Credit):
    def display_info(self):
        print(f"Банковский кредит банка: {self.bank_name}")
        print(f"Процентная ставка: {self.interest_rate}%")
        print(f"Максимальная сумма: {self.max_amount}")
        print(f"Досрочное погашение: {'Да' if self.allows_early_repayment else 'Нет'}")
        print(f"Возможность увеличить кредитную линию: {'Да' if self.allows_increase_line else 'Нет'}")
        print("-" * 40)

class CreditService:
    def __init__(self, credits):
        self.credits = credits

    def display_all(self):
        for credit in self.credits:
            credit.display_info()

    def search_by_bank(self, bank_name):
        results = [c for c in self.credits if bank_name.lower() in c.bank_name.lower()]
        if results:
            for c in results:
                c.display_info()
        else:
            print("Кредиты по заданному банку не найдены.")

    def filter_by_interest_rate(self, min_rate, max_rate):
        results = [c for c in self.credits if min_rate <= c.interest_rate <= max_rate]
        if results:
            for c in results:
                c.display_info()
        else:
            print("Кредиты не найдены по заданным условиям.")

def load_credits(filename):
    credits = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) >= 6:
                    type_ = parts[0]
                    bank = parts[1]
                    rate = float(parts[2])
                    max_amount = float(parts[3])
                    allows_early = parts[4].lower() == 'true'
                    allows_increase = parts[5].lower() == 'true'
                    purpose = parts[6] if len(parts) > 6 else ''
                    if type_ == 'target':
                        credits.append(TargetCredit(bank, rate, max_amount, allows_early, allows_increase, purpose))
                    elif type_ == 'bank':
                        credits.append(BankCredit(bank, rate, max_amount, allows_early, allows_increase))
    except FileNotFoundError:
        print("Файл с данными не найден.")
    return credits

def main():
    filename = 'credits.txt'
    credits = load_credits(filename)
    service = CreditService(credits)

    while True:
        print("\nВыберите действие:")
        print("1 - Показать все кредиты")
        print("2 - Поиск по банку")
        print("3 - Фильтрация по процентной ставке")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            service.display_all()
        elif choice == '2':
            bank_name = input("Введите название банка для поиска: ")
            service.search_by_bank(bank_name)
        elif choice == '3':
            try:
                min_rate = float(input("Введите минимальную ставку: "))
                max_rate = float(input("Введите максимальную ставку: "))
                service.filter_by_interest_rate(min_rate, max_rate)
            except ValueError:
                print("Некорректный ввод чисел.")
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

main()