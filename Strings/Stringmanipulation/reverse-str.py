def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result 
print(reverse_string("Hello"))