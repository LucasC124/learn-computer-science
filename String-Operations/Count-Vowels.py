#This code will count vowels so any of ("aeiouAEIOU") will increase the count by one everytime one of them is found in a word that is typed in 
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1 
    print("number of vowels", count)
str = "hellowworld"
vowel_count(str)