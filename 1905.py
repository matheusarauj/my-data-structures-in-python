# URI 1905 - Polícia e Ladrão

winner = False
result = []

def find(mat, coord, i, j):
    global winner
    if(i >= 0 and i < 5 and j >= 0 and j < 5 and not winner):
        coord[i][j]['visited'] = True
        if(i == 4 and j == 4):
            winner = True
        else:
            if(j + 1 < 5 and mat[i][j+1] == 0 and not coord[i][j+1]['visited'] ):
                find(mat, coord, i, j+1)
            if(j - 1 >= 0 and mat[i][j-1] == 0 and not coord[i][j-1]['visited'] ):
                find(mat, coord, i, j-1)
            if(i + 1 < 5 and mat[i+1][j] == 0 and not coord[i+1][j]['visited'] ):
                find(mat, coord, i+1, j)
            if(i - 1 >= 0 and mat[i-1][j] == 0 and not coord[i-1][j]['visited'] ):
                find(mat, coord, i-1, j)

t = int(input())
for i in range(t):
    coord = [[{"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}],
            [{"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}],
            [{"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}],
            [{"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}],
            [{"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}, {"x": 0, "y": 0, "visited": False}]
            ]
    mat = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    
    j = 0
    while j < 5:
        e = list(map(int, input().split()))
        if(len(e) == 5):
            for k in range(5):
                mat[j][k] = e[k]

                coord[j][k]['x'] = j
                coord[j][k]['y'] = k
                coord[j][k]['visited'] = False
            j += 1
   
    winner = False

    if(mat[0][0] == 0 and mat[4][4] == 0):
        find(mat, coord, 0, 0)

    if(winner):
        result.append("COPS")
    else:
        result.append("ROBBERS")
for i in result:
    print(i)


