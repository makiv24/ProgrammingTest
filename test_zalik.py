import re
with open('Lab_5.txt', 'r', encoding="utf-8") as f:

    def wordSearch():
        text = f.read().split("\n\n")
        word = str(input("Введіть слово у нижньому реєстрі:"))
        for i in text:
            x = i
            x = re.sub('[?;:()%^&*_+=!@#$-.,—]', '', x)
            x = x.lower()
            x = x.split()

            if word in x:
                print(i, "\n---------")

    wordSearch()
