import os
import sys
from googletrans import Translator
import inquirer

sys.path.append(os.path.realpath("."))
translator = Translator()

list_linguas = [
            ("Português", "pt"),
            ("Espanhol", "es"),
            ("Inglês", "en"),
            ("Francês", "fr")
        ]

while True:
    text = input("Digite o texto para ser traduzido: ")

    questions = [
        inquirer.List(
            "size",
            message="Para qual língua quer traduzir o texto?",
            choices=list_linguas,
        ),
    ]

    answers = inquirer.prompt(questions)

    print('Texto traduzido: ')
    translation = translator.translate(text, dest=answers['size'])
    print(translation.text)