# Import nltk library and it's sub-modules corpus, tokenize 

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = "I love ML programming. ML programming is very intresting topic. ML has lot of scope in the current market. market is good now."
# text = "I like this product. This product is very useful. Lot of customers given good reviews about this product. But few customers dislike this produt."


stopwords = set(stopwords.words("english"))
words =     word_tokenize(text)
freqTable = dict()

# Tokenize the given text and store it in freqTable dictionary with the count of each words. Exclude stopwords.

for word in words: 
    word = word.lower() 
    if word in stopwords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1 
    else: 
        freqTable[word] = 1
print (freqTable)

sentences = sent_tokenize(text)
sentenceValue = dict()

# Add the score for each sentence in the given text by using the frequency count of each word in the senetence
# and store the sentense and it's scpre in the sentenceValue dictionary.

for sentence in sentences: 
    for word, freq in freqTable.items(): 
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq 
print ('sentence:',sentenceValue)

# Calculate the average value of original text using it's sentence score

sumValues = 0
for sentence in sentenceValue:
    print(sentence) 
    sumValues += sentenceValue[sentence] 
   
print("I am sum value:", sumValues)
average = int(sumValues / len(sentenceValue)) 

print("I am average Value:", average)
   
# Using each sentense score and the hurstic value of 1.2 find the most frequently used sentence in the given text.
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
print("Prints the final results:", summary) 