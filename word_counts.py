word_count={}

with open ("poem.txt","r") as f:
    for line in f:
        words =line.split(' ')
        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
print(word_count)

word_occurance = list(word_count.values())
max_count=max(word_occurance)
print("max occurances of any word is: ",max_count)
print("words with max occurances are: ")
for word ,count in word_count.items():
    if count == max_count:
        print(word)
        
