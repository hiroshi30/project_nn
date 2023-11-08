from pprint import pprint


a = [[[5, 12, 1, 4, 8],
      [7, 1, 13, 11, 0],
      [11, 1, 4, 3, 7],
      [2, 6, 0, 0, 9],
      [1, 20, 4, 8, 3]],
     [[1, 5, 0, -11, 2],
      [8, 9, 0, 0, 3],
      [-7, 3, 18, 1, 0],
      [2, 0, 6, 11, 12],
      [1, -9, 0, 7, 15]],
     [[5, 7, -13, 8, 0],
      [16, 0, 20, 7, -2],
      [11, 6, 1, 0, 3],
      [12, 2, 9, 0, 0],
      [11, 9, 5, -1, 2]]]

w = [[[1, 2, 0],
      [1, 0, -1],
      [-2, 1, -1]],
     [[1, 0, 0],
      [1, 0, 0],
      [0, 1, 1]],
     [[0, -1, -1],
      [0, 0, 0],
      [0, 2, -1]]]


bias = [[1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]]


def padding(a):
    b = []
    for i in range(len(a)):
        b.append([])
        b[i].append([0] * (len(a[i][0]) + 2))
        for j in range(len(a[i])):
            b[i].append([0] + a[i][j] + [0])
        b[i].append([0] * (len(a[i][0]) + 2))

    return b


a = padding(a)

b = [[[0 for l in range(1 + len(a[0][0]) - len(w[0][0]))] for j in range(1 + len(a[0]) - len(w[0]))] for i in range(len(a))]

for i in range(len(a)):
    for j in range(1 + len(a[0]) - len(w[0])):
        for l in range(1 + len(a[0][0]) - len(w[0][0])):
            for mh in range(len(w[0])):
                for mw in range(len(w[0][0])):
                    b[i][j][l] += a[i][j + mh][l + mw] * w[i][mh][mw]

pprint(b)

c = []

for i in range(len(b[0])):
    c.append([])
    for j in range(len(b[0][0])):
        c[i].append(bias[i][j])
        for l in range(len(b)):
            c[i][j] += b[l][i][j]

pprint(c)

d = []

for i in range(len(b[0])):
    d.append([])
    for j in range(len(b[0][0])):
        d[i].append(max(c[i][j], 0))

pprint(d)
