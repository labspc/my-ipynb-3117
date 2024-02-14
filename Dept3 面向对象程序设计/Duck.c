// C 示例代码
#include <stdio.h>

// 定义鸭子类型的函数
void make_it_quack(void (*quack)()) {
    quack();
}

// 定义鸭子对象
void duck_quack() {
    printf("Quack\n");
}

// 定义人类对象
void person_quack() {
    printf("I'm quacking like a duck\n");
}

int main() {
    // 传递鸭子对象
    make_it_quack(duck_quack);  // 输出：Quack
    
    // 传递人类对象
    make_it_quack(person_quack);  // 输出：I'm quacking like a duck
    
    return 0;
}
