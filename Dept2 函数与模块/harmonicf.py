#-----------------------------------------------------------------------
# harmonicf.py
# https://introcs.cs.princeton.edu/python/21function/harmonicf.py.html
#-----------------------------------------------------------------------

import stdio
import sys

# Return the nth harmonic number.
def harmonic(n): # n代表调和数的阶数
    total = 0.0

    # 这就是 Python 中实现调和数的函数的主要代码
    for i in range(1, n+1):
        # total += 1.0 / float(i)
        total = total + 1.0 / float(i)
    return total

# Write to standard output the harmonic numbers specified as
# command-line arguments.

for j in range(1, len(sys.argv)):

    arg = int(sys.argv[j]) #获取命令行参数，并进行显式类型转换
    value = harmonic(arg) # arg = n，调用调和数函数，返回值 total，再赋值给 value
    stdio.writeln(value) 
