本节代码 `BankAccount` 类的 `API` 文档如下：


| 方法名               | 描述                   | 参数                          | 返回值             |
|---------------------|------------------------|-------------------------------|-------------------|
| \_\_init\_\_        | 创建银行账户对象         | account_number (str), balance=0 (float) | 无               |
| deposit             | 存款到账户中             | amount (float)                | 无               |
| withdraw            | 从账户中取款             | amount (float)                | 无或错误信息      |
| get_balance         | 获取账户的余额           | 无                            | balance (float)   |
| get_account_number  | 获取账户的账号           | 无                            | account_number (str) |

这个表格清晰地展示了 BankAccount 类的每个方法的名称、描述、参数以及返回值。用户可以根据这个表格了解如何使用这些方法来操作银行账户对象。