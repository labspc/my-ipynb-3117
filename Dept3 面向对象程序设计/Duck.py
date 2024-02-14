# 问题：本例子使用了鸭子🦆类型，多态性具体体现在哪里？
# Python 示例代码
class Duck:
    def quack(self):
        print("Quack")

    def walk(self):
        print("Walk")

class Person:
    def quack(self):
        print("I'm quacking like a duck")

    def walk(self):
        print("I'm walking like a duck")

def make_it_quack(obj):
    #
    obj.quack()


# Client 创建类对象    
duck = Duck() 
person = Person()


make_it_quack(duck)  # 输出：Quack
make_it_quack(person)  # 输出：I'm quacking like a duck

