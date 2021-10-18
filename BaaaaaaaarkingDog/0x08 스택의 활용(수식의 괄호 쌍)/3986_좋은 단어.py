cnt = 0
for i in range(int(input())):
    word = input()
    stack = []
    for s in word:
        if not stack:    
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    if not stack:
        cnt += 1
print(cnt)


num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		temp, word = word, word.replace("AA", "").replace("BB", "")
	if not word:
		num_of_good_words += 1

print(num_of_good_words)