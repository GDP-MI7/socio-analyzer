import nltk

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

print(stemmer.stem("beautiful"))
print(stemmer.stem("beautic"))
print(stemmer.stem("beautiness"))
print(stemmer.stem("beautify"))


print(stemmer.stem("go"))
print(stemmer.stem("went"))
print(stemmer.stem("gone"))
print(stemmer.stem("going"))
