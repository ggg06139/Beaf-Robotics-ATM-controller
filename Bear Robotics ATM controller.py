import time

class ATM:
    def __init__(self, name, account_num, account_pin, balance=0):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance
        self.__account_pin = account_pin
        
    def __repr__(self):
        return f'\n{self.__name}\'s account ({self.__account_num}) has a balance of ${self.__balance}.'
    
    #Function to replace card insertion
    def discrimination_card(self):
        input_card = input('Please enter your card (Replace with text \'card\') : ')
        while input_card != 'card':
            print('Invalid input. Please re-enter')
            input_card = input('Please enter your card (Replace with text \'card\') : ')
            
    #Function to input PIN number
    def discrimination_pin(self):
        input_pin = input('Please enter your PIN : ')
        if self.__account_pin != int(input_pin):
            print('Invalid input. Please re-enter')
            self.discrimination_pin()

    #Function to choice options
    def discrimination_option(self):
        print('Please select an option')
        input_option = input('1.Withdrawal 2.Deposit 3.Balance Inquiry 4.Transfer 5.Exit (Please enter a number) : ')
        if input_option == '1':
            self.withdrawal()
        elif input_option == '2':
            self.deposit()
        elif input_option == '3':
            print(self)
        elif input_option == '4':
            self.transfer()
        elif input_option == '5':
            pass
        else:
            print('Invalid input. Please re-enter')
            self.discrimination_option()
    
    #Function to deposit
    def deposit(self):
        deposit_money = int(input('\nPlease enter the amount to deposit : '))
        self.time_sleep()
        self.__balance += deposit_money
        print(f'${deposit_money} has been deposited. The balance is ${self.__balance}')

    #Function to withdrawal
    def withdrawal(self):
        withdrawal_money = int(input('\nPlease enter the amount to withdraw : '))
        if self.__balance < withdrawal_money:
            print(f'The account balance is ${self.__balance} which is less than the withdrawal request amount of ${withdrawal_money}')
        else:
            self.time_sleep()
            self.__balance -= withdrawal_money
            print(f'The balance after the withdrawal of ${withdrawal_money} is ${self.__balance}')

    #Function to transfer
    def transfer(self):
        transfer_account = input('\nPlease enter the account number of the recipient : ')
        self.discrimination_pin()
        transfer_money = int(input('Please enter the amount to transfer : '))
        confirmation_Que = input(f'Is \'{transfer_account}\' the correct account number to send? (Y/N) : ')
        if confirmation_Que == 'Y':
            if self.__balance < transfer_money:
                print(f'The account balance is ${self.__balance} which is less than the transfer request amount of ${transfer_money}')
            else:
                self.time_sleep()
                self.__balance -= transfer_money
                print(f'The balance after the transfer of ${transfer_money} is ${self.__balance}')
        else:
            self.transfer()

    #Function to additional tasks
    def additional_task(self):
        answer = input('Are there any additional tasks? (Y/N): ')
        if answer == 'Y':
            print('\n')
            self.discrimination_option()
            print('\n')
            self.additional_task()
        elif answer == 'N':
            pass
        else:
            print('Invalid input. Please re-enter')
            self.additional_task()

    #Function to print receipt
    def receipt(self):
        answer = input('Would you like to get a receipt? (Y/N): ')
        if answer == 'Y':
            print('\nCurrent Time : ')
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print(f'Name : {self.__name}')
            print(f'Account Number : {self.__account_num}')
            print(f'Current Balance : {self.__balance}')
        elif answer == 'N':
            pass
        else:
            print('Invalid input. Please re-enter')
            self.receipt()

        print('\nPlease make sure there are no items left')

    #Function to indicate loading
    def time_sleep(self):
        for _ in range(5):
            print('- ',end='')
            time.sleep(0.5)
        print('\n')

def main(account):

    account.discrimination_card()
    print('\n')
    account.discrimination_pin()
    print('\n')
    account.discrimination_option()
    print('\n')
    account.additional_task()
    print('\n')
    account.receipt()

account = ATM('Hwang Seunghyeon', '1234-1234', 1234, 10000)
main(account)
