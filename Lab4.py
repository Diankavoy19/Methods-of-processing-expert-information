import numpy as np

R1 = np.array([[4, 6, 4, 4, 3],
               [3, 3, 2, 3, 4],
               [2, 2, 1, 2, 2],
               [6, 5, 6, 5, 6],
               [1, 1, 3, 1, 1],
               [5, 4, 5, 6, 5],
               [7, 7, 7, 7, 7]])
print(" Matrix R1 =", R1)
print("The sum of ranks:")
for j in range(0, 7):
    s = 0
    for i in range(0, 5):
        s += R1[j][i]
    print("%3d" % s, end='')
print()
print("Average arithmetic rank")
for j in range(0, 7):
    s = 0
    a = 0
    for i in range(0, 5):
        s += R1[j][i]
        a = s/5.0
    print(a, "", end='')
print()
a = [4.2, 3,1.8,5.6,1.4,5,7]
a.sort()
a.reverse()
print("Sorted middle rank:", a)
a3 = [7,4,6,1,2,3,5]
print("Final ranks of objects by the arithmetic mean method:", a3)
print("Medians of ranks:")
for i in range(0, 7):
    for j in range(0, 7):
        if j == 2:
            a1 = R1[i][j]
            print(a1)
a1 = [4, 2, 1, 6, 3, 5, 7]
a1.sort()
a1.reverse()
print("Sorted median ranks:", a1)
a2 = [7,4,6,1,5,2,3]
print("Final rank by medians:", a2)
print()
print("Comparison of rankings by the arithmetic mean method and the median method:")
print("Factors:1 2 3 4 5 6 7")
print("Final ranks of objects by the arithmetic mean method: 7 4 6 1 2 3 5")
print("Final rank by medians: 7 4 6 1 5 2 3")
print("Conclusion: the rankings are similar, although there are small differences.")
print()
R2 = np.array([[7, 4, 6, 1, 2, 3, 5]])
R3 = np.array([[7, 4, 6, 1, 5, 2, 3]])
R4 = R2-R3
R5 = R4 * R4
print("Checking the consistency of experts' opinions according to Spearman's criterion:")
for j in range(0, 1):
    s = 0
    for i in range(0, 7):
        s += R5[j][i]
        f = 1 - ((6*s)/(7*(7*7-1)))
    print("Spearman's rank correlation coefficient =", f)
print("According to the majestic Spearman rank correlation coefficient, there is a high degree of agreement between the opinions of experts according to the examination." )
R6 = R2 + R3
print("The sum of ranks:", R6)
R7 = np.array([[1, 3.5, 2, 7, 5, 6, 3.5]])
print("The final rank of the factor: ", R7)
p = R7/28.0
print("Weight factor:", p)
print("We calculate the sum of the weights of all 7 factors:")
for j in range(0, 1):
    s = 0
    for i in range (0, 7):
      s += p[j][i]
      print(s)
