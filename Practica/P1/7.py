text = input("ingresa varias palabras separadas por espacios: ")
words = text.split()

filtered_words = []

for word in words:
    if len(word) > 3:
        filtered_words.append(word)

final_txt = " ".join(filtered_words)

print(f"texto final: {final_txt}")
