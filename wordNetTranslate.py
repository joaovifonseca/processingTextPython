from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

while True:
    frase = input("Digite a frase para ser traduzida: ")
    palavras = frase.split()
    frase_final = ''

    for palavra in frase.split():
        english_words = wordnet.synsets(palavra, lang="por")
        if len(english_words) > 0:
            word = wordnet.synsets(palavra, lang="por")[0]._lemma_names[0]
            frase_final += str(word) + ' '

    print(frase_final)
