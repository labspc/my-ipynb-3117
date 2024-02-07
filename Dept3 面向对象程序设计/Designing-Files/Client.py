
# By Lambert, 2024.02.07
# The client is separated from the implementation.
# Read the API of the program, click: /Designing-Files/API.md
# Read the implementation of the program, click: /Designing-Files/Implementation.py

from Implementation import BankAccount

# 创建一个 BankAccount 类的对象
account1 = BankAccount("123456", 1000)

# 调用类的方法
print("Account Number:", account1.get_account_number())  # 输出账户号码
print("Balance:", account1.get_balance())  # 输出余额

# 进行存款和取款操作
account1.deposit(500)
account1.withdraw(200)

# 再次打印余额
print("Updated Balance:", account1.get_balance())  # 输出更新后的余额

# Test Output:

# $ python Client.py

# Account Number: 123456
# Balance: 1000
# Updated Balance: 1300
