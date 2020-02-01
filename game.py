n = 3
m = 3
val = [0] * n
# for x in range (n):
#     val[x] = [0] * m
# print(val)

# val = [""] * n
# for i in range(n):
#     val[i] = [n] * m
# val[1][1] = 0
# print(val)

for i in range(n):
    if i == 0:
        val[i][0] = 1
        val[i][1] = 4
        val[i][2] = 7
    elif i == 1:
        val[i][0] = 2
        val[i][1] = 5
        val[i][2] = 8
    else:
        val[i][0] = 3
        val[i][1] = 6
        val[i][2] = 9

print(val)