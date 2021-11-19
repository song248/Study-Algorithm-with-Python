def solution(n, number):
    arr = [0] + [{int(str(n)*i)} for i in range(1, 9)]
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in arr[j]:
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num2 - num1)
                    arr[i].add(num1 * num2)
                    if num2 != 0:    arr[i].add(num1 // num2)
                    if num1 != 0:    arr[i].add(num2 // num1)
        if number in arr[i]:
            return i
    return -1