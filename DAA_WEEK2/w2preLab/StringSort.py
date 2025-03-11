str="You are extraordinally talented, displaying a wide range of skills and abilities"

words=str.split()
print(words)

n=len(words)
for i in range(0,n):
    for j in range(0,n-i-1):
        if len(words[j])>len(words[j+1]):
            words[j],words[j+1]=words[j+1],words[j]
result=' '.join(words)
print(result)