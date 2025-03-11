def WordSort(word,order,):
    order_map={}
    for index,char in enumerate(order):
        order_map[char]=index
    def convert_order(word):
        return [order_map[char] for char in word]
    n=len(word)
    for i in range(n):
        for j in range(0,n-i-1):
            n1=word[j]
            n2=word[j+1]
            if(convert_order(n1)>convert_order(n2)):
                word[j],word[j+1]=word[j+1],word[j]
    return word
word=["word", "world", "row"]
order="worldabcefghijkmnpqstuvxyz"
sort_word=WordSort(word,order)
print(sort_word)