n_zip = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    n_zip.append((a,b))
dungchi = []
for a in n_zip:
    grade = 1
    for b in n_zip:
        if a[0] < b[0] and a[1] < b[1]:
            grade += 1
    dungchi.append(grade)
for i in dungchi:
    print(i, end = ' ')