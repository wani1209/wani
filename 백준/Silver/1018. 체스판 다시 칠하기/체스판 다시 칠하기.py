n, m = map(int, input().split())
l = []
result = []
for _ in range(n):
    l.append(input())
for i in range(n-7):
    for j in range(m-7):
        d1 = 0 ; d2 = 0
        
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if l[a][b] != 'B':
                        d1 += 1
                    if l[a][b] != 'W':
                        d2 += 1
                else:
                    if l[a][b] != 'W':
                        d1 += 1
                    if l[a][b] != 'B':
                        d2 += 1
        result.append(d1)
        result.append(d2)
print(min(result))