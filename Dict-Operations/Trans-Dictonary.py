#This code has the firdt letters of words and the spanish trnaklsation of them for example 'c' = 'gatto' which is cat in english 
#The text will then ask for ones of these letters and will then print the spanish translation out 
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
