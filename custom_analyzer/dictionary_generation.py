#Script to clasify words as positive negative neutral
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import vader
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

sia = vader.SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

#Specify the file paths
positiveReviewsFileName = "../input_files/trainingData.txt"
# positiveReviewsFileName = "../input_files/rt-polarity.pos"
# negativeReviewsFileName = "../input_files/rt-polarity.neg"

positiveWords = []
negativeWords = []
neutralWords = []

def getSentiment(word):
    polarity = sia.polarity_scores(word)['compound']
    word = stemmer.stem(word)
    if polarity > 0:
        positiveWords.append(word)
    elif polarity < 0:
        negativeWords.append(word)
    else:
        neutralWords.append(word)

#Read the files and collect the data
with open(positiveReviewsFileName,'r') as f:
    for line in f.readlines():
        word_tokens =[w for w in word_tokenize(line) if not w in stop_words]
        for word in word_tokens:
            getSentiment(word)

# with open(negativeReviewsFileName,'r') as f:
#     for line in f.readlines():
#         word_tokens =[w for w in word_tokenize(line) if not w in stop_words]
#         for word in word_tokens:
#             getSentiment(word)

# print(set(positiveWords))

positiveWordsSet = set(positiveWords)
negativeWordsSet = set(negativeWords)
neutralWordsSet = set(neutralWords)

print("No of positive words ", len(positiveWordsSet))
print("No of negative words ", len(negativeWordsSet))
print("No of neutral words ", len(neutralWordsSet))

positiveWordsFileName = "../output_files/pos.txt"
negativeWordsFileName = "../output_files/neg.txt"
neutralWordsFileName = "../output_files/neu.txt"


posF = open(positiveWordsFileName,'w') 
negF = open(negativeWordsFileName,'w') 
neuF = open(neutralWordsFileName,'w') 

for word in positiveWordsSet:
    posF.write(word + "\n")
for word in negativeWordsSet:
    negF.write(word + "\n")
for word in neutralWordsSet:
    neuF.write(word + "\n")

posF.close()
negF.close()
neuF.close()

print('Data ready...')