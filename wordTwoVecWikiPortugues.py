import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

source = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Jair_Bolsonaro')

prettySoup = bs.BeautifulSoup(source, 'lxml')

text = "".join(paragraph.text for paragraph in prettySoup.find_all('p'))

#Removing part of the text that could cause problems
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)
text = text.lower()
text = re.sub(r'[@#\$%&\*\(\)\<\>\'\":;,.\]\[-]',' ', text)
text = re.sub(r'\d', ' ', text)
text = re.sub(r'\s+', ' ', text)

#Removing stop words
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
sentences = [[word for word in sentences[index] if word not in stopwords.words('Portuguese')] for index in range(len(sentences))]

model = Word2Vec(sentences, min_count=1)

while True:
    frase = input("Digite a palavra para ser encontrada: ")
    try:
        print(model.wv.most_similar(frase))
    except:
        print("Palavra não encontrada")
