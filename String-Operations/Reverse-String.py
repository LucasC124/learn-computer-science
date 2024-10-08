#This code reverse any word inputted in such as 'hello' which becomes 'olleh'
def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result 
print(reverse_string("Hello"))