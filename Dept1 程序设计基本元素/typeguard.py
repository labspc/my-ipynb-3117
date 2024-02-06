from typing import Literal

op: Literal[10] = 1+2+3  # 这会在类型检查时报错，因为 1+2+3 的结果不是 10
print(op)
res = op/4
print(res)