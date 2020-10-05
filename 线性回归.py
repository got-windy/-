import matplotlib.pyplot as plt

p0 = 0
p1 = 0
# 步长
erf = 0.01
min = 0.000001

x = [1, 2, 3,3, 3,4, 5, 6, 7, 8, 9, 10, 11, 12 ]
y = [20, 22, 24,25,26,25, 27, 29, 31, 33, 35 , 37,41,41]
n = len(x)
plt.scatter(x, y, s=10)

def a(n):
    p = 0
    for i in range(n):
        p += p0 + x[i] * p1 - y[i]
    return p*1/n


def b(n):
    p = 0
    for i in range(n):
        p += (p0 + x[i] * p1 - y[i]) * x[i]
    return p*1/n


j_p0 = a(n)
j_p1 = b(n)
while j_p0 ** 2 >= min or j_p1 ** 2 >= min:
    p0 = p0 - erf*j_p0
    p1 = p1 - erf*j_p1

    j_p0 = a(n)
    j_p1 = b(n)


print(p0, p1)
plt.plot(x, [p0 + p1*i for i in x],  linewidth=1)
plt.show()