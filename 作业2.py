#Action2 统计全班的成绩
import numpy as np
persontype = np.dtype({
    'names':['name','chinese','math','english'],
    'formats':['S32','i','i','i']})
peoples = np.array([("ZhangFei",65,65,30),("GuanYu",95,76,98),
                    ("LiuBei",98,86,88),("DianWei",90,88,77),("XuChu",80,90,90)],
                   dtype=persontype)
chineses = peoples['chinese']
maths = peoples['math']
englishs = peoples['english']

#平均成绩
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

#最小成绩
print(np.min(chineses))
print(np.min(maths))
print(np.min(englishs))

#最大成绩
print(np.max(chineses))
print(np.max(maths))
print(np.max(englishs))

#方差
print(np.var(chineses))
print(np.var(maths))
print(np.var(englishs))

#标准差
print(np.std(chineses))
print(np.std(maths))
print(np.std(englishs))

#排序(从小到大)
print(np.sort(chineses))
print(np.sort(maths))
print(np.sort(englishs))



