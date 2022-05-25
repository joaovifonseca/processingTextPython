from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('./cbow_s50.txt')

frase = input("Digite a frase para ser alterada: ")
palavras = frase.split()
frase_final = ''

for palavra in frase.split():
    try:
        palavra_similar = model.most_similar(palavra)
        frase_final += model.most_similar(palavra)[0][0] + ' '
    except:
        frase_final += palavra + ' '

print("Frase final: " + frase_final)
