# my_module.py

def public_function():
    print("This is a public function.")

def _private_function():
    print("This is a private function, only for internal use.")

# 在模块内部调用私有函数
_private_function()
