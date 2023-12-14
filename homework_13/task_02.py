# Обновите приложение "Банк" из прошлой лекции таким образом,
# чтобы все данные о банковских аккаунтах сохранялись в базу данных.
# Перепишите функции load_accounts и save_accounts так, чтобы они писали и читали не из файла, а из базы данных.
# Название таблицы и столбцов в базе продумайте сами.

import random
import sqlite3
import os


class BankAccount:
    def __init__(self, card_holder, money=0.0, account_number=None, card_number=None, id=None):
        """
        Инициализирует банковский счет.

        :param id: Уникальный идентификатор
        :param card_holder: Имя держателя карты.
        :param money: Начальный баланс (по умолчанию 0.0).
        :param account_number: Номер счета (генерируется, если не указан).
        :param card_number: Номер карты (генерируется, если не указан).
        """
        self.id = id
        self.card_holder: str = card_holder.upper()
        self.money: float = money
        self.account_number: str = account_number or self.get_random_digits(16)
        self.card_number: str = card_number or self.get_random_digits(20)

    @staticmethod
    def get_random_digits(count: int) -> str:
        """
        Генерирует случайную строку из цифр.

        :param count: Количество цифр в генерируемой строке.
        :return: Строка из случайных цифр.
        """
        return ''.join([str(random.randint(0, 9)) for _ in range(count)])


def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    """
    Преобразует объект BankAccount в словарь.

    :param bank_account: Объект BankAccount для преобразования.
    :return: Словарь, представляющий объект BankAccount.
    """
    return {
        'card_holder': bank_account.card_holder,
        'money': bank_account.money,
        'card_number': bank_account.card_number,
        'account_number': bank_account.account_number
    }


def save_accounts(bank_accounts: list[BankAccount], file_name: str):
    """
    Сохраняет список банковских счетов в db-файл.

    :param bank_accounts: Список объектов BankAccount для сохранения.
    :param file_name: Имя db-файла для сохранения.
    """
    with sqlite3.connect(file_name) as connection:
        for account in bank_accounts:
            if account.id is None:
                data = (account.card_holder, account.money, account.account_number, account.card_number)
                connection.execute('INSERT INTO bank_accounts '
                                   '(card_holder, money, account_number, card_number) VALUES(?, ?, ?, ?)', data)
            else:
                data = (account.card_holder, account.money, account.account_number, account.card_number, account.id)
                connection.execute('UPDATE bank_accounts '
                                   'SET card_holder=?, money = ?, account_number=?, card_number=?'
                                   'WHERE id = ?', data)


def load_accounts(file_name: str) -> list[BankAccount]:
    """
     Загружает список банковских счетов из db-файла.

    :param file_name: Имя db-файла для загрузки.
    :return: Список объектов BankAccount, загруженных из файла.
    """
    if not os.path.exists(file_name):
        return []
    with sqlite3.connect(file_name) as connection:
        all_account = connection.execute('SELECT card_holder, money, account_number, card_number, id '
                                         'FROM bank_accounts')
        return [BankAccount(**value_account) for value_account in all_account.fetchall()]


class Bank:
    def __init__(self, bank_accounts: list[BankAccount] = None):
        """
        Инициализирует банк с переданным словарем банковских счетов.

        :param bank_accounts: Словарь банковских счетов.
        """
        self.__bank_accounts: dict[str, BankAccount] = {account.account_number: account for account in
                                                        bank_accounts or []}

    def open_account(self, card_holder: str) -> BankAccount:
        """
        Открывает новый банковский счет.

        :param card_holder: Имя держателя карты.
        :return: Новый объект BankAccount.
        """
        account = BankAccount(card_holder)
        self.__bank_accounts[account.account_number] = account
        return account

    def __get_account(self, account_number: str) -> BankAccount | None:
        """
        Возвращает найденный банковский счет.

        :param account_number (str): Номер аккаунта.
        :return: BankAccount: Новый объект BankAccount.
        """
        return self.__bank_accounts[account_number]

    def get_all_bank_accounts(self) -> list[BankAccount]:
        """
        Возвращает список всех банковских счетов.

        :return: list[BankAccount]: Список объектов BankAccount.
        """
        return list(self.__bank_accounts.values())

    def add_money(self, account_number: str, money: float):
        """
        Пополняет баланс банковского счета.

        :param account_number: Номер счета для пополнения.
        :param money: Сумма для пополнения.
        :return: В случае, если сумма отрицательная, будет выведено сообщение об ошибке.
        """
        target_account = self.__get_account(account_number)
        target_account.money += money

    def transfer_money(self, from_account_number: str, to_account_number: str, money: float):
        """
        Переводит деньги между банковскими счетами.

        :param from_account_number: Номер счета отправителя.
        :param to_account_number: Номер счета получателя.
        :param money: Сумма для перевода.
        :return: Если сумма отрицательная, будет выведено сообщение об ошибке.
        Если на счете отправителя недостаточно средств, будет выведено сообщение об ошибке.
        """
        from_account = self.__get_account(from_account_number)
        to_account = self.__get_account(to_account_number)
        from_account.money -= money
        to_account.money += money

    def external_transfer(self, from_account_number: str, to_external_number, money: float):
        """
        Переводит деньги между банковскими счетами.

        :param from_account_number: Номер счета отправителя.
        :param to_external_number: Номер счета получателя.
        :param money: Сумма для перевода.
        :return: Если сумма отрицательная, будет выведено сообщение об ошибке.
        Если на счете отправителя недостаточно средств, будет выведено сообщение об ошибке.
        """
        from_account = self.__get_account(from_account_number)
        from_account.money -= money
        print(f"Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}")


class Controller:
    def __init__(self, data_file_name: str):
        """
        Инициализирует контроллер.

        :param data_file_name: Имя файла данных для загрузки и сохранения банковских счетов.
        """
        self.data_file_name = data_file_name
        bank_accounts: list[BankAccount] = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print("Здравствуйте, наш банк открылся!")
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')

            action = input()
            if action == '0':
                save_accounts(self.bank.get_all_bank_accounts(), self.data_file_name)
                print("До свидания!")
                break
            elif action == '1':
                card_holder = input('Введите имя и фамилию держателя карты: ')
                account = self.bank.open_account(card_holder)
                print(f"Счёт {account.account_number} создан!")
            elif action == '2':
                print('Все счета:')
                for account in self.bank.get_all_bank_accounts():
                    print(f'Cчёт: {account.account_number}')
                    print(f'   Остаток на счету: {account.money}$')
                    print(f'   Номер карты: {account.card_number}')
                    print(f'   Держатель карты: {account.card_holder}')
            elif action == '3':
                account_number = input('Введите номер счёта: ')
                money = float(input('Введите количество денег: '))
                self.bank.add_money(account_number, money)
            elif action == '4':
                from_account_number = input('Введите номер счёта отправителя: ')
                to_account_number = input('Введите номер счёта получателя: ')
                money = float(input('Введите количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)
            elif action == '5':
                from_account_number = input('Введите номер счёта отправителя: ')
                to_external_number = input('Введите номер внешнего счёта: ')
                money = float(input('Введите количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Вы ввели неподдерживаемую команду')


if __name__ == '__main__':
    controller = Controller('bank.db')
    controller.run()
