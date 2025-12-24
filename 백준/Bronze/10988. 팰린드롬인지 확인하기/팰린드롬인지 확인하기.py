word = input()
word_list = list(word)
n = len(word_list)
num = 1
for i in range(n//2):
    if word_list[i] == word_list[n-i-1]:
        num =1
        pass
    else:
        num =0
        break
print(num)
