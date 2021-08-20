def hundred(arrr):
    for i in range(len(arrr)):
        for j in range(len(arrr)):
            if i == j:  pass
            else:  
                if arrr[i] + arrr[j] == 100:
                    return 1
    return 0
	
print(hundred([1,52,48]))
print(hundred([50,42]))
print(hundred([4,13,63,87]))