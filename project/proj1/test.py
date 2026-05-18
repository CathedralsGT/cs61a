from mpmath import mp

# 1. 严格设置十进制有效数字为 100 位
mp.dps = 100

# 2. 直接获取高精度的 pi 对象
pi_100 = mp.pi

# 打印结果（它会以字符串或高精度 mpf 对象形式完美呈现 100 位）
print(f"mpmath 计算的 100 位 Pi:\n{pi_100}")