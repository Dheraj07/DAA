def stringMatch(pattern,text):
    n=len(text)
    m=len(pattern)

    for i in range(n-m+1):
        j=0
        while j<m and text[i+j]==pattern[j]:
            j+=1
        if j==m:
            print("Pattern found at index ",i)
text="THIS IS A TEST TEXT"
pattern="TEXT"
stringMatch(pattern,text)
