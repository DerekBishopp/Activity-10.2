__author__ = 'Derek'
m = [1, 3, 2, 4, 5, 7, 6, 8]

for i in range(len(m)-1):

    x = i+1
    if int(m[i]) > int(m[x]):
        q = m[x]
        m[x] = m[i]
        m[i] = q
print(m)
