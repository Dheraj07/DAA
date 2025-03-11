def rabin_karp(text,pattern,prime=101):
    m=len(pattern)
    n=len(text)
    pattern_hash=0
    text_hash=0
    base=256
    result=[]

    h=1
    for i in range(m-1):
        h=(h*base)%prime
    for i in range(m):
        pattern_hash=(base*pattern_hash+ord(pattern[i]))%prime
        text_hash=(base*text_hash+ord(text[i]))%prime
    for i in range(n-m+1):
        if text_hash==pattern_hash:
            if text[i:i+m]==pattern:
                result.append(i)
        if i<n-m:
            text_hash=(base*(text_hash-ord(text[i])*h)+ord(text[i+m]))%prime
            if text_hash<0:
                text_hash+=prime
    return result
text="GEEKS FOR GEEKS"
pattern="FOR"
res=rabin_karp(text,pattern)
print(res)