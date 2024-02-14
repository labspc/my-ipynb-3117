# 定义一个 BankAccount 类
class BankAccount:
    # __init__ 方法（记作一个 idioms）
    def __init__(self, account_number, balance=0):
        # 一个 idiom：只能在构造函数中，定义和初始化一个新建对象的实例变量
        self._account_number = account_number  # 隐藏账户号码的细节，使用下划线表示私有属性
        self._balance = balance  # 隐藏余额的细节

    def deposit(self, amount): 
    # self是特殊参数变量，amount是普通参数变量
        
        """存款"""
        if amount > 0:
            self._balance += amount # _balance是实例变量

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """获取余额"""
        return self._balance

    def get_account_number(self):
        """获取账户号码"""
        return self._account_number

if __name__ == '__main__':
    main()

