translation_dict = {
    "c": "gato",
    "d": "perro",
    "a": "manzana",
    "r": "car",
}
text = input("please select a word")
translation_table = str.maketrans(translation_dict)
translated_text = text.translate(translation_table)
print(translated_text)
